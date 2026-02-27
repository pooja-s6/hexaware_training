#employer_controller.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.services.job_service import create_new_job, get_my_jobs, delete_job
from app.services.application_service import get_job_applications
from app.schemas.job_schema import JobCreate, JobResponse

#Create job controller
def create_job_controller(job_data: JobCreate, user_id: int, db: Session):
    try:
        new_job = create_new_job(db, job_data, user_id)
        return JobResponse.model_validate(new_job)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

#Get my posted jobs controller
def get_my_jobs_controller(user_id: int, db: Session):
    jobs = get_my_jobs(db, user_id)
    return [JobResponse.model_validate(job) for job in jobs]

#Delete job controller
def delete_job_controller(job_id: int, user_id: int, db: Session):
    try:
        result = delete_job(db, job_id, user_id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )

#Get applications for job controller
def get_job_applications_controller(job_id: int, db: Session):
    applications = get_job_applications(db, job_id)
    return applications
