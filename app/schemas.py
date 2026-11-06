from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

class RecordCreate(BaseModel):
    equipment_id: int
    student_id: str
    description: Annotated[str, StringConstraints(min_length=5, max_length=100)]
    priority: int = Field(gt=1, lt=5)

class RecordRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
    equipment_id: int
    student_id: str
    description: Annotated[str, StringConstraints(min_length=5, max_length=100)]
    priority: int = Field(gt=1, lt=5)
    status: str

