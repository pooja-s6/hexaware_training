#employer_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_employer
from app.controllers.employer_controller import (
    create_job_controller,
    get_my_jobs_controller,
    delete_job_controller,
    get_job_applications_controller
)
from app.schemas.job_schema import JobCreate, JobResponse

router = APIRouter(prefix="/employer", tags=["Employer"])

#Create job
@router.post("/jobs", response_model=JobResponse)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_employer)
):
    return create_job_controller(job_data, current_user.id, db)

#Get my posted jobs
@router.get("/jobs")
def get_my_jobs(
    db: Session = Depends(get_db),
    current_user = Depends(require_employer)
):
    return get_my_jobs_controller(current_user.id, db)

#Delete job
@router.delete("/jobs/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_employer)
):
    return delete_job_controller(job_id, current_user.id, db)

#Get applications for a job
@router.get("/jobs/{job_id}/applications")
def get_job_applications(
    job_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_employer)
):
    return get_job_applications_controller(job_id, db)
