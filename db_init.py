import sqlite3

def init_db():
    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE 
    IF NOT EXISTS students
    (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL,
    score INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

    print("数据库初始化完成。")

if __name__ == "__main__":
    init_db()    