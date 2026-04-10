from db_storage import add_student_to_db
from db_storage import get_all_students_from_db
from db_storage import get_student_by_id_from_db

##获取全部学生（字典列表）：
def get_all_students_service():
    students = get_all_students_from_db()
    return students

##按学号查询学生：
def get_student_by_id_service(student_id):
    student = get_student_by_id_from_db(student_id)
    return student

##添加学生：
def add_student_service(student_data):
    existing_student = get_student_by_id_from_db(student_data["id"])

    if existing_student is not None:
        return False,"学号已存在,不能重复添加。"
    success = add_student_to_db(student_data)
    if success:
        return True,"新增成功。"
    return False,"新增失败。"

if __name__ == "__main__":
    
    print("全部学生：",
    get_all_students_service())

    print("查询 001 :",
    get_student_by_id_service("001"))

    text_student = {
        "id": "004",     
        "name": "赵六",
        "age": 21,
        "major": "人工智能",
        "score": 91,
        }
    
    result = add_student_service(text_student)
    print("新增测试结果：",result)
