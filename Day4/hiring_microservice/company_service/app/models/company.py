from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    description = Column(String)
    location = Column(String)
    industry = Column(String)
