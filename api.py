from fastapi import FastAPI, HTTPException, status,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from routers.students import router as students_router
from schemas import ErrorResponse, ErrorItem

app = FastAPI(title="Student Manager API")
app.include_router(students_router)

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


##根路径接口：
@app.get("/")
async def root():
    return {"message": "Student Manager API is running"}



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
    exc: HTTPException,        
):  
    
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