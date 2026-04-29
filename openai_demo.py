from ai_client import generate_ai_reply
from prompts import build_student_manager_prompt
def main():
    print("1. 程序开始运行")
    print("2. 正在通过 ai_client.py 调用百炼模型...")

    user_prompt = "请用一句话解释 FastAPI 在学生信息管理系统中的作用。"
    final_prompt = build_student_manager_prompt(user_prompt)

    try:
        reply = generate_ai_reply(final_prompt)
        print("3. 请求成功，模型返回：")
        print(reply)
    except Exception as e:
        print("3. 请求失败")
        print("错误类型：",type(e).__name__)
        print("错误内容：",e)

        
if __name__ == "__main__":
    main()
    