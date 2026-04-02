from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from service import StudentService


app = FastAPI(title="Student Manager API")
service = StudentService()

class StudentCreateRequest(BaseModel):
    id:str
    name:str
    age:int
    major:str
    score:int

def student_to_dict(student):
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "major": student.major,
        "score": student.score,
    }


##根路径接口：
@app.get("/")
async def root():
    return {"message": "Student Manager API is running"}

##查看所有学生接口：
@app.get("/students")
async def get_students():
    students = service.list_students()
    return [student_to_dict(student) for student in students]


##按学号查询接口：
@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = service.find_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="未找到该学号对应的学生。")
    return student_to_dict(student)

##添加（创建）学生接口：
@app.post("/students",status_code=status.HTTP_201_CREATED)
async def create_student(student_data:StudentCreateRequest):
    try:
        student = service.add_student(
            student_data.id,
            student_data.name,
            student_data.age,
            student_data.major,
            student_data.score,
        )
        return student_to_dict(student)
    except(ValueError,TypeError)as e:
        raise HTTPException(status_code=400,detail=str(e))
        
