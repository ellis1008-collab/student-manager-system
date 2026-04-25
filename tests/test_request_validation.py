##测试添加学生时缺少 score 字段，返回422：
def test_create_student_missing_score_should_return_422(
        client_with_test_db,
        assert_error_response,
):
    new_student = {
        "id": "003",
        "name": "王五",
        "age": 20,
        "major":"数据科学与技术",
    }
    response = client_with_test_db.post("/students",json=new_student)
    
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="该字段是必填项。",
        field="请求体.score",
    )


##测试修改学生时 age 不是整数，返回422：
def test_update_student_age_not_integer_should_return_422(
        client_with_test_db,
        assert_error_response,
):
    updated_student={
        "name": "张三同学",
        "age": "十八岁",
        "major": "人工智能",
        "score": 96,
    }

    response=client_with_test_db.put("/students/001",json=updated_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="该字段必须是整数。",
        field="请求体.age",
        )


##测试添加学生时姓名是纯数字，返回422：
def test_create_student_name_all_digits_should_return_422(
  client_with_test_db,
  assert_error_response,      
):
    new_student={
        "id": "003",
        "name": "123",
        "age": 20,
        "major": "数据科学与技术",
        "score": 92,
    }
    
    response=client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="姓名不能是纯数字。",
        field="请求体.name",
    )


##测试添加学生时 age 超过 150 ，返回422：
def test_create_student_age_too_large_should_return_422(
        client_with_test_db,
        assert_error_response,
):
    new_student = {
        "id": "003",
        "name": "王五",
        "age": 151,
        "major": "数据科学与技术",
        "score": 92,
    }

    response = client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="输入值必须小于等于150。",
        field="请求体.age",
    )


##测试添加学生时 score 超过 100 ，返回422：
def test_create_student_score_too_large_should_return_422(
        client_with_test_db,
        assert_error_response
):
    new_student = {
        "id": "003",
        "name": "王五",
        "age": 20,
        "major": "数据科学与技术",
        "score": 101,
    }
    response=client_with_test_db.post("/students",json=new_student)

    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="输入值必须小于等于100。",
        field="请求体.score",
    )

##测试添加学生时 age 小于 0 ，返回422：
def test_create_student_age_too_small_should_return_422(
  client_with_test_db,
  assert_error_response,      
):
    new_student = {
        "id": "003",
        "name": "张三",
        "age": -1,
        "major": "数据科学与技术",
        "score": 92,
    }
    response=client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="输入值必须大于等于0。",
        field="请求体.age",
    )

##测试添加学生时 score 小于 0 ，返回422：
def test_create_student_score_too_small_should_return_422(
        client_with_test_db,
        assert_error_response
):
    new_student = {
        "id": "003",
        "name": "张三",
        "age": 20,
        "major": "数据科学与技术",
        "score": -1,
    }
   
    response=client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="输入值必须大于等于0。",
        field="请求体.score",
    )

##测试添加学生时 name 为空字符串，返回422：
def test_create_student_name_too_short_should_return_422(
        client_with_test_db,
        assert_error_response,
):
    new_student = {
        "id": "003",
        "name": "",
        "age": 20,
        "major": "数据科学与技术",
        "score": 92,
    }

    response=client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="字符串长度不能少于 1 个字符。",
        field="请求体.name",
    )

##测试添加学生时 name 超过20个字符，返回422：
def test_create_student_name_too_long_should_return_422(
        client_with_test_db,
        assert_error_response,
):
    new_student = {
        "id": "003",
        "name": "张"*21,
        "age": 20,
        "major": "数据科学与技术",
        "score": 92,
    }
    response=client_with_test_db.post("/students",json=new_student)
    assert_error_response(
        response=response,
        status_code=422,
        top_message="请求参数校检失败。",
        detail_message="字符串长度不能超过 20 个字符。",
        field="请求体.name",
    )