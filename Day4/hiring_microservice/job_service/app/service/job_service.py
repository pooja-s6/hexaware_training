from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.job_repository import JobRepository
from app.schemas.job_schema import JobCreate, JobUpdate

class JobService:
    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)
    
    def create_job(self, job_data: JobCreate):
        # Create job
        job_dict = job_data.model_dump()
        job = self.job_repo.create_job(job_dict)
        return job
    
    def get_job_by_id(self, job_id: int):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return job
    
    def update_job(self, job_id: int, update_data: JobUpdate):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        
        update_dict = update_data.model_dump(exclude_unset=True)
        updated_job = self.job_repo.update_job(job, update_dict)
        return updated_job
    
    def delete_job(self, job_id: int):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        
        self.job_repo.delete_job(job)
