from prompts import build_student_manager_prompt

##检查用户问题是否在 prompt 中：
def test_build_student_manager_prompt_contains_user_prompt():
    user_prompt = "请解释 FastAPI 路由的作用。"

    final_prompt = build_student_manager_prompt(user_prompt)
    assert user_prompt in final_prompt


##测试规定的模板内容是否在 prompt 里面的内容是否在
def test_build_student_manager_prompt_contains_project_context():
    final_prompt = build_student_manager_prompt("测试问题")

    assert "学生信息管理系统" in final_prompt
    assert "Python 后端开发学习助手" in final_prompt

    assert "FastAPI" in final_prompt

    assert "阿里云百炼大模型 API " in final_prompt

##检查是否没有前后空白字符：
def test_build_student_manager_prompt_strips_extra_whitespace():
    final_prompt = build_student_manager_prompt("测试问题")
    assert final_prompt == final_prompt.strip()




