from fastapi import FastAPI
from app.controllers import student_controller, course_controller, enrollment_controller

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to lms API",
        "version": "1.0",
        "endpoints": {
            "students": "/students",
            "courses": "/courses",
            "enrollments": "/enrollments",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }

app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)