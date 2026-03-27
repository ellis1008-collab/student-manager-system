from student import Student


class StudentManager:
    def __init__(self):
        self.students=[]


    ##添加学生的管理器
    def add_student(self,student:Student):
        if not isinstance(student,Student):
           raise TypeError("添加的对象必须是Student类型。")
        if self.find_student_by_id(student.id) is not None:
           raise ValueError("学号已存在，不能重复添加。")
        self.students.append(student)


    ##检查学号是否已经存在
    def find_student_by_id(self,student_id:str):
        if not isinstance(student_id,str):
            raise TypeError("学号必须是字符串。")
        for student in self.students:
            if student.id == student_id:
               return student
        return None

    def list_students(self):
        return  self.students.copy()
if __name__ == "__main__":
    manager = StudentManager()


    stu1 = Student("001","张三",18,"计算机科学与技术",95)
    stu2 = Student("002","李四",19,"软件工程",99)

    manager.add_student(stu1)
    manager.add_student(stu2)

    print("当前学生数量：",len(manager.students))
    print("学生如下：")
    for student in manager.students:
        print(student.to_dict())

    print("\n下面开始测试重复学号:")
    try:
        stu3 = Student("002","王五",20,"人工智能",90)
        manager.add_student(stu3)
        print("错误：重复学号本来不应该添加成功。")
    except Exception as e:
        print("捕获异常：",e)

    print("\n下面测试查找成功:")
    found_student = manager.find_student_by_id("002")
    if found_student is not None:
        print("找到的学生:",found_student.to_dict())
    else:
        print("没有找到该学号的学生。") 

    print("下面测试查找失败：")
    not_found_student = manager.find_student_by_id("999")
    if not_found_student is None:
        print("没有找到学号999对应的学生。")
    else:
        print("错误:不应该找到学号999对应的学生。")

    