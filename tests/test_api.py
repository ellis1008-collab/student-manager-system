import sqlite3

import pytest
from fastapi.testclient import TestClient

from api import app


@pytest.fixture   ##声明下面的函数是夹具函数：
def client_with_test_db(tmp_path, monkeypatch):
    test_db_path = tmp_path / "test_students.db"

    monkeypatch.setenv("STUDENT_DB_PATH", str(test_db_path))

    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            major TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    cursor.executemany(
        """
        INSERT INTO students (id, name, age, major, score)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            ("001", "张三", 18, "计算机科学与技术", 95),
            ("002", "李四", 19, "软件工程", 88),
        ],
    )

    conn.commit()
    conn.close()
    
    with TestClient(app) as client:
        yield client


def test_root_returns_running_message(client_with_test_db):
    response = client_with_test_db.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student Manager API is running"


def test_get_students_returns_list(client_with_test_db):
    response = client_with_test_db.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2