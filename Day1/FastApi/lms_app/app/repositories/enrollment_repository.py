enrollments = []
enrollment_id_counter = 1

def create_enrollment(enrollment):
    global enrollment_id_counter
    enroll_dict = enrollment.dict()
    enroll_dict["id"] = enrollment_id_counter
    enrollments.append(enroll_dict)
    enrollment_id_counter += 1
    return enroll_dict

def get_existing(student_id, course_id):
    for e in enrollments:
        if e["student_id"] == student_id and e["course_id"] == course_id:
            return e
    return None

def get_all_enrollments():
    return enrollments