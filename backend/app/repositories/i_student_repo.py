from typing import Protocol

from app.models.base_model import BaseResponse
from app.models.student_model import StudentModel

class StudentProtocol(Protocol):
    @staticmethod
    def load_students() -> object: BaseResponse[StudentModel]
    
    @staticmethod
    def insert_into_db(students: list[StudentModel]) -> None: ...
    
    @staticmethod
    def get_all_students() -> object: BaseResponse[StudentModel]
    
    @staticmethod
    def get_student_by_id(student_id: str) -> object: BaseResponse[StudentModel]
    
    @staticmethod
    def create_student(student: StudentModel) -> object: BaseResponse[StudentModel]
    
    @staticmethod
    def update_student(student_id: str, student: StudentModel) -> object: BaseResponse[StudentModel]
    
    @staticmethod
    def delete_student(student_id: str) -> object: BaseResponse[StudentModel]