#job_repo.py
from sqlalchemy.orm import Session
from app.models.job import Job
#Create Job
def create_job(db: Session, job_data: dict) -> Job:
    db_job = Job(**job_data)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
#Get Job by ID
def get_job_by_id(db: Session, job_id: int) -> Job:
    return db.query(Job).filter(Job.id == job_id).first()
#Get All Jobs
def get_all_jobs(db: Session) -> list[Job]:
    return db.query(Job).all()
#Get Jobs by Company
def get_jobs_by_company(db: Session, company_id: int) -> list[Job]:
    return db.query(Job).filter(Job.company_id == company_id).all()
#Get Jobs by Creator
def get_jobs_by_creator(db: Session, user_id: int) -> list[Job]:
    return db.query(Job).filter(Job.created_by == user_id).all()

#Delete Job by ID
def delete_job_by_id(db: Session, job_id: int) -> None:
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
