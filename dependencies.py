from fastapi import HTTPException, status,Depends
from service import get_student_by_id_service
from typing import Annotated


##校检路径中的路径参数 student_id 是否合法：
def validate_student_id(student_id:str):
    student_id = student_id.strip()
    if student_id == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="学号不能为空。"
        )
    if not student_id.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="学号必须是纯数字。")
    return student_id
StudentIdDepends = Annotated[str,Depends(validate_student_id)]

##检查目标学生是否存在，存在就返回学生信息字典，不存在就直接报404
def get_student_or_404(student_id:StudentIdDepends):
    student = get_student_by_id_service(student_id)
    if student is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="未找到该学号对应的学生。",
        )
    return student

StudentDepends = Annotated[dict,Depends(get_student_or_404)]
