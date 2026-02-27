#auth_controller.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth_service import register_user, login_user
from app.schemas.user_schema import UserCreate, UserResponse

#Register controller
def register_controller(user_data: UserCreate, db: Session):
    try:
        new_user = register_user(db, user_data)
        return UserResponse.model_validate(new_user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

#Login controller
def login_controller(email: str, password: str, db: Session):
    try:
        token_data = login_user(db, email, password)
        return token_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
