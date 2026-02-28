from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.company_repository import CompanyRepository
from app.schemas.company_schema import CompanyCreate, CompanyUpdate

class CompanyService:
    def __init__(self, db: Session):
        self.db = db
        self.company_repo = CompanyRepository(db)
    
    def create_company(self, company_data: CompanyCreate):
        # Check if company already exists
        existing_company = self.company_repo.get_company_by_email(company_data.email)
        if existing_company:
            raise HTTPException(status_code=400, detail="Company email already registered")
        
        # Create company
        company_dict = company_data.model_dump()
        company = self.company_repo.create_company(company_dict)
        return company
    
    def get_company_by_email(self, email: str):
        company = self.company_repo.get_company_by_email(email)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        return company
    
    def update_company(self, email: str, update_data: CompanyUpdate):
        company = self.company_repo.get_company_by_email(email)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        update_dict = update_data.model_dump(exclude_unset=True)
        updated_company = self.company_repo.update_company(company, update_dict)
        return updated_company
    
    def delete_company(self, email: str):
        company = self.company_repo.get_company_by_email(email)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        self.company_repo.delete_company(company)
