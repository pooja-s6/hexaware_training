#main.py

from fastapi import FastAPI
from app.routers import auth_router, employer_router, candidate_router, admin_router
from app.database.session import engine
from app.database.base import Base

#Create database tables
Base.metadata.create_all(bind=engine)

#Create FastAPI app
app = FastAPI(title="Job Portal API", version="2.0")

#Include routers
app.include_router(auth_router.router)
app.include_router(employer_router.router)
app.include_router(candidate_router.router)
app.include_router(admin_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to Job Portal API V2"}
