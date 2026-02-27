#auth_service.py

from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories.user_repo import create_user, get_user_by_email, get_user_by_id
from app.schemas.user_schema import UserCreate

#Register new user
def register_user(db: Session, user_data: UserCreate):
    #Check if user already exists
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Email already registered")
    
    #Hash password
    hashed_password = hash_password(user_data.password)
    
    #Create user data
    user_dict = user_data.model_dump()
    user_dict["password"] = hashed_password
    
    #Create user in database
    new_user = create_user(db, user_dict)
    return new_user

#Login user
def login_user(db: Session, email: str, password: str):
    #Get user by email
    user = get_user_by_email(db, email)
    if not user:
        raise ValueError("Invalid credentials")
    
    #Verify password
    if not verify_password(password, user.password):
        raise ValueError("Invalid credentials")
    
    #Create access token
    token_data = {"user_id": user.id, "email": user.email, "role": user.role}
    access_token = create_access_token(token_data)
    
    return {"access_token": access_token, "token_type": "bearer"}

#Get current user from token
def get_current_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError("User not found")
    return user
