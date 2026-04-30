import pytest
import ai_client

from fastapi.testclient import TestClient

from api import app
from prompts import build_student_advice_prompt

client = TestClient(app)

##保护型fixture:
@pytest.fixture(autouse=True)
def block_real_bailian_client(monkeypatch):
    def fake_get_bailian_client():
        raise AssertionError("测试期间不应该真实创建百炼客户端")
    monkeypatch.setattr(
        "ai_client.get_bailian_client",
        fake_get_bailian_client,
    )


##原来：测试接口是否直接把 prompt 传给generate_ai_reply:
##现在：测试是否成功使用了 prompt 模板，以及用户问题是否在：
def test_ai_reply_success(monkeypatch):
    def fake_generate_ai_reply(prompt: str) -> str:
        
        assert "请用一句话介绍 FastAPI。" in prompt
        assert "学生信息管理系统" in prompt
        assert "Python 后端开发学习助手" in prompt

        return "这是模拟的大模型回复。"

    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response = client.post(
        "/ai/reply",
        json={"prompt": "请用一句话介绍 FastAPI。"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "reply": "这是模拟的大模型回复。"
    }


##测试发生502异常（假调用，直接报错）：
def test_ai_reply_runtime_error(monkeypatch):
    def fake_generate_ai_reply(prompt: str) -> str:
        raise RuntimeError("模型服务暂时不可用")

    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response = client.post(
        "/ai/reply",
        json={"prompt": "请用一句话介绍 FastAPI。"},
    )

    assert response.status_code == 502

    body = response.json()
    assert body["code"] == 502
    assert body["errors"][0]["message"] == "模型服务暂时不可用"


##测试 prompt 为空(假调用，直接报错）：
def test_ai_reply_empty_prompt_validation_error(monkeypatch):
    def fake_generate_ai_reply(prompt:str) -> str:
        raise AssertionError("空 prompt 不应该调用模型")
    
    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response = client.post(
        "/ai/reply",
        json={"prompt":""},
        )
    assert response.status_code == 422
    body = response.json()

    assert body["code"] == 422
    assert body["errors"][0]["field"] == "请求体.prompt"
    assert "不能少于" in body["errors"][0]["message"]


##测试 prompt 过长：
def test_ai_reply_too_long_prompt_validation_error(monkeypatch):
    def fake_generate_ai_reply(prompt:str) -> str:
        raise AssertionError("过长 prompt 不应该调用模型")

    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    long_prompt = "a"*501

    response = client.post(
        "/ai/reply",
        json={"prompt":long_prompt},
    )

    assert response.status_code == 422
    body = response.json()

    assert body["code"] == 422
    assert body["errors"][0]["field"] == "请求体.prompt"
    assert "不能超过" in body["errors"][0]["message"]

##测试 prompt 进入路由函数为空字符串报400：
def test_ai_reply_value_Error(monkeypatch):
    def fake_generate_ai_reply(prompt:str) -> str:
        raise ValueError("prompt 内容不合法")
    
    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response = client.post(
        "ai/reply",
        json={"prompt":"   "},
    )

    assert response.status_code == 400

    body = response.json()
    assert body["code"] == 400
    assert body["errors"][0]["message"] == "prompt 内容不合法"


##保护型测试：
def test_ai_tests_block_real_bailian_client():
    with pytest.raises(AssertionError) as exc_info:
        ai_client.get_bailian_client()

    assert "测试期间不应该真实创建百炼客户端" in str(exc_info.value)

##测试根据已有学生生成学习建议成功：
def test_create_student_advice_success(client_with_test_db,monkeypatch):
    def fake_generate_ai_reply(prompt: str) -> str:
        assert prompt == build_student_advice_prompt(
            name="张三",
            major="计算机科学与技术",
            score=95,
        )
        return "建议张三继续巩固计算机专业基础。"
    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )
    response=client_with_test_db.post("/ai/students/001/advice")
    assert response.status_code == 200
    assert response.json() == {"advice":"建议张三继续巩固计算机专业基础。"}

##测试根据学生生成学习建议时，学号格式不合法返回400：
def test_create_student_advice_invalid_student_id_return_400(
    client_with_test_db,
    monkeypatch,
    assert_error_response,      
):
    def fake_generate_ai_reply(prompt: str) -> str:
        raise AssertionError("学号格式不合法时，不应该调用大模型。")
    
    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response=client_with_test_db.post("/ai/students/not-exist/advice")

    assert_error_response(
        response=response,
        status_code=400,
        top_message="请求数据不合法。",
        detail_message="学号必须是纯数字。",
    )

##测试根据学生生成学习建议时，学生不存在返回404：
def test_create_student_advice_not_found_returns_404(
        client_with_test_db,
        monkeypatch,
        assert_error_response,
):
    def fake_generate_ai_reply(prompt:str) -> str:
        raise AssertionError("学生不存在时，不应该调用大模型。")
    
    monkeypatch.setattr(
        "routers.ai.generate_ai_reply",
        fake_generate_ai_reply,
    )

    response=client_with_test_db.post("/ai/students/999999/advice")

    assert_error_response(
        response=response,
        status_code=404,
        top_message="目标资源不存在。",
        detail_message="未找到该学号对应的学生。",
    )  

