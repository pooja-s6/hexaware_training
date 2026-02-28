# Company router
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.service.company_service import CompanyService
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyResponse

router = APIRouter(prefix="/companies", tags=["Companies"])

# Dependency to get the CompanyService with the DB session
def get_company_service(db: Session = Depends(get_db)):
    return CompanyService(db)

@router.post("/register", response_model=CompanyResponse)
def create_company(
    payload: CompanyCreate,
    company_service: CompanyService = Depends(get_company_service)
):
    return company_service.create_company(payload)

@router.get("/{email}", response_model=CompanyResponse)
def get_company(
    email: str,
    company_service: CompanyService = Depends(get_company_service)
):
    return company_service.get_company_by_email(email)

@router.put("/{email}", response_model=CompanyResponse)
def update_company(
    email: str,
    payload: CompanyUpdate,
    company_service: CompanyService = Depends(get_company_service)
):
    return company_service.update_company(email, payload)

@router.delete("/{email}")
def delete_company(
    email: str,
    company_service: CompanyService = Depends(get_company_service)
):
    company_service.delete_company(email)
    return {"message": "Company deleted successfully"}
