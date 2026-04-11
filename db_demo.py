import sqlite3

DB_PATH = "data/students.db"

##添加：
def insert_student(student_id,name,age,major,score):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO students
            (id,name,age,major,score)
            VALUES(?,?,?,?,?)
            """,(student_id,name,age,major,score))
        conn.commit()
        print("新增成功。")
    except sqlite3.IntegrityError:
        print(f"新增失败，学号{student_id}已存在。")
    finally:
        conn.close()

##读取全部学生：
def get_all_students():
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,name,age,major,score
        FROM students
        """)
        ##执行select之后，可以调用fetchall()得到的匹配行组成的列表
    rows = cursor.fetchall()
    conn.close()
    return rows

##列出所有学生：
def print_all_students():
    students = get_all_students()
    print("当前学生数据如下：")
    for student in students:
        print(student)


if __name__ == "__main__":
    insert_student("001","张三",18,"计算机科学与技术",95)
    insert_student("002","李四",19,"软件工程",88)
    insert_student("001","重复测试",20,"人工智能",90)

    print_all_students() 


