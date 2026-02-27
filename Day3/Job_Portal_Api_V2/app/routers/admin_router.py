#admin_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_admin
from app.controllers.admin_controller import (
    get_all_users_controller,
    delete_user_controller,
    create_company_controller,
    get_all_companies_controller,
    delete_company_controller,
    get_all_applications_controller
)
from app.schemas.company_schema import CompanyCreate, CompanyResponse

router = APIRouter(prefix="/admin", tags=["Admin"])

#Get all users
@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return get_all_users_controller(db)

#Delete user
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return delete_user_controller(user_id, db)

#Create company
@router.post("/companies", response_model=CompanyResponse)
def create_company(
    company_data: CompanyCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return create_company_controller(company_data, db)

#Get all companies
@router.get("/companies")
def get_all_companies(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return get_all_companies_controller(db)

#Delete company
@router.delete("/companies/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return delete_company_controller(company_id, db)

#Get all applications
@router.get("/applications")
def get_all_applications(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return get_all_applications_controller(db)
