from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class LoanProduct(Base):
    __tablename__ = "loan_products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False, index=True)
    interest_rate = Column(Float, nullable=False)
    max_amount = Column(Float, nullable=False)
    tenure_months = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    loan_applications = relationship("LoanApplication", back_populates="loan_product")
