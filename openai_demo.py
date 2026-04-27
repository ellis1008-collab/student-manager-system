import os
from openai import OpenAI

def main():
    print("1. 程序开始运行")

    if not os.getenv("DASHSCOPE_API_KEY"):
        print("2.DASHSCOPE_API_KEY 未配置")
        return
    print("2. DASHSCOPE_API_KEY 已读取")
    print("3. 正在创建百炼 OpenAI 兼容 client")

    client = OpenAI(
        api_key = os.getenv("DASHSCOPE_API_KEY"),
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        timeout=20.0,
    )
    print("4. 正在发送请求，请等待...")

    try:
        response = client.responses.create(
            model = "qwen-plus",
            input="请用一句中文回答：大模型 API 对 python 后端项目有什么作用？",
        )
        print("5. 请求成功，模型返回：")
        print(response.output_text)

    except Exception as e:
        print("5. 请求失败")
        print("错误类型：",type(e).__name__)
        print("错误内容：",e)


if __name__ == "__main__":
        main()







