from pydantic import BaseModel, EmailStr
from typing import Optional

class ApplicationBase(BaseModel):
    job_id: int
    applicant_email: EmailStr
    cover_letter: Optional[str] = None
    resume_url: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    job_id: Optional[int] = None
    applicant_email: Optional[EmailStr] = None
    status: Optional[str] = None
    cover_letter: Optional[str] = None
    resume_url: Optional[str] = None

class ApplicationResponse(ApplicationBase):
    id: int
    status: str

    class Config:
        from_attributes = True
