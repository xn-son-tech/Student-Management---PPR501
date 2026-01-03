import csv
from pathlib import Path
from typing import List
from app.models.student_model import StudentModel
from app.models.base_model import BaseResponse
from app.repositories.i_student_repo import StudentProtocol
from app.core.database import SessionLocal
from app.mapper.student_mapping import to_entity

DATA_FILE = Path('app/seeds/students.csv')

class StudentRepository(StudentProtocol):
    
    @staticmethod
    def load_students() -> BaseResponse[StudentModel]:
        students: List[StudentModel] = []
        try:
            with DATA_FILE.open(mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:  
                    student = StudentModel(
                        student_id=row['student_id'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        dob=row['date_of_birth'],
                        hometown=row['hometown'],
                        math_score=float(row['math_score']),
                        literature_score=float(row['literature_score'])
                    )
                    students.append(student)
            return BaseResponse(success=True, data=students)
        except Exception as e:
            return BaseResponse(success=False, error=str(e))
    
    @staticmethod
    def insert_into_db(students: BaseResponse[StudentModel]):
        if not students.success:
            raise Exception("Failed to load students from CSV.")
        
        data_students = students.data
        try: 
            with SessionLocal() as session:
                for student in data_students:
                    session.add(to_entity(student))
                session.commit()
        except Exception as e:
            raise e
        