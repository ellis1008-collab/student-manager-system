from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator

from service import StudentService


app = FastAPI(title="Student Manager API")
service = StudentService()

##添加学生请求体模型：
class StudentCreateRequest(BaseModel):
    id: str = Field(
        description="学生学号，字符串形式，若有前导 0 请保留",
        min_length=1,
        max_length=20,
    )
    name: str = Field(
        description="学生姓名",
        min_length=1,
        max_length=20,
    )
    age: int = Field(
        description="年龄，范围是 0 到 150",
        ge=0,
        le=150,
    )
    major: str = Field(
        description="专业名称",
        min_length=1,
        max_length=50,
    )
    score: int = Field(
        description="成绩，范围是 0 到 100",
        ge=0,
        le=100,
    )

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        value = value.strip()
        if value == "":
            raise ValueError("学号不能为空。")
        if not value.isdigit():
            raise ValueError("学号必须是纯数字。")
        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()
        if value == "":
            raise ValueError("姓名不能为空。")
        if value.isdigit():
            raise ValueError("姓名不能是纯数字。")
        return value

    @field_validator("major")
    @classmethod
    def validate_major(cls, value: str) -> str:
        value = value.strip()
        if value == "":
            raise ValueError("专业不能为空。")
        if value.isdigit():
            raise ValueError("专业不能是纯数字。")
        return value


##修改学生请求体模型
class StudentUpdateRequest(BaseModel):
    name:str=Field(
        description="学生姓名",
        min_len=1,
        max_len=20,
    )
    age:int=Field(
        description="学生年龄",
        ge=0,
        le=150,
    )
    major:str=Field(
        description="学生专业",
        min_len=1,
        max_len=20,
    )
    score:int=Field(
        description="学生成绩",
        ge=0,
        le=100,
    )

    @field_validator("name")
    @classmethod
    def validate_name(cla,value:str)->str:
        value = value.strip()
        if value.strip()=="":
            raise ValueError("姓名不能为空。")
        if value.isdigit():
            raise ValueError("姓名不能为纯数字。")
        return value

    @field_validator("major")
    @classmethod
    def validate_major(cls,value:str)->str:
        value = value.strip()
        if value=="":
            raise ValueError("专业不能为空。")
        if value.isdigit():
            raise ValueError("专业不能为纯数字。")
        return value

##响应体模型
class StudentResponse(BaseModel):
    id:str=Field(description="学生学号")
    name:str=Field(description="学生姓名")
    age:int=Field(description="学生年龄")
    major:str=Field(description="学生专业")
    score:int=Field(description="学生成绩")




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
@app.get("/students",response_model=list[StudentResponse])
async def get_students():
    students = service.list_students()
    return [student_to_dict(student) for student in students]


##按学号查询接口：
@app.get("/students/{student_id}",response_model=StudentResponse)
async def get_student(student_id: str):
    student = service.find_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="未找到该学号对应的学生。")
    return student_to_dict(student)

##添加（创建）学生接口：
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
    )
async def create_student(student_data:StudentCreateRequest):
    try:
        student = service.add_student(
            student_data.id,
            student_data.name,
            student_data.age,
            student_data.major,
            student_data.score,
        )
        service.save()
        return student_to_dict(student)
    except(ValueError,TypeError)as e:
        raise HTTPException(status_code=400,detail=str(e))

##修改学生接口：
@app.put("/students/{student_id}",response_model=StudentResponse)
async def update_student(student_id:str, student_data:StudentUpdateRequest):
    existing_student = service.find_student_by_id(student_id)
    if existing_student is None:
        raise HTTPException(status_code=404,detail="未找到该学号对应的学生。")
    try:
        updated_student = service.update_student_by_id(
            student_id,
            student_data.name,
            student_data.age,
            student_data.major,
            student_data.score,
            )
        service.save()
        return student_to_dict(updated_student)
    except (ValueError, TypeError) as e:
        raise HTTPException (status_code=400,detail=str(e))

##删除学生接口：
@app.delete("/students/{student_id}",response_model=StudentResponse)
async def delete_student(student_id:str):
    try:
        deleted_student = service.delete_student_by_id(student_id)
        service.save()
        return student_to_dict(deleted_student)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
