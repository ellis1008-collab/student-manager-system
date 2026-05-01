from pydantic import BaseModel, Field, field_validator, ConfigDict


##学生响应体模型：写在路由里面
class StudentResponse(BaseModel):

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "001",
                    "name": "张三",
                    "age": 18,
                    "major": "计算机科学与技术",
                    "score": 95,
                }
            ]
        }
    )

    id:str=Field(description="学生学号")
    name:str=Field(description="学生姓名")
    age:int=Field(description="学生年龄")
    major:str=Field(description="学生专业")
    score:int=Field(description="学生成绩")




##模型请求体模型：
class AIReplyRequest(BaseModel):
    prompt:str = Field(
        min_length=1,
        max_length=500,
        description="用户输入给大模型的问题或指令",
        examples=["请用一句话介绍 FastAPI。"],
    )

##模型响应体模型：
class AIReplyResponse(BaseModel):
    reply: str = Field(
        description="大模型返回的回复内容"
    )

##学生建议响应模型：
class StudentAdviceResponse(BaseModel):
    advice: str = Field(description="根据学生信息生成的学习建议")




##添加学生请求体模型：
class StudentCreateRequest(BaseModel):

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "003",
                    "name": "王五",
                    "age": 20,
                    "major": "数据科学与技术",
                    "score": 92,
                }
            ]
        }
    )

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

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "name": "张三同学",
                    "age": 20,
                    "major": "人工智能",
                    "score": 96,
                }
            ]
        }
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

COMMON_ERROR_RESPONSES = {
    400: {
        "model": ErrorResponse,
        "description": "请求数据不合法。",
        "content": {
            "application/json": {
                "example": {
                    "code": 400,
                    "message": "请求数据不合法。",
                    "errors": [
                        {
                            "field": None,
                            "message": "学号必须是纯数字。",
                        }
                    ],
                }
            }
        },
    },
    404: {
        "model": ErrorResponse,
        "description": "目标资源不存在。",
        "content": {
            "application/json": {
                "example": {
                    "code": 404,
                    "message": "目标资源不存在。",
                    "errors": [
                        {
                            "field": None,
                            "message": "未找到该学号对应的学生。",
                        }
                    ],
                }
            }
        },
    },
    422: {
        "model": ErrorResponse,
        "description": "请求参数校检失败。",
        "content": {
            "application/json": {
                "example": {
                    "code": 422,
                    "message": "请求参数校检失败。",
                    "errors": [
                        {
                            "field": "请求体.score",
                            "message": "该字段是必填项。",
                        }
                    ],
                }
            }
        },
    },
}