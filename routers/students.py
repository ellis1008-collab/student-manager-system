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


@router.get("/", response_model=list[StudentResponse])
def get_students():
    return get_all_students_service()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    responses={404: COMMON_ERROR_RESPONSES[404],
               400:COMMON_ERROR_RESPONSES[400],},
)
def get_student(student :StudentDepends):
    return student


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: COMMON_ERROR_RESPONSES[400],
        422: COMMON_ERROR_RESPONSES[422],},
)
def create_student(student_data: StudentCreateRequest):
    success, message = add_student_service(student_data.model_dump())

    if not success:
        raise HTTPException(status_code=400, detail=message)
    return get_student_or_404(student_data.id )

@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    responses={
        404: COMMON_ERROR_RESPONSES[404],
        422: COMMON_ERROR_RESPONSES[422],
        400: COMMON_ERROR_RESPONSES[400],
    },
    dependencies=[Depends(get_student_or_404)],
)
def update_student(student_id: StudentIdDepends, 
                   student_data: StudentUpdateRequest):
    
    _, _, updated_student = update_student_service(
        student_id, student_data.model_dump())

    return updated_student


@router.delete(
    "/{student_id}",
    response_model=StudentResponse,
    responses={404: COMMON_ERROR_RESPONSES[404],
               400: COMMON_ERROR_RESPONSES[400],},
    dependencies=[Depends(get_student_or_404)],
)
def delete_student(student_id: StudentIdDepends):
    _, _, deleted_student = delete_student_service(student_id)

    return deleted_student