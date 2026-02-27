#application_repo.py
from sqlalchemy.orm import Session
from app.models.application import Application
#Create Application
def create_application(db: Session, application_data: dict) -> Application:
    db_application = Application(**application_data)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application
#Get Application by ID
def get_application_by_id(db: Session, application_id: int) -> Application:
    return db.query(Application).filter(Application.id == application_id).first()
#Get All Applications
def get_all_applications(db: Session) -> list[Application]:
    return db.query(Application).all()
#Get Applications by Candidate
def get_applications_by_candidate(db: Session, candidate_id: int) -> list[Application]:
    return db.query(Application).filter(Application.candidate_id == candidate_id).all()
#Get Applications by Job
def get_applications_by_job(db: Session, job_id: int) -> list[Application]:
    return db.query(Application).filter(Application.job_id == job_id).all()

#Delete Application by ID
def delete_application_by_id(db: Session, application_id: int) -> None:
    application = db.query(Application).filter(Application.id == application_id).first()
    if application:
        db.delete(application)
        db.commit()
