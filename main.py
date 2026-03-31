from student import Student
from manager import StudentManager
from storage import load_students, save_students  ##读取/写入

def format_student(student):
    return (
        f"学号：{student.id}\n"
        f"姓名：{student.name}\n"
        f"年龄：{student.age}\n"
        f"专业：{student.major}\n"
        f"成绩：{student.score}\n"
        "------------------------"
    )

def show_menu():
    print("\n====== 学生信息管理系统 ======")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 按学号查询学生")
    print("4. 修改学生信息")
    print("5. 删除学生")
    print("6. 保存并退出")

def input_menu_choice():    ##菜单输入辅助函数
    while True:
        choice = input("请输入你的选择：").strip()
        if choice in ("1","2","3","4","5","6"):
            return choice
        print("输入无效,请输入 1~6 的数字。")

def input_non_empty(prompt):    ##非空输入辅助函数
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("输入不能为空,请重新输入。")

##整数范围输入辅助函数：
def input_int_in_range(prompt,field_name,min_value=None,max_value=None):
    while True:

        text = input(prompt).strip()

        try:
            value = int(text)
        except ValueError:
            print(f"{field_name}输入无效,请输入整数。")
            continue
        
        if min_value is not None and value < min_value:
            print(f"{field_name}不能小于{min_value}。")
            continue

        if max_value is not None and value > max_value:
            print(f"{field_name}不能大于{max_value}。")
            continue

        return value

def input_optional_text(prompt,current_value):   ##可选文本输入辅助函数
    text = input(prompt).strip()
    return text if text else current_value

##可选整数范围输入辅助函数：
def input_optional_int_in_range(prompt,field_name,current_value,min_value=None,max_value=None):
    while True:
        text = input(prompt).strip()

        if text == "":
            return current_value

        try:
            value = int(text)
        except ValueError:
            print(f"{field_name}输入无效,请输入整数,或直接回车保留原值。")
            continue

        if min_value is not None and value < min_value:
            print(f"{field_name}不能小于{min_value},或直接回车保留原值。")
            continue

        if max_value is not None and value > max_value:
            print(f"{field_name}不能大于{max_value},或直接回车保留原值。")
            continue
        return value

##添加学生学号时的校检：
def input_student_id(prompt):
    while True:
        text = input(prompt).strip()
        if text =="":
            print("学号不能为空，请重新输入。")
            continue
        if not text.isdigit():
            print("学号必须是纯数字，请重新输入。")
            continue
        return text

##添加学生姓名时的校检：
def input_name(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("姓名不能为空，请重新输入。")
            continue
        if text.isdigit():
            print("姓名不能为纯数字，请重新输入。")
            continue
        return text

##添加学生专业时的校检：
def input_major(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("成绩不能为空,请重新输入。")
            continue
        if text.isdigit():
            print("专业不能为纯数字，请重新输入。")
            continue
        return text

##修改学生姓名时的校检：
def input_optional_name(prompt,current_value):
    while True:
        text = input(prompt).strip()
        if text == "":
            return current_value
        if text.isdigit():
            print("姓名不能为纯数字,或者按回车保留原值。")
        return text

##修改学生信息时对专业的校检：
def input_optional_major(prompt,current_value):
    while True:
        text = input(prompt).strip()
        if text =="":
           return current_value
        if text.isdigit():
            print("专业不能为纯数字,或者回车保留原值。")
            continue
        return text
        

def add_student_flow(manager):
    print("\n====== 添加学生 ======")

    
    stu_id = input_student_id("请输入学号：")
    stu_name = input_name("请输入姓名：")
    stu_age = input_int_in_range("请输入年龄:","年龄",0,150)
    stu_major = input_major("请输入专业：")
    stu_score = input_int_in_range("请输入成绩：","成绩",0,100)

    try:
        student = Student(stu_id, stu_name, stu_age, stu_major, stu_score)
        manager.add_student(student)

        print("添加成功,学生信息如下：")
        print(format_student(student))
    except Exception as e:
        print("添加失败",e)


def update_student_flow(manager):
    print("\n====== 修改学生 ======")

    student_id = input("请输入要修改的学号：").strip()
    try:
        student = manager.find_student_by_id(student_id)
        if student is None:
            print("未找到对应学号的学生。")
            return
        print("当前学生信息如下：")
        print(format_student(student))

        new_name = input_optional_name(
            f"请输入新的姓名 (当前:{student.name},直接回车表示不修改):",
            student.name
        )
        new_age = input_optional_int_in_range(
            f"请输入新的年龄 (当前:{student.age},直接回车表示不修改):",
            "年龄",
            student.age,
            0,150
        )
        new_major = input_optional_major(
            f"请输入新的专业 (当前:{student.major},直接回车表示不修改):",
            student.major
        )
        new_score = input_optional_int_in_range(
            f"请输入新的成绩(当前：{student.score},直接回车表示不修改):",
            "成绩",
            student.score,
            0,
            100
        )


        manager.update_student_by_id(student_id, new_name, new_age, new_major, new_score)
    
        updated_student = manager.find_student_by_id(student_id)
        print("修改成功,修改后的学生信息如下:")
        print(format_student(updated_student))
    except Exception as e:
        print("修改异常：",e)

def delete_student_flow(manager):
    print("\n====== 删除学生 ======")

    student_id = input("请输入要删除的学号：").strip()

    try:
        student = manager.find_student_by_id(student_id)

        if student is None:
            print("未找到该学号对应的学生。")
            return
        print("即将删除的学生信息如下：")
        print(format_student(student))

        confirm = input("如确认删除,请输入:确认;如取消删除,请直接按回车。").strip()
        if confirm != "确认":
            print("删除已取消。")
            return

        manager.delete_student_by_id(student_id)
        print("删除成功。")
    except Exception as e:
        print("删除失败：",e)


def list_students_flow(manager):
    students = manager.list_students()

    if not students:
        print("当前没有学生数据。")
        return

    print("当前学生如下：")
    for student in students:
        print(format_student(student))


def find_student_flow(manager):
    student_id = input("请输入要查询的学号：").strip()

    try:
        student = manager.find_student_by_id(student_id)
        if student is None:
            print("没有找到该学号对应的学生。")
        else:
            print("找到的学生：")    ##也可以加\n
            print(format_student(student))
    except Exception as e:
        print("查询失败：", e)


def main():
    ##存储学生数据的本地json文件：
    file_path = "data/students.json"

    ##创建一个学生管理器变量：
    manager = StudentManager()

    ##从JSON文件中读取学生数据：
    loaded_students = load_students(file_path)

    ##将读取的学生数据添加到学生管理器变量中：
    for student in loaded_students:
        manager.add_student(student)

    ##对外输出学生数据个数：
    print(f"已加载 {len(manager.list_students())} 条学生数据。")

    ##按6选项才可退出菜单：
    while True:
        ##显示菜单与提示：
        show_menu()
        choice = input_menu_choice()
        ##选择：
        if choice == "1":
            add_student_flow(manager)   ##添加学生信息
        elif choice == "2":
            list_students_flow(manager)  ##输出管理器当中的学生信息
        elif choice == "3":
            find_student_flow(manager)   ##根据学号查询学生信息
        elif choice == "4":
            update_student_flow(manager)   ##根据学号修改学生
        elif choice == "5":
            delete_student_flow(manager)    ##根据学号删除学生
        elif choice == "6":
            ##存储学生信息：
            save_students(file_path, manager.list_students())
            print("数据已保存，程序退出，再见！")
            break
        else:
            print("输入无效,请输入 1~6 的数字。")


if __name__ == "__main__":
    main()