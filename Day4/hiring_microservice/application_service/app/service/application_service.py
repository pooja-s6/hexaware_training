from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.application_repository import ApplicationRepository
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate

class ApplicationService:
    def __init__(self, db: Session):
        self.db = db
        self.application_repo = ApplicationRepository(db)
    
    def create_application(self, application_data: ApplicationCreate):
        # Create application
        application_dict = application_data.model_dump()
        application_dict['status'] = 'pending'  # Set default status
        application = self.application_repo.create_application(application_dict)
        return application
    
    def get_application_by_id(self, application_id: int):
        application = self.application_repo.get_application_by_id(application_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        return application
    
    def update_application(self, application_id: int, update_data: ApplicationUpdate):
        application = self.application_repo.get_application_by_id(application_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        
        update_dict = update_data.model_dump(exclude_unset=True)
        updated_application = self.application_repo.update_application(application, update_dict)
        return updated_application
    
    def delete_application(self, application_id: int):
        application = self.application_repo.get_application_by_id(application_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        
        self.application_repo.delete_application(application)
