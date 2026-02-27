#candidate_controller.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.services.job_service import get_all_job_listings, get_job
from app.services.application_service import apply_to_job, get_my_applications, cancel_application
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.schemas.job_schema import JobResponse

#Get all jobs controller
def get_all_jobs_controller(db: Session):
    jobs = get_all_job_listings(db)
    return [JobResponse.model_validate(job) for job in jobs]

#Get job details controller
def get_job_details_controller(job_id: int, db: Session):
    try:
        job = get_job(db, job_id)
        return JobResponse.model_validate(job)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

#Apply to job controller
def apply_to_job_controller(application_data: ApplicationCreate, candidate_id: int, db: Session):
    try:
        application = apply_to_job(db, application_data, candidate_id)
        return ApplicationResponse.model_validate(application)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

#Get my applications controller
def get_my_applications_controller(candidate_id: int, db: Session):
    applications = get_my_applications(db, candidate_id)
    return [ApplicationResponse.model_validate(app) for app in applications]

#Cancel application controller
def cancel_application_controller(application_id: int, candidate_id: int, db: Session):
    try:
        result = cancel_application(db, application_id, candidate_id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
