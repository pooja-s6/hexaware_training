#company_repo.py
from sqlalchemy.orm import Session
from app.models.company import Company
#Create Company
def create_company(db: Session, company_data: dict) -> Company:
    db_company = Company(**company_data)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
#Get Company by ID
def get_company_by_id(db: Session, company_id: int) -> Company:
    return db.query(Company).filter(Company.id == company_id).first()

#Get All Companies
def get_all_companies(db: Session) -> list[Company]:
    return db.query(Company).all()

#Delete Company by ID
def delete_company_by_id(db: Session, company_id: int) -> None:
    company = db.query(Company).filter(Company.id == company_id).first()
    if company:
        db.delete(company)
        db.commit()