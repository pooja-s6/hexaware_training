from app.repositories import course_repository

def create_course(course):
    return course_repository.create_course(course)

def get_course(course_id):
    return course_repository.get_course(course_id)

def get_all_courses():
    return course_repository.get_all_courses()