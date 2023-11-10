from flask import request


def deserialize_student_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return {
        "name": name,
        "age": age
    }


def deserialize_teacher_data():
    data = request.get_json()

    name = data.get("name")
    subject = data.get("subject")
    rate = data.get("rate")
    work_experience = data.get("work_experience")

    return {
        "name": name,
        "subject": subject,
        "rate": rate,
        "work_experience": work_experience
    }


def deserialize_mark_data():
    data = request.get_json()

    student_id = data.get("student_id")
    value = data.get("value")
    teacher_id = data.get("teacher_id")

    return {
        "student_id": student_id,
        "value": value,
        "teacher_id": teacher_id
   }