from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentResponse(StudentCreate):
    id: int