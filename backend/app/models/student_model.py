# backend/app/models/student.py
from typing import Optional, Dict


class StudentModel:
    def __init__(
        self,
        student_id: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        dob: Optional[str] = None,
        hometown: Optional[str] = None,
        math_score: Optional[float] = None,
        literature_score: Optional[float] = None,
        english_score: Optional[float] = None,
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
        self.hometown = hometown
        self.math_score = math_score
        self.literature_score = literature_score
        self.english_score = english_score

    @staticmethod
    def from_dict(data: Dict):
        return StudentModel(
            student_id=data.get("student_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            dob=data.get("dob"),
            hometown=data.get("hometown"),
            math_score=_to_float(data.get("math_score")),
            literature_score=_to_float(data.get("literature_score")),
            english_score=_to_float(data.get("english_score")),
        )

    def to_dict(self) -> Dict:
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "dob": self.dob,
            "hometown": self.hometown,
            "math_score": self.math_score,
            "literature_score": self.literature_score,
            "english_score": self.english_score,
        }


def _to_float(value):
    if value in (None, "", "null"):
        return None
    try:
        return float(value)
    except ValueError:
        return None
