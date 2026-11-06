from sqlite3 import IntegrityError

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from app.database import get_db, Session
from app.schemas import RecordCreate, RecordRead
from app.models import MaintenanceDB

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}


@app.post("/requests",
          response_model=RecordRead,
          status_code=status.HTTP_201_CREATED)
def saveRequest(new_record: RecordCreate,
                db: Session = Depends(get_db)):
    db_record = MaintenanceDB(**new_record.model_dump())
    db_record.status = "OPEN"
    db.add(db_record)
    try:
        db.commit()
        db.refresh(db_record)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=404, detail="Failed to create record")
    
    return db_record

@app.get("/requests",
         response_model=list[RecordRead])
def readRequest(db: Session = Depends(get_db)):
    statment = select(MaintenanceDB.order_by(MaintenanceDB.id))
    return db.execute(statment).scalars().all()
