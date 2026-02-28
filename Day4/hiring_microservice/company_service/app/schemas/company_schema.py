from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    email: EmailStr
    description: Optional[str] = None
    location: Optional[str] = None
    industry: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None
    location: Optional[str] = None
    industry: Optional[str] = None

class CompanyResponse(CompanyBase):
    id: int

    class Config:
        from_attributes = True
