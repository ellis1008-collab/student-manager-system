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


    ##查询学生的管理器
    def find_student_by_id(self,student_id:str):
        if not isinstance(student_id,str):
            raise TypeError("学号必须是字符串。")
        for student in self.students:
            if student.id == student_id:
               return student
        return None

    ##删除根据学号删除对应的学生
    def delete_student_by_id(self,student_id:str):
        if not isinstance(student_id,str):
            raise TypeError("学号必须是字符串。")
        ##遍历管理器学生列表，获取索引和对象
        for index,student in enumerate(self.students):
            if student.id == student_id:
                self.students.pop(index)
                return  ##进入if语句，删除对应学生后结束方法
            ##遍历完列表没找到对应学生，报错，由外层处理
        raise ValueError("未找到该学号对应的学生。")


    def update_student_by_id(self,student_id,new_name,new_age,new_major,new_score):
        student = self.find_student_by_id(student_id)
        
        if student is None:
            raise ValueError("未找到对应学号的学生。")
        
        ##"复用逻辑"，"层次协作"：
        ##利用Student学生类的校检逻辑来检查输入的数据是否合法，可在外层解决（try/except)：
        
        checked_student = Student(student_id,new_name,new_age,new_major,new_score)
        
        student.name = checked_student.name
        student.age = checked_student.age
        student.major = checked_student.major
        student.score = checked_student.score

    ##列出管理器中的学生信息    
    def list_students(self):
        return  self.students.copy()

##模拟外层环境进行的测试：
if __name__=="__main__":
    manager=StudentManager()

    stu1 = Student("001","张三",18,"计算机科学与技术",95)
    stu2 = Student("002","李四",19,"软件工程",88)
    stu3 = Student("003","王五",20,"人工智能",90)

    manager.add_student(stu1)
    manager.add_student(stu2)
    manager.add_student(stu3)

    print("初始学生列表：")
    for student in manager.list_students():
        print(student.to_dict())
    
    print("\n下面开始测试删除学生:")
    try:
        manager.delete_student_by_id("002")
        print("删除学号002成功")
    except Exception as e:
        print("删除失败：",e)
    
    print("删除后的学生列表：")
    for student in manager.list_students():
        print(student.to_dict())
    
    print("\n下面开始测试修改学生:")
    try:
        manager.update_student_by_id("003","王五",21,"数据与科学",93)
        print("修改学号003成功。")
    except Exception as e:
        print("修改失败：",e)

    print("修改后的学生列表：")
    for student in manager.list_students():
        print(student.to_dict())

    print("\n下面开始测试删除不存在的学生:")
    try:
        manager.delete_student_by_id("999")
    except Exception as e:
        print("捕获异常：",e)

    print("\n下面开始测试修改不存在的学生:")
    try:
        manager.update_student_by_id("999","不存在",18,"无",60)
    except Exception as e:
        print("捕获异常：",e)

    




