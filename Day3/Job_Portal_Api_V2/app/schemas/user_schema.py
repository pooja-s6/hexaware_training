#user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional
 
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str
    
#Create User
class UserCreate(UserBase):
    password: str
    company_id: Optional[int] = None
    
#Update User
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
 
#Response User
class UserResponse(UserBase):
    id: int
    company_id: Optional[int] = None
 
    class Config:
        from_attributes = True
 