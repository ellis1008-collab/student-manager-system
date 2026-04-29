import pytest
import ai_client

from fastapi.testclient import TestClient

from api import app


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