from fastapi import APIRouter
from app.schemas import enrollment_schema
from app.services import enrollment_service
from app.repositories import enrollment_repository

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/")
def enroll(enrollment: enrollment_schema.EnrollmentCreate):
    return enrollment_service.enroll_student(enrollment)

@router.get("/")
def get_all_enrollments():
    return enrollment_repository.get_all_enrollments()