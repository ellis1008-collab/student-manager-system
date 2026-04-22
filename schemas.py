from pydantic import BaseModel, Field, field_validator

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

COMMON_ERROR_RESPONSES = {
    400:{"model": ErrorResponse,"description":"请求数据不合法。"},
    404:{"model":ErrorResponse,"description":"目标资源不存在。"},
    422:{"model":ErrorResponse,"description":"请求参数校检失败。"}
}