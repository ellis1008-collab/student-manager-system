class Student:
    def __init__(self,stu_id:str,stu_name:str,stu_age:int,stu_major:str,stu_score:int):
        if not isinstance(stu_id,str) or stu_id.strip() == "":
            raise ValueError("学号不能为空，且必须是字符串。")
        if not stu_id.strip().isdigit():
            raise ValueError("学号必须是纯数字。")

        if not isinstance(stu_name,str) or stu_name.strip() == "":
            raise ValueError("姓名不能为空，且必须是字符串。")
        if stu_name.strip().isdigit():
            raise ValueError("姓名不能是纯数字。")

        if not isinstance(stu_major,str) or stu_major.strip() == "":
            raise ValueError("专业不能为空，且必须是字符串。")
        if stu_major.strip().isdigit():
            raise ValueError("专业不能是纯数字。")

        if not isinstance(stu_age,int):
            raise TypeError("年龄必须是整数。")

        if stu_age < 0:
            raise ValueError("年龄不能小于0。")
        
        if stu_age > 150:
            raise ValueError("年龄不能大于 150 。")


        if not isinstance(stu_score,int):
            raise TypeError("成绩必须是整数。")

        if stu_score <0 or stu_score>100:
            raise TypeError("成绩必须在0到100之间")

        self.id=stu_id.strip()
        self.name=stu_name.strip()
        self.age=stu_age
        self.major=stu_major.strip()
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




    print("\n下面开始测试 Day 9 新规则：")

    test_cases = [
        ("abc","张三",18,"计算机科学与技术",95),
        ("001","123",18,"计算机科学与技术",95),
        ("001","张三",18,"123",95),
        ("001","张三",200,"计算机科学与技术",95),
    ]

    for i,case in enumerate(test_cases,start=1):
        try:
            Student(*case)
            print(f"测试{i}:错误,本来不应该创建成功。")
        except Exception as e:
            print(f"测试{i}:捕获异常 -> {e}")