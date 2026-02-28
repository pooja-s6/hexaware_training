from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title: str
    description: str
    company_email: str
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    company_email: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True
