from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer)
    applicant_email = Column(String)
    status = Column(String, default='pending')  # 'pending', 'approved', 'rejected'
    cover_letter = Column(String)
    resume_url = Column(String)