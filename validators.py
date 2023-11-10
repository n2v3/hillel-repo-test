from db import Student, Teacher


class ValidationError(Exception):
    pass


def validate_student_data(data):
    name = data.get("name")
    age = data.get("age")

    if not (name and age):
        raise ValidationError("name and age are required")

    if not isinstance(age, int):
        raise ValidationError("age must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")

    if age < 0:
        raise ValidationError("age must be positive")
    if name == "":
        raise ValidationError("name must not be empty")


def validate_teacher_data(data):
    name = data.get("name")
    subject = data.get("subject")
    rate = data.get("rate")
    work_experience_years = data.get("work_experience_years")

    if not (name and subject and work_experience_years):
        raise ValidationError("name, subject and work_experience_years are required")
    if not isinstance(subject, str):
        raise ValidationError("subject must be string")
    if not isinstance(rate, int):
        raise ValidationError("rate must be int")
    if not isinstance(work_experience_years, int):
        raise ValidationError("work_experience_years must be int")

    if rate < 0:
        raise ValidationError("rate must be positive")
    if work_experience_years < 0:
        raise ValidationError("work_experience_years must be positive")
    if subject == "":
        raise ValidationError("subject must not be empty")


def validate_mark_data(data):
    student_id = data.get("student_id")
    value = data.get("value")
    teacher_id = data.get("teacher_id")

    student = Student.get_or_none(id=student_id)
    teacher = Teacher.get_or_none(id=teacher_id)

    if not teacher:
        raise ValidationError("teacher with such id does not exist")

    if not student:
        raise ValidationError("student with such id does not exist")

    if not (student_id and value and teacher_id):
        raise ValidationError("student_id, value and teacher_id are required")

    if not isinstance(student_id, int):
        raise ValidationError("student_id must be integer")
    if not isinstance(teacher_id, int):
        raise ValidationError("teacher_id must be integer")
    if not isinstance(value, int):
        raise ValidationError("value must be integer")

    if value < 0:
        raise ValidationError("value must be positive")

    data["student"] = student
    return data
