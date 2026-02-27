#auth_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.user_schema import UserCreate, UserResponse
from pydantic import BaseModel
router = APIRouter(prefix="/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    email: str
    password: str
#Register endpoint
@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_controller(user_data, db)
#Login endpoint
@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(login_data.email, login_data.password, db)
