from app.repositories import student_repository

def create_student(student):
    return student_repository.create_student(student)

def get_student(student_id):
    return student_repository.get_student(student_id)