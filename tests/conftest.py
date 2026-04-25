import sqlite3
import pytest
from fastapi.testclient import TestClient
from api import app

@pytest.fixture 
def client_with_test_db(tmp_path,monkeypatch):
    test_db_path = tmp_path / "test_students_db"

##monkeypatch.setenv("STUDENT_DB_PATH", str(test_db_path))
# 保证测试的时候连接临时数据库，正常运行业务的时候连接真实数据库：
    monkeypatch.setenv("STUDENT_DB_PATH", str(test_db_path))
    
    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE students(
                   id TEXT PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   major TEXT NOT NULL,
                   score INTEGER NOT NULL
                   )
                   """)
    cursor.executemany("""
                    INSERT INTO students(
                   id,name,age,major,score)
                   VALUES(?,?,?,?,?)
                   """,
                   [
                       ("001","张三",18,"计算机科学与技术",95),
                       ("002","李四",19,"软件工程",88)
                   ],
                   )
    conn.commit()
    conn.close()

    with TestClient(app) as client:
        yield client


##统一测试的错误响应的断言：
##结果为返回一个函数：
@pytest.fixture
def assert_error_response():
    def _assert_error_response(
            response,
            status_code:int,
            top_message:str,
            detail_message:str,
            field=None,
    ):
        assert response.status_code == status_code
        data=response.json()
        assert data["code"] == status_code
        assert data["message"] == top_message
        assert len(data["errors"]) == 1
        assert data["errors"][0]["field"] == field
        assert data["errors"][0]["message"] == detail_message

    return _assert_error_response


        
        
        
