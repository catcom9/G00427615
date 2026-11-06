def record_payload():
        return {
                "equipment_id": 4,
                "student_id": "ST-AB0571",
                "description": "Fix this please",
                "priority": 2
        }

def test_create_records(client):
    client.post("/requests", json = record_payload())

    response = client.get("/requests")

    assert response.status_code == 200

