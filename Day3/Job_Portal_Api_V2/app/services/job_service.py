#job_service.py

from sqlalchemy.orm import Session
from app.repositories.job_repo import (
    create_job, 
    get_job_by_id, 
    get_all_jobs,
    get_jobs_by_company,
    get_jobs_by_creator,
    delete_job_by_id
)
from app.schemas.job_schema import JobCreate

#Create new job
def create_new_job(db: Session, job_data: JobCreate, user_id: int):
    job_dict = job_data.model_dump()
    job_dict["created_by"] = user_id
    new_job = create_job(db, job_dict)
    return new_job

#Get job by ID
def get_job(db: Session, job_id: int):
    job = get_job_by_id(db, job_id)
    if not job:
        raise ValueError("Job not found")
    return job

#Get all jobs
def get_all_job_listings(db: Session):
    return get_all_jobs(db)

#Get jobs by company
def get_company_jobs(db: Session, company_id: int):
    return get_jobs_by_company(db, company_id)

#Get jobs created by user
def get_my_jobs(db: Session, user_id: int):
    return get_jobs_by_creator(db, user_id)

#Delete job
def delete_job(db: Session, job_id: int, user_id: int):
    job = get_job_by_id(db, job_id)
    if not job:
        raise ValueError("Job not found")
    
    if job.created_by != user_id:
        raise ValueError("Not authorized to delete this job")
    
    delete_job_by_id(db, job_id)
    return {"message": "Job deleted successfully"}
