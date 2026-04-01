from student import Student
from manager import StudentManager
from storage import load_students,save_students


class StudentService:
    def __init__(self,file_path="data/students.json"):
    ##为这个类创建两个属性：
        self.file_path = file_path
        self.manager = StudentManager()

        ##读取JSON文本的学生数据，并存储在学生服务层(manager属性的列表)里面：
        loaded_students = load_students(self.file_path)
        for student in loaded_students:
            self.manager.add_student(student)

    ##manager中的copy()
    def list_students(self):
        return self.manager.list_students()
    
    ##查询学生有些BUG(可输入空，输出没找到)
    def find_student_by_id(self,student_id):
        return self.manager.find_student_by_id(student_id)

    ##添加学生：
    def add_student(self,stu_id,stu_name,stu_age,stu_major,stu_score):
        student = Student(stu_id,stu_name,stu_age,stu_major,stu_score)
        self.manager.add_student(student)
        return student
    
    ##修改学生：
    def update_student_by_id(self,student_id,new_name,new_age,new_major,new_score):
        self.manager.update_student_by_id(student_id,new_name,new_age,new_major,new_score)
        return self.manager.find_student_by_id(student_id)
   
    ##删除学生：
    def delete_student_by_id(self,student_id):
        student = self.manager.find_student_by_id(student_id)

        if student is None:
            raise ValueError("未找到该学号对应的学生。")
        
        self.manager.delete_student_by_id(student_id)
        return student
    
    ##储存(覆盖写入）：
    def save(self):
        save_students(self.file_path,self.manager.list_students())




