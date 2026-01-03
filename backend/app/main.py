from app.repositories.student_repo import StudentRepository
print('hello')
student_repo = StudentRepository()

students = student_repo.load_students()
print(students.data)
student_repo.insert_into_db(students=students)