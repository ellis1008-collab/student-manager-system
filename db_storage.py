import sqlite3

DB_PATH = "data/students.db"


##连接函数：
def get_connection():
    return sqlite3.connect(DB_PATH)


##将返回的元组结构转换为字典结构   ：
def row_to_student_dict(row):
    return {
        "id": row[0],
        "name": row[1],
        "age": row[2],
        "major": row[3],
        "score": row[4],
    }


##添加学生：
def add_student_to_db(student_data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO students(id,
            name,age,major,score)
            VALUES(?,?,?,?,?)
            """,
            (
                student_data["id"],
                student_data["name"],
                student_data["age"],
                student_data["major"],
                student_data["score"],
            ),
        )
        conn.commit()
        return True, "新增成功。"
    except sqlite3.IntegrityError:  ##主要是主键冲突：比如学号已经存在，又添加相同学号
        return False, "学号已存在，不能重复添加。"
    finally:
        conn.close()


##列出所有学生：
def get_all_students_from_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,name,age,major,score
        FROM students
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return [row_to_student_dict(row) for row in rows]


##按学号查询学生：
def get_student_by_id_from_db(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,name,age,major,score
        FROM students
        WHERE id=?
        """,
        (student_id,),
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return row_to_student_dict(row)


##修改学生：
def update_student_by_id_in_db(student_id, student_data):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    UPDATE students
    SET name=?,age=?,major=?,score=?
    WHERE id=?
    """,
        (
            student_data["name"],
            student_data["age"],
            student_data["major"],
            student_data["score"],
            student_id
        ),
    )
    conn.commit()
    conn.close()


##删除学生：
def delete_student_by_id_from_db(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id=?
        """,
        (student_id,),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    student = {
        "id": "003",
        "name": "王五",
        "age": 20,
        "major": "数据科学",
        "score": 92,
    }

    result = add_student_to_db(student)
    print("新增结果：", result)
    print("全部学生:", get_all_students_from_db())
    print("查询 003: ", get_student_by_id_from_db("003"))
