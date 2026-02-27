#application_service.py

from sqlalchemy.orm import Session
from app.repositories.application_repo import (
    create_application,
    get_application_by_id,
    get_all_applications,
    get_applications_by_candidate,
    get_applications_by_job,
    delete_application_by_id
)
from app.repositories.job_repo import get_job_by_id
from app.schemas.application_schema import ApplicationCreate

#Apply to a job
def apply_to_job(db: Session, application_data: ApplicationCreate, candidate_id: int):
    #Check if job exists
    job = get_job_by_id(db, application_data.job_id)
    if not job:
        raise ValueError("Job not found")
    
    application_dict = application_data.model_dump()
    application_dict["candidate_id"] = candidate_id
    application_dict["status"] = "applied"
    
    new_application = create_application(db, application_dict)
    return new_application

#Get application by ID
def get_application(db: Session, application_id: int):
    application = get_application_by_id(db, application_id)
    if not application:
        raise ValueError("Application not found")
    return application

#Get my applications
def get_my_applications(db: Session, candidate_id: int):
    return get_applications_by_candidate(db, candidate_id)

#Get applications for a job
def get_job_applications(db: Session, job_id: int):
    return get_applications_by_job(db, job_id)

#Get all applications
def get_all_application_list(db: Session):
    return get_all_applications(db)

#Cancel application
def cancel_application(db: Session, application_id: int, candidate_id: int):
    application = get_application_by_id(db, application_id)
    if not application:
        raise ValueError("Application not found")
    
    if application.candidate_id != candidate_id:
        raise ValueError("Not authorized to cancel this application")
    
    delete_application_by_id(db, application_id)
    return {"message": "Application cancelled successfully"}
