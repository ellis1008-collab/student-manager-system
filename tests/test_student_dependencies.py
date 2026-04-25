##测试按学号查询学生时学号不合法返回400
def test_get_student_with_invalid_id_should_return_400(
        client_with_test_db,
        assert_error_response,        
):
    response = client_with_test_db.get("/students/abc")
    assert_error_response(
        response=response,
        status_code=400,
        top_message="请求数据不合法。",
        detail_message="学号必须是纯数字。"
        )
    
##测试按学号查询学生时学号合法，其对应的学生不存在：
def test_get_student_with_not_found_id_should_return_404(
        client_with_test_db,
        assert_error_response,
        ):
   
    response = client_with_test_db.get("/students/999")
    assert_error_response(
        response=response,
        status_code=404,
        top_message="目标资源不存在。",
        detail_message="未找到该学号对应的学生。"
        )


##测试更新学生时的不合法学号：
def test_update_student_with_invalid_id_should_return_400(
        client_with_test_db,
        assert_error_response
        ):

    response = client_with_test_db.put("/students/abc",
                          json={
                              "name":"张三", 
                              "age":18,
                              "major":"软件工程",
                              "score":90,
                          }
                          )
    assert_error_response(
        response=response,
        status_code=400,
        top_message="请求数据不合法。",
        detail_message="学号必须是纯数字。"
        )


##测试删除学生时学号不合法，
def test_delete_student_with_invalid_id_should_return_400(
        client_with_test_db,
        assert_error_response
        ):
    
    response = client_with_test_db.delete("/students/abc")
    assert_error_response(
        response=response,
        status_code=400,
        top_message="请求数据不合法。",
        detail_message="学号必须是纯数字。"
        )
