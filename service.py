from db_orm import add_student_orm
from db_orm import get_all_students_orm
from db_orm import get_student_by_id_orm
from db_orm import update_student_by_id_orm
from db_orm import delete_student_by_id_orm

def student_orm_to_dict(student):
    if student is None:
        return None
    return {
        "id":student.id,
        "name":student.name,
        "age":student.age,
        "major":student.major,
        "score":student.score,
    }
##获取所有学生的字典列表：
def get_all_students_service():
        students = get_all_students_orm()
        return [student_orm_to_dict(student) for student in students]

##按学号查询学生：
def get_student_by_id_service(student_id):
    student = get_student_by_id_orm(student_id)
    return student_orm_to_dict(student)

##添加学生：
def add_student_service(student_data):
    existing_student = get_student_by_id_orm(student_data["id"])
    if existing_student is not None:
        return False, "学号已存在,不能重复添加。"
    created_student = add_student_orm(student_data)
    if created_student is not None:
        return True, "新增成功。"
    return False, "新增失败。"

##修改学生：
def update_student_service(student_id,student_data):
    existing_student = get_student_by_id_orm(student_id)
    if existing_student is None:
        return False, "未找到该学号对应的学生。",None
    updated_student = update_student_by_id_orm(student_id,student_data)
    return True, "修改成功。",student_orm_to_dict(updated_student)
    
##删除学生：
def delete_student_service(student_id):
    existing_student = get_student_by_id_orm(student_id)
    if existing_student is None:
        return False, "未找到该学号对应的学生。",None
    deleted_student = delete_student_by_id_orm(student_id)
    return True, "删除成功。",student_orm_to_dict(deleted_student)
   


if __name__ == "__main__":
    print("全部学生：", get_all_students_service())

    print("查询 003: ",get_student_by_id_service("003"))
