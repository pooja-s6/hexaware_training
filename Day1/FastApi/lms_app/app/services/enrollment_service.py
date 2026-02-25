from fastapi import HTTPException
from app.repositories import student_repository, course_repository, enrollment_repository

def enroll_student(enrollment):

    student = student_repository.get_student(enrollment.student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    course = course_repository.get_course(enrollment.course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    existing = enrollment_repository.get_existing(
        enrollment.student_id, enrollment.course_id
    )
    if existing:
        raise HTTPException(status_code=400, detail="Already enrolled")

    return enrollment_repository.create_enrollment(enrollment)