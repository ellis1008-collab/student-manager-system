from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from ai_client import generate_ai_reply
from prompts import build_student_manager_prompt, build_student_advice_prompt
from dependencies import StudentDepends

router = APIRouter(
    prefix="/ai",
    tags=["ai"],
)

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

##AI Python 后端开发助手接口：
@router.post(
    "/reply",
    response_model=AIReplyResponse,
    status_code=status.HTTP_200_OK,
    summary="调用百炼模型生成回复",
    description="接收用户输入的 prompt, 调用 ai_client.py 中封装的百炼模型客户端，并返回模型回复。",
    )
def create_ai_reply(request:AIReplyRequest):
    final_prompt = build_student_manager_prompt(request.prompt)
    try:
        reply=generate_ai_reply(final_prompt)
        return AIReplyResponse(reply=reply)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail=str(e),
        ) from e
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,detail=str(e),
        ) from e
    

##AI 学生建议接口：
@router.post(
    "/students/{student_id}/advice",
    response_model=StudentAdviceResponse,
    status_code = status.HTTP_200_OK,
    summary="根据学生信息生成学习建议",
    description="根据路径参数 student_id 查询数据库中已有学生信息，并调用大模型生成学生建议。",
)
def create_student_advice(student: StudentDepends):
    
    final_prompt = build_student_advice_prompt(
        name=student["name"],
        major=student["major"],
        score=student["score"],
    )

    try:
        advice = generate_ai_reply(final_prompt)
        return StudentAdviceResponse(advice=advice)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY,detail=str(e)) from e