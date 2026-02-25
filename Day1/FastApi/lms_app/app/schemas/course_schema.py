from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str
    duration: int

class CourseResponse(CourseCreate):
    id: int