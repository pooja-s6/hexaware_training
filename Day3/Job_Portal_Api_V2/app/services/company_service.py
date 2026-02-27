#company_service.py

from sqlalchemy.orm import Session
from app.repositories.company_repo import (
    create_company,
    get_company_by_id,
    get_all_companies,
    delete_company_by_id
)
from app.schemas.company_schema import CompanyCreate

#Create new company
def create_new_company(db: Session, company_data: CompanyCreate):
    company_dict = company_data.model_dump()
    new_company = create_company(db, company_dict)
    return new_company

#Get company by ID
def get_company(db: Session, company_id: int):
    company = get_company_by_id(db, company_id)
    if not company:
        raise ValueError("Company not found")
    return company

#Get all companies
def get_all_company_list(db: Session):
    return get_all_companies(db)

#Delete company
def delete_company(db: Session, company_id: int):
    company = get_company_by_id(db, company_id)
    if not company:
        raise ValueError("Company not found")
    
    delete_company_by_id(db, company_id)
    return {"message": "Company deleted successfully"}
