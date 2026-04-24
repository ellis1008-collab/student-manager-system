from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

##测试不合法学号返回400
def test_get_student_with_invalid_id_should_return_400():
    response = client.get("/students/abc")
    assert response.status_code == 400
    
    data = response.json()

    assert data["code"] == 400
    assert data["message"] == "请求数据不合法。"
    assert data["errors"][0]["message"] == "学号必须是纯数字。"

##测试学号合法，其对应的学生不存在：
def test_get_student_with_not_found_id_should_return_404():
    client = TestClient(app)

    response = client.get("/students/999")
    assert response.status_code == 404
    
    data = response.json()
    
    assert data["code"] == 404
    assert data["message"] == "目标资源不存在。"
    assert data["errors"][0]["message"] == "未找到该学号对应的学生。"

##测试更新学生时的不合法学号：
def test_update_student_with_invalid_id_should_return_400():
    client = TestClient(app)

    response = client.put("/students/abc",
                          json={
                              "name":"张三",
                              "age":18,
                              "major":"软件工程",
                              "score":90,
                          }
                          )
    assert response.status_code == 400

    data = response.json()
    
    assert data["code"] == 400
    assert data["message"] == "请求数据不合法。"
    assert data["errors"][0]["message"] == "学号必须是纯数字。"

##测试删除学生时学号不合法，
def test_delete_student_with_invalid_id_should_return_400():
    client = TestClient(app)
    response = client.delete("/students/abc")
    assert response.status_code == 400
    
    data = response.json()
    
    assert data["code"] == 400
    assert data["message"] == "请求数据不合法。"
    assert data["errors"][0]["message"] == "学号必须是纯数字。"

