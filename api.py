from fastapi import FastAPI, HTTPException

from service import StudentService


app = FastAPI(title="Student Manager API")
service = StudentService()


def student_to_dict(student):
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "major": student.major,
        "score": student.score,
    }


@app.get("/")
async def root():
    return {"message": "Student Manager API is running"}


@app.get("/students")
async def get_students():
    students = service.list_students()
    return [student_to_dict(student) for student in students]


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = service.find_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="未找到该学号对应的学生。")
    return student_to_dict(student)