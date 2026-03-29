import json
from student import Student

##将学生对象数据以字典形式写入本地JSON文件：
def save_students(file_path:str,students:list):
      data = [student.to_dict() for student in students]

      with open (file_path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

##从JSON文件中读取学生数据，并将其转换为学生对象
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




    ##with:上下文管理器，代码块结束可以自动关闭文件，不需要手动f.close()
    ##open:打开指定路径的文件
    ##as f：给文件起别名
    ##结尾的：对打开的文件进行一下操作
    ##json.load：将JSON文件中的数据转换为python中的字典格式
    ##json.dump(...):将python数据转化为JSON格式文本，并写入JSON文件中
