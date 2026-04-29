from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from ai_client import generate_ai_reply

router = APIRouter(
    prefix="/ai",
    tags=["ai"],
)

class AIReplyRequest(BaseModel):
    prompt:str = Field(
        min_length=1,
        max_length=500,
        description="用户输入给大模型的问题或指令",
        examples=["请用一句话介绍 FastAPI。"],
    )

class AIReplyResponse(BaseModel):
    reply: str = Field(
        description="大模型返回的回复内容"
    )

@router.post(
    "/reply",
    response_model=AIReplyResponse,
    status_code=status.HTTP_200_OK,
    summary="调用百炼模型生成回复",
    description="接收用户输入的 prompt, 调用 ai_client.py 中封装的百炼模型客户端，并返回模型回复。",
    )
def create_ai_reply(request:AIReplyRequest):
    try:
        reply=generate_ai_reply(request.prompt)
        return AIReplyResponse(reply=reply)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail=str(e),
        ) from e
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,detail=str(e),
        ) from e