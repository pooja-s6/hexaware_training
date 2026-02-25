from fastapi import APIRouter
from app.schemas import student_schema
from app.services import student_service

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def create_student(student: student_schema.StudentCreate):
    return student_service.create_student(student)

@router.get("/{student_id}")
def get_student(student_id: int):
    return student_service.get_student(student_id)