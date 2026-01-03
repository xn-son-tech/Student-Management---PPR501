from typing import List
from app.repositories.student_repo import StudentRepository

class StudentService: 
    
    @staticmethod 
    def load_students():
        return StudentRepository.load_students()
        