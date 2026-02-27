#admin_controller.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repo import get_all_users, delete_user_by_id
from app.services.company_service import create_new_company, get_all_company_list, delete_company
from app.services.application_service import get_all_application_list
from app.schemas.company_schema import CompanyCreate, CompanyResponse
from app.schemas.user_schema import UserResponse

#Get all users controller
def get_all_users_controller(db: Session):
    users = get_all_users(db)
    return [UserResponse.model_validate(user) for user in users]

#Delete user controller
def delete_user_controller(user_id: int, db: Session):
    delete_user_by_id(db, user_id)
    return {"message": "User deleted successfully"}

#Create company controller
def create_company_controller(company_data: CompanyCreate, db: Session):
    try:
        company = create_new_company(db, company_data)
        return CompanyResponse.model_validate(company)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

#Get all companies controller
def get_all_companies_controller(db: Session):
    companies = get_all_company_list(db)
    return [CompanyResponse.model_validate(company) for company in companies]

#Delete company controller
def delete_company_controller(company_id: int, db: Session):
    try:
        result = delete_company(db, company_id)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

#Get all applications controller
def get_all_applications_controller(db: Session):
    applications = get_all_application_list(db)
    return applications
