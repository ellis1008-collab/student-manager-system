from ai_client import generate_ai_reply
def main():
    print("1. 程序开始运行")
    print("2. 正在通过 ai_client.py 调用百炼模型...")

    try:
        reply = generate_ai_reply(
            "请用一句中文回答：AI 客户端封装测试成功。"
        )
        print("3. 请求成功，模型返回：")
        print(reply)
    except Exception as e:
        print("3. 请求失败")
        print("错误类型：",type(e).__name__)
        print("错误内容：",e)


if __name__ == "__main__":
    main()
    