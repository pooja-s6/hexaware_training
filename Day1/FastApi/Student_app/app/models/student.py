from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    age: int
    courses: str
    active: bool