class Student:
    def __init__(self,stu_id:str,stu_name:str,stu_age:int,stu_major:str,stu_score:int):
        if not isinstance(stu_id,str) or stu_id.strip() == "":
            raise ValueError("学号不能为空，且必须是字符串。")
        if not isinstance(stu_name,str) or stu_name.strip() == "":
            raise ValueError("姓名不能为空，且必须是字符串。")
        if not isinstance(stu_major,str) or stu_major.strip() == "":
            raise ValueError("专业不能为空，且必须是字符串。")
        if not isinstance(stu_age,int):
            raise TypError("年龄必须是整数。")
        if stu_age < 0:
            raise ValueError("年龄不能小于0。")
        if not isinstance(stu_score,int):
            raise TypeError("成绩必须是整数。")
        if stu_score <0 or stu_score>100:
            raise TypeError("成绩必须在0到100之间")
        self.id=stu_id
        self.name=stu_name
        self.age=stu_age
        self.major=stu_major
        self.score=stu_score

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "major":self.major,
            "score":self.score

        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["id"],
            data["name"],
            data["age"],
            data["major"],
            data["score"]
        )
if __name__=="__main__":
    stu1=Student("001","张三",18,"计算机科学与技术",95)



    print("学号:",stu1.id)
    print("姓名:",stu1.name)
    print("年龄:",stu1.age)
    print("专业：",stu1.major)
    print("成绩：",stu1.score)


    student_dict=stu1.to_dict()
    print("转成字典后：",student_dict)


    stu2=Student.from_dict(student_dict)
    print("从字典恢复猴的姓名：",stu2.name)


    print("\n下面开始测试非法数据:")

    try:
        bad_student = Student("002","李四",-1,"软件工程",120)
        print("错误：这行本来不应该创建成功",bad_student.name)
    except Exception as e:
            print("捕获异常：",e)