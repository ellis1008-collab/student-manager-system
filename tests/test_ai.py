from fastapi.testclient import TestClient

from api import app


client = TestClient(app)


def test_ai_reply_success(monkeypatch):
    def fake_generate_ai_reply(prompt: str) -> str:
        assert prompt == "请用一句话介绍 FastAPI。"
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