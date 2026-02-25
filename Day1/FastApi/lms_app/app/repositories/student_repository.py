students = []
student_id_counter = 1

def create_student(student):
    global student_id_counter
    student_dict = student.dict()
    student_dict["id"] = student_id_counter
    students.append(student_dict)
    student_id_counter += 1
    return student_dict

def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None