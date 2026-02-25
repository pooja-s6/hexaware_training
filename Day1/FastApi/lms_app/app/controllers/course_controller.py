from fastapi import APIRouter
from app.schemas import course_schema
from app.services import course_service

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/")
def create_course(course: course_schema.CourseCreate):
    return course_service.create_course(course)

@router.get("/")
def get_all_courses():
    return course_service.get_all_courses()

@router.get("/{course_id}")
def get_course(course_id: int):
    return course_service.get_course(course_id)