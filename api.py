from fastapi import FastAPI, HTTPException, status,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

from service import get_all_students_service
from service import get_student_by_id_service
from service import add_student_service
from service import update_student_service
from service import delete_student_service





app = FastAPI(title="Student Manager API")

##学生响应体模型：写在路由里面
class StudentResponse(BaseModel):
    id:str=Field(description="学生学号")
    name:str=Field(description="学生姓名")
    age:int=Field(description="学生年龄")
    major:str=Field(description="学生专业")
    score:int=Field(description="学生成绩")


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


##错误的一部分：
class ErrorItem(BaseModel):
    field: str | None = Field(default=None,description="出错字段位置")
    message: str = Field(description="错误说明")

##整份错误：
class ErrorResponse(BaseModel):
    code: int = Field(description="HTTP 状态码")
    message: str = Field(description="错误总说明")
    errors: list[ErrorItem] = Field(default_factory=list,description="详细错误列表")



##格式化错误位置信息：
def format_error_location(loc) -> str|None:
    if not loc:
        return None
    source = str(loc[0])
    rest = [str(item) for item in loc[1:]]

    source_map = {
        "body": "请求体",
        "path": "路径参数",
        "query": "查询参数",
    }
    source_text = source_map.get(source,source)

    if rest:
        return f"{source_text}." + ".".join(rest)
    return source_text


##第二个新增辅助函数：
def translate_validation_error(error: dict) -> str:
    error_type = error.get("type","")
    ctx = error.get("ctx",{})
    msg = error.get("msg","请求参数不合法。")

    if msg.startswith("Value error ,"):
        msg = msg[len("Value error,"):]
    if error_type == "less_than_equal":
        return f"输入值必须小于等于{ctx.get('le')}。"
    if error_type == "greater_than_equal":
        return f"输入值必须大于等于 {ctx.get('ge')}。"
    if error_type == "string_too_short":
        return f"字符串长度不能少于 {ctx.get('min_length')} 个字符。"
    if error_type == "string_too_long":
        return f"字符串长度不能超过 {ctx.get('max_length')} 个字符。"
    if error_type == "missing":
        return "该字段是必填项。"
    if error_type == "int_parsing":
        return "该字段必须是整数。"
    if error_type == "string_type":
        return "该字段必须是字符串。"

    return msg



COMMON_ERROR_RESPONSES = {
    400:{"model": ErrorResponse,"description":"请求数据不合法。"},
    404:{"model":ErrorResponse,"description":"目标资源不存在。"},
    422:{"model":ErrorResponse,"description":"请求参数校检失败。"}
}


##根路径接口：
@app.get("/")
async def root():
    return {"message": "Student Manager API is running"}

##查看所有学生接口(已修改）：
@app.get("/students",response_model=list[StudentResponse])
async def get_students():
    students = get_all_students_service()
    return students


##按学号查询接口（已修改）：
@app.get(
        "/students/{student_id}",
        response_model=StudentResponse,
        responses = {404:COMMON_ERROR_RESPONSES[404]},
        )
async def get_student(student_id: str):
    student = get_student_by_id_service(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="未找到该学号对应的学生。")
    return student

##添加（创建）学生接口（已修改）：
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400:COMMON_ERROR_RESPONSES[400],
        422:COMMON_ERROR_RESPONSES[422],
    },
    )

async def create_student(student_data:StudentCreateRequest):
    success,message = add_student_service(student_data.model_dump())
    if not success:
        raise HTTPException(status_code=400,detail=message)
    created_student = get_student_by_id_service(student_data.id)
    return created_student


##修改学生接口(已修改）：
@app.put("/students/{student_id}",
         response_model=StudentResponse,
         responses = {
             404:COMMON_ERROR_RESPONSES[404],
             422:COMMON_ERROR_RESPONSES[422],
         },
         )
async def update_student(student_id:str, student_data:StudentUpdateRequest):
    
    success,message,updated_student = update_student_service(student_id,student_data.model_dump())
    if not success:
        raise HTTPException(status_code=404,detail=message)
    return updated_student



##删除学生接口(已修改）：
@app.delete("/students/{student_id}",
            response_model=StudentResponse,
            responses = {
                404:COMMON_ERROR_RESPONSES[404]},
            )
async def delete_student(student_id:str):
    success,message,deleted_student = delete_student_service(student_id)
    if not success:
        raise HTTPException(status_code=404,detail=message)
    return deleted_student




##exception_handler:app提供的一个方法，作用是注册异常处理器，
##告诉FastAPI,出现下面函数中的异常时，就按照我的方法解决
##请求校检异常处理器：
@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request,
    exc:RequestValidationError,
):
    errors = []

    for error in exc.errors():
        errors.append(
           ErrorItem(
                field=format_error_location(error.get("loc",())),
                message=translate_validation_error(error),
            )
        )
    payload = ErrorResponse(
        code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message="请求参数校检失败。",   ##（路由前）
        errors=errors,
    )
    return JSONResponse(
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=payload.model_dump(),
    )


##HTTPException统一处理器：
@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request, 
    exc: HTTPException,        ##外部异常状态码
):  
    ##内部异常状态码的异常说明（只有内部有异常说明）（路由后，主动抛出的HTTP异常）
    if exc.status_code == status.HTTP_404_NOT_FOUND:
        top_message = "目标资源不存在。"
    elif exc.status_code == status.HTTP_400_BAD_REQUEST:
        top_message = "请求数据不合法。"
    else:
        top_message = "请求处理失败。"

    payload = ErrorResponse(
        code=exc.status_code,
        message=top_message,
        errors=[
            ErrorItem(
                field=None,
                message=str(exc.detail),
            )
        ],
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=payload.model_dump(),
    )