from fastapi import APIRouter, HTTPException, status, Depends
from dependencies import get_student_or_404, StudentDepends, StudentIdDepends 

from service import (
    add_student_service,
    delete_student_service,
    get_all_students_service,
    update_student_service,
)
from schemas import (
    COMMON_ERROR_RESPONSES,
    StudentCreateRequest,
    StudentResponse,
    StudentUpdateRequest,
)
  
router = APIRouter(
    prefix="/students",
    tags=["students"],
)

##获取全部学生：
@router.get(
        "/",
        response_model=list[StudentResponse],
        summary="获取学生列表",
        description="获取当前系统中所有学生的信息列表，返回结果为学生对象数组。",
)
def get_students():
    return get_all_students_service()


##按学号查询学生：
@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    responses={
               404: COMMON_ERROR_RESPONSES[404],
               400: COMMON_ERROR_RESPONSES[400],
               422: COMMON_ERROR_RESPONSES[422],
    },
               summary="根据学号获取学生",
               description="根据路径参数 student_id 查询单个学生。学号必须是纯数字；如果学生不存在，返回404。",
)
def get_student(student :StudentDepends):
    return student


##创建学生：
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: COMMON_ERROR_RESPONSES[400],
        422: COMMON_ERROR_RESPONSES[422],
    },
        summary="新增学生",
        description="新增一个学生信息。请求体需要包含学号，姓名，年龄，专业和成绩；学号不能重复。",
)
def create_student(student_data: StudentCreateRequest):
    success, message = add_student_service(student_data.model_dump())

    if not success:
        raise HTTPException(status_code=400, detail=message)
    return get_student_or_404(student_data.id )


##按学号更新学生：
@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    responses={
        404: COMMON_ERROR_RESPONSES[404],
        422: COMMON_ERROR_RESPONSES[422],
        400: COMMON_ERROR_RESPONSES[400],
    },
    dependencies=[Depends(get_student_or_404)],
    summary="根据学号修改学生",
    description="根据路径参数 student_id 修改指定学生的信息。学号必须是纯数字；如果学生不存在，返回404。",
)
def update_student(student_id: StudentIdDepends, 
                   student_data: StudentUpdateRequest):
    
    _, _, updated_student = update_student_service(
        student_id, student_data.model_dump())

    return updated_student


##按学号删除学生：
@router.delete(
    "/{student_id}",
    response_model=StudentResponse,
    responses={
               404: COMMON_ERROR_RESPONSES[404],
               400: COMMON_ERROR_RESPONSES[400],
               422: COMMON_ERROR_RESPONSES[422],
    },
    dependencies=[Depends(get_student_or_404)],
    summary="根据学号删除学生",
    description="根据路径参数 student_id 删除指定学生的信息。学号必须是纯数字；如果学生不存在，返回 404。删除成功后返回被删除的学生信息。",
)
def delete_student(student_id: StudentIdDepends):
    _, _, deleted_student = delete_student_service(student_id)

    return deleted_student