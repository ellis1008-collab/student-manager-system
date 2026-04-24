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

##测试根目录：
def test_root_returns_running_message(client_with_test_db):
    response = client_with_test_db.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student Manager API is running"


##测试列出所有学生接口：
def test_get_students_returns_list(client_with_test_db):
    response = client_with_test_db.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    

##测试添加学生接口（成功版）：
def test_create_student_returns_201_and_creates_record(client_with_test_db):
    new_student = {
        "id": "003",
        "name": "王五",
        "age": 20,
        "major": "数据科学与技术",
        "score": 92
    }
    response = client_with_test_db.post("/students",json=new_student)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == "003"
    assert data["name"] == "王五"
    assert data["age"] == 20
    assert data["major"] == "数据科学与技术"
    assert data["score"] == 92

    list_response = client_with_test_db.get("/students")
    assert list_response.status_code == 200

    students = list_response.json()

    assert len(students) == 3
    assert any (student ["id"] == "003" for student in students)


##测试修改学生接口（成功版）：
def test_update_student_returns_200_and_updates_record(client_with_test_db):
    updated_student={
        "name": "张三同学",
        "age": 20,
        "major": "人工智能",
        "score": 96,
    }
    
    response = client_with_test_db.put("/students/001",json=updated_student)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == "001"
    assert data["name"] == "张三同学"
    assert data["age"] == 20
    assert data["major"] == "人工智能"
    assert data["score"] == 96

    list_response = client_with_test_db.get("/students")
    assert list_response.status_code == 200

    students = list_response.json()
    assert len(students) == 2
    student_001 = next(student for student in students if student["id"] == "001")
    assert student_001 ["name"] == "张三同学"
    assert student_001["age"] == 20
    assert student_001["major"] == "人工智能"
    assert student_001["score"] == 96

##测试删除学生接口（成功版）：
def test_delete_student_return_200_and_removes_record(client_with_test_db):
    response = client_with_test_db.delete("/students/001")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == "001"
    assert data["name"] =="张三"
    assert data["age"] == 18
    assert data["major"] == "计算机科学与技术"
    assert data["score"] == 95

    list_response = client_with_test_db.get("/students")

    assert list_response.status_code == 200
    students = list_response.json()
    assert len(students) == 1
    assert all(student["id"] != "001" for student in students)

##重复学号新增失败测试：
def test_create_student_with_duplicate_id_returns_400(client_with_test_db):
        duplicate_student = {
            "id" : "001",
            "name" : "新张三",
            "age" : 20,
            "major" : "人工智能",
            "score" : 99
        }
        
        response = client_with_test_db.post("/students",json=duplicate_student)
        assert response.status_code == 400
        
        data = response.json()
        assert data["code"] == 400
        assert data["message"] == "请求数据不合法。"
        assert len(data["errors"]) == 1
        assert data["errors"][0]["field"] is None
        assert data["errors"][0]["message"] == "学号已存在,不能重复添加。"

        list_response = client_with_test_db.get("/students")

        assert list_response.status_code == 200
        students = list_response.json()
        assert len(students) == 2
        assert any (student["id"] == "001" 
                    and student["name"] == "张三" for student in students)
        
##修改不存在学生失败测试：
def test_update_nonexistent_student_returns_404(client_with_test_db):
        update_student = {
            "name": "不存在的学生",
            "age":21,
            "major":"人工智能",
            "score": 90
        }
        response = client_with_test_db.put("/students/999",json=update_student)

        assert response.status_code == 404
        data = response.json()
        assert data["code"] == 404
        assert data["message"] == "目标资源不存在。"
        assert len(data["errors"]) == 1
        assert data["errors"][0]["field"] == None
        assert data["errors"][0]["message"] == "未找到该学号对应的学生。"

        list_response = client_with_test_db.get("/students")
        assert list_response.status_code == 200
        students = list_response.json()
        assert len(students) == 2

##删除不存在学生失败测试：
def test_delete_nonexistent_student_returns_404(client_with_test_db):
            response = client_with_test_db.delete("/students/999")
            
            assert response.status_code == 404

            data = response.json()
            assert data["code"] == 404
            assert data["message"] == "目标资源不存在。"
            assert len(data["errors"]) == 1
            assert data["errors"][0]["field"] == None
            assert data["errors"][0]["message"] == "未找到该学号对应的学生。"

            list_response = client_with_test_db.get("/students")
            assert list_response.status_code == 200
            students = list_response.json()
            assert len(students) == 2






