import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_title: str = "Student Manager API"
    app_description : str = (
        "基于 FastAPI 的学生信息管理系统后端接口，"
        "支持学生的新增、查询、修改、删除、以及统一错误响应。"
    )
    app_version : str = "0.4.4"

    database_path : str = os.getenv(
        "STUDENT_DB_PATH",
        "data/students.db",
    )

    log_level :str = os.getenv("LOG_LEVEL","INFO")
    
settings = Settings()