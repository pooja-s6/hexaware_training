#candidate_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_candidate
from app.controllers.candidate_controller import (
    get_all_jobs_controller,
    get_job_details_controller,
    apply_to_job_controller,
    get_my_applications_controller,
    cancel_application_controller
)
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.schemas.job_schema import JobResponse

router = APIRouter(prefix="/candidate", tags=["Candidate"])

#Get all jobs
@router.get("/jobs")
def get_all_jobs(db: Session = Depends(get_db)):
    return get_all_jobs_controller(db)

#Get job details
@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job_details(job_id: int, db: Session = Depends(get_db)):
    return get_job_details_controller(job_id, db)

#Apply to job
@router.post("/applications", response_model=ApplicationResponse)
def apply_to_job(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_candidate)
):
    return apply_to_job_controller(application_data, current_user.id, db)

#Get my applications
@router.get("/applications")
def get_my_applications(
    db: Session = Depends(get_db),
    current_user = Depends(require_candidate)
):
    return get_my_applications_controller(current_user.id, db)

#Cancel application
@router.delete("/applications/{application_id}")
def cancel_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_candidate)
):
    return cancel_application_controller(application_id, current_user.id, db)
