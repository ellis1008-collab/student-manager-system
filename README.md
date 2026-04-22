学生信息管理系统

这是一个基于 Python、FastAPI、SQLite 和 SQLModel ORM 实现的学生信息管理系统项目。

项目保留了早期的命令行版本，同时已经完成了基于 FastAPI + SQLite + ORM 的后端接口版本，并补充了最小测试体系与统一错误响应结构。

---

一、项目简介

本项目最初是一个基于 JSON 文件存储的命令行学生信息管理系统，后续逐步演进为一个具备后端接口、数据库存储、ORM 操作、自动化测试和接口文档的学习型工程项目。

当前项目的核心目标是：

- 巩固 Python 面向对象与模块化基础
- 掌握 FastAPI 后端开发基础流程
- 完成数据层从 JSON 到 SQLite 的升级
- 理解并实践 ORM（SQLModel）操作数据库
- 建立最小可用的接口测试体系
- 为后续更正规的工程结构改造做准备

---

二、当前已完成内容

1. 命令行版本

已完成命令行学生信息管理系统，支持：

- 添加学生
- 查看所有学生
- 按学号查询学生
- 修改学生信息
- 删除学生信息
- 保存并退出

命令行版本当前仍然保留，主要使用：

- "main.py"
- "cli.py"
- "cli_service.py"
- "manager.py"
- "student.py"
- "json_storage.py"
- "data/students.json"

---

2. FastAPI 后端版本

已完成基础学生管理接口：

- "GET /students"
- "GET /students/{student_id}"
- "POST /students"
- "PUT /students/{student_id}"
- "DELETE /students/{student_id}"

当前后端版本已经具备：

- 请求体模型
- 响应体模型
- 字段校验
- 自定义校验逻辑
- 统一错误响应结构
- Swagger 接口文档

---

3. 数据层升级

项目已经完成从 JSON 文件存储 到 SQLite 数据库存储 的升级。

已实现：

- SQLite 表初始化
- 基于 SQLite 的 CRUD
- 通过环境变量切换数据库路径
- ORM 主线接入

当前数据库相关文件包括：

- "db_init.py"
- "db_storage.py"
- "db_models.py"
- "db_orm.py"

---

4. ORM 接入

项目当前已经完成基于 SQLModel ORM 的最小 CRUD 闭环，包括：

- 建表
- 查询全部学生
- 按学号查询学生
- 新增学生
- 修改学生
- 删除学生

同时，项目已经将 "service.py" 切换到 ORM 主线，并通过服务层完成对象到字典的转换，使 API 层可以平滑接入 ORM。

---

5. 统一异常响应

项目当前已经实现统一错误响应结构，错误响应格式为：

- "code"
- "message"
- "errors"

已处理的错误类型包括：

- 请求参数校验错误
- 资源不存在错误
- 业务逻辑错误（如重复学号）

---

6. 自动化测试

项目已经建立最小自动化测试体系，使用：

- "pytest"
- "FastAPI TestClient"

并实现了测试数据库隔离。当前已覆盖的测试包括：

- 根接口健康检查
- 查询全部学生成功
- 创建学生成功
- 修改学生成功
- 删除学生成功
- 重复学号创建失败
- 修改不存在学生失败
- 删除不存在学生失败

测试文件：

- "tests/test_api.py"

测试配置文件：

- "pyproject.toml"

---

三、当前项目结构

student_manager_cli/
├─ api.py
├─ main.py
├─ cli.py
├─ cli_service.py
├─ manager.py
├─ student.py
├─ service.py
├─ json_storage.py
├─ db_storage.py
├─ db_models.py
├─ db_orm.py
├─ db_init.py
├─ db_demo.py
├─ tests/
│  └─ test_api.py
├─ data/
│  └─ students.json
├─ .gitignore
├─ pyproject.toml
└─ README.md

---

四、各文件作用说明

命令行主线

- "main.py"：命令行程序入口
- "cli.py"：命令行交互与输入处理
- "cli_service.py"：命令行服务层
- "manager.py"：学生对象管理逻辑
- "student.py"：学生实体类
- "json_storage.py"：JSON 文件读写

FastAPI / 数据库主线

- "api.py"：FastAPI 应用入口，接口定义、请求响应模型、异常处理
- "service.py"：服务层，负责业务逻辑组织与 ORM 结果转换
- "db_storage.py"：早期 SQLite 操作层
- "db_models.py"：ORM 表模型定义
- "db_orm.py"：ORM 数据操作层
- "db_init.py"：数据库初始化脚本
- "db_demo.py"：数据库相关演示代码

测试与配置

- "tests/test_api.py"：接口自动化测试
- "pyproject.toml"：pytest 配置
- ".gitignore"：Git 忽略规则

---

五、如何运行项目

1. 运行命令行版本

在项目根目录执行：

python main.py

---

2. 初始化 SQLite 数据库

在项目根目录执行：

python db_init.py

---

3. 启动 FastAPI 接口服务

在项目根目录执行：

uvicorn api:app --reload

启动后可在浏览器访问：

http://127.0.0.1:8000/docs

查看 Swagger 接口文档。

---

六、如何运行测试

在项目根目录执行：

python -m pytest

或：

python -m pytest -q

当前测试通过 "pyproject.toml" 配置，只收集 "tests" 目录下的测试文件。

---

七、当前项目特点

本项目当前具备以下特点：

- 同时保留命令行版本和 FastAPI 版本，便于对比学习
- 已完成从 JSON 到 SQLite 的数据层演进
- 已完成 ORM 主线接入
- 已建立最小测试体系
- 已实现统一错误响应
- 已开始进行接口文档收口
- 正在向更正规的 FastAPI 工程结构演进

---

八、下一步计划

项目下一阶段将继续推进：

- 多文件路由拆分
- "APIRouter" 路由分组
- "Depends" 依赖注入
- 配置分层
- 日志
- 数据库会话依赖

目标是逐步把当前项目从“学习型单文件后端”推进到“更规范的工程化 FastAPI 项目”。

---