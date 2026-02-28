from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    company_email = Column(String)
    location = Column(String)
    salary = Column(String)
    job_type = Column(String)
