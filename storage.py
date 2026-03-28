import json
from student import Student

def save_students(file_path:str,student:list):
      data = [student.to_dict() for student in students]

      with open (file_path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)


def load_students(file_path:str):
    try:
        with open (file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
            return [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    file_path = "data/students.json"

    stu1 = Student("001","张三",18,"计算机科学与技术",95)
    stu2 = Student("002","李四",19,"软件工程",88)

    students = [stu1,stu2]

    save_students(file_path,students)
    print("保存成功。")

    loaded_students = load_students(file_path)
    print("读取成功，读取结果如下：")

    for student in loaded_students:
        print(student.to_dict())




    