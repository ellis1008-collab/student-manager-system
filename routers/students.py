from fastapi import APIRouter, HTTPException, status

from service import (
    add_student_service,
    delete_student_service,
    get_all_students_service,
    get_student_by_id_service,
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
    tags=["students"]    
)


@router.get("/", response_model=list[StudentResponse])
def get_students():
    return get_all_students_service()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    responses={404: COMMON_ERROR_RESPONSES[404]},
)
def get_student(student_id: str):
    student = get_student_by_id_service(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="未找到该学号对应的学生。")

    return student


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: COMMON_ERROR_RESPONSES[400],
        422: COMMON_ERROR_RESPONSES[422],
    },
)
def create_student(student_data: StudentCreateRequest):
    success, message = add_student_service(student_data.model_dump())

    if not success:
        raise HTTPException(status_code=400, detail=message)

    created_student = get_student_by_id_service(student_data.id)
    return created_student


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    responses={
        404: COMMON_ERROR_RESPONSES[404],
        422: COMMON_ERROR_RESPONSES[422],
    },
)
def update_student(student_id: str, student_data: StudentUpdateRequest):
    success, message, updated_student = update_student_service(
        student_id, student_data.model_dump()
    )

    if not success:
        raise HTTPException(status_code=404, detail=message)

    return updated_student


@router.delete(
    "/{student_id}",
    response_model=StudentResponse,
    responses={404: COMMON_ERROR_RESPONSES[404]},
)
def delete_student(student_id: str):
    success, message, deleted_student = delete_student_service(student_id)

    if not success:
        raise HTTPException(status_code=404, detail=message)

    return deleted_student