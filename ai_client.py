import os
from openai import APIConnectionError, APIStatusError, OpenAI, OpenAIError, RateLimitError

BAILIAN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_MODEL = "qwen-plus"
DEFAULT_TIMEOUT = 20.0

def get_bailian_client() -> OpenAI:
    api_key=os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("DASHSCOPE_API_KEY 未配置，请先配置百炼 API KEY。")
    
    return OpenAI(
        api_key=api_key,
        base_url=BAILIAN_BASE_URL,
        timeout=DEFAULT_TIMEOUT,
    )

def generate_ai_reply(prompt:str) -> str:
    if not isinstance(prompt,str):
        raise ValueError("prompt 必须是字符串。")
    if not prompt.strip():
        raise ValueError("prompt 不能为空。")
    
    client = get_bailian_client()

    try:
        reply=client.responses.create(
            model=DEFAULT_MODEL,
            input=prompt,
        )
        
    except APIConnectionError as e:
        raise RuntimeError("无法连接百炼模型服务，请检查网络、代理或 base_url 配置。") from e
    
    except RateLimitError as e:
        raise RuntimeError("百炼模型服务当前限流，或 API 额度不足，请稍后重试或检查额度。") from e
    
    except APIStatusError as e:
        raise RuntimeError(f"百炼模型服务返回错误：status_code={e.status_code},message={e.message}") from e
    
    except OpenAIError as e:
        raise RuntimeError(f"百炼模型调用失败：{e}") from e
    
    ##避免直接报错，可在下面简单的主动报处理好的错误
    output_text = getattr(reply,"output_text",None)

    if not output_text:
        raise RuntimeError("百炼模型返回内容为空。")
    
    return output_text