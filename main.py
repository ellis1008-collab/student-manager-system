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


def add_student_flow(manager):
    print("\n====== 添加学生 ======")
    stu_id = input("请输入学号：").strip()
    stu_name = input("请输入姓名：").strip()
    age_text = input("请输入年龄：").strip()
    stu_major = input("请输入专业：").strip()
    score_text = input("请输入成绩：").strip()

    try:
        ##try/except属于add_student_flow函数
        stu_age = int(age_text)
        stu_score = int(score_text)

        student = Student(stu_id,stu_name, stu_age, stu_major, stu_score)
        manager.add_student(student)
        print("添加成功,学生信息如下：")
        print(format_student(student))
    except Exception as e:
        print("添加失败：", e)


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

        new_name = input(f"请输入新的姓名：(当前：{student.name},直接回车表示不修改):").strip()
        age_text = input(f"请输入新的年龄：(当前：{student.age},直接回车不修改):").strip()
        new_major = input(f"请输入新的专业：(当前：{student.major},直接回车不修改):").strip()
        score_text = input(f"请输入新的成绩：(当前：{student.score},直接回车不修改):").strip()

        final_name = new_name if new_name else student.name
        final_age = int(age_text) if age_text else student.age
        final_major = new_major if new_major else student.major
        final_score = int(score_text) if score_text else student.score 

        manager.update_student_by_id(student_id,final_name,final_age,final_major,final_score)
    
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
        choice = input("请输入你的选择：").strip()
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
            print("输入无效，请输入 1~6 的数字。")


if __name__ == "__main__":
    main()