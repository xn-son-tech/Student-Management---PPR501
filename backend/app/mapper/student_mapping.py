from app.models.student import StudentModel
from app.models.student_model import StudentModel as Student

def to_entity(domain: Student) -> StudentModel:
    return StudentModel(
        student_id=domain.student_id,
        first_name=domain.first_name,
        last_name=domain.last_name,
        email=domain.email,
        dob=domain.dob,
        hometown=domain.hometown,
        math_score=domain.math_score,
        literature_score=domain.literature_score,
        english_score=domain.english_score,
    )
