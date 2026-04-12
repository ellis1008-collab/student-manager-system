from fastapi.testclient import TestClient
##导入可在本地进行自动化测试的测试工具类

from api import app

##本地接口调用器：
client = TestClient(app) 

##测试根目录接口函数（pytest会自动识别并运行以test开头的测试函数）：
def test_root_returns_running_message():
    
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Student Manager API is running"

##
def test_get_students_returns_list():
    response = client.get("/students")
    assert response.status_code == 200
    data = response.json()    
    assert isinstance(data,list)
