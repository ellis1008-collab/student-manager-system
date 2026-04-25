# 学生信息管理系统

这是一个基于 Python、FastAPI、SQLite 和 SQLModel ORM 实现的学生信息管理系统项目。

项目最初是一个命令行学生信息管理系统，后续逐步演进为具备后端接口、数据库存储、ORM 操作、统一错误响应、接口文档和自动化测试的学习型后端工程项目。

---

## 1. 项目简介

本项目用于管理学生信息，支持学生数据的新增、查询、修改和删除。

当前项目同时保留了早期命令行版本，并已经完成 FastAPI 后端接口版本。后端版本已经接入 SQLite 数据库和 ORM 操作，并补充了统一错误响应结构、接口文档说明和自动化测试。

项目当前重点是：

- 巩固 Python 模块化开发能力
- 掌握 FastAPI 后端接口开发流程
- 理解请求体、响应体和参数校验
- 掌握 SQLite 数据库存储
- 理解 ORM 数据访问方式
- 掌握 FastAPI 的 APIRouter 路由拆分
- 掌握 Depends 依赖注入
- 建立统一错误响应结构
- 建立最小可用的自动化测试体系
- 形成更规范的后端项目结构

---

## 2. 技术栈

当前项目主要使用：

- Python
- FastAPI
- Pydantic
- SQLite
- SQLModel ORM
- pytest
- FastAPI TestClient
- Git / GitHub

---

## 3. 项目功能

### 3.1 命令行版本

命令行版本支持：

- 添加学生
- 查看所有学生
- 按学号查询学生
- 修改学生信息
- 删除学生信息
- 保存并退出

命令行版本主要文件：

- `main.py`
- `cli.py`
- `cli_service.py`
- `manager.py`
- `student.py`
- `json_storage.py`
- `data/students.json`

---

### 3.2 FastAPI 后端版本

FastAPI 后端版本支持：

- 获取学生列表
- 根据学号查询学生
- 新增学生
- 根据学号修改学生
- 根据学号删除学生
- 请求体字段校验
- 路径参数校验
- 学生存在性检查
- 统一错误响应
- Swagger UI 接口文档
- OpenAPI JSON 接口总说明书
- 自动化接口测试

当前主要接口：

| 方法 | 路径 | 说明 |
|---|---|---|
| `GET` | `/` | 根路径健康检查 |
| `GET` | `/students/` | 获取学生列表 |
| `POST` | `/students/` | 新增学生 |
| `GET` | `/students/{student_id}` | 根据学号获取学生 |
| `PUT` | `/students/{student_id}` | 根据学号修改学生 |
| `DELETE` | `/students/{student_id}` | 根据学号删除学生 |

---

## 4. 项目结构

当前项目结构大致如下：

```text
student_manager_cli/
├─ api.py
├─ main.py
├─ cli.py
├─ cli_service.py
├─ manager.py
├─ student.py
├─ service.py
├─ dependencies.py
├─ schemas.py
├─ json_storage.py
├─ db_storage.py
├─ db_models.py
├─ db_orm.py
├─ db_init.py
├─ db_demo.py
├─ routers/
│  ├─ __init__.py
│  └─ students.py
├─ tests/
│  ├─ conftest.py
│  ├─ test_api.py
│  ├─ test_student_dependencies.py
│  └─ test_request_validation.py
├─ data/
│  ├─ students.json
│  └─ students.db
├─ .gitignore
├─ pyproject.toml
└─ README.md
```

---

## 5. 核心模块说明

### 5.1 FastAPI 主线

- `api.py`  
  FastAPI 应用入口，负责创建 FastAPI 应用、注册路由、配置项目元信息，并实现全局异常处理器。

- `routers/students.py`  
  学生相关接口路由文件，负责定义学生的新增、查询、修改和删除接口。

- `dependencies.py`  
  FastAPI 依赖函数文件，负责路径参数 `student_id` 的校验，以及根据学号检查学生是否存在。

- `schemas.py`  
  Pydantic 模型文件，负责定义请求体模型、响应体模型、错误响应模型，以及接口文档中的示例数据。

- `service.py`  
  业务逻辑层，负责组织学生相关业务逻辑，并对接数据库操作层。

---

### 5.2 数据库主线

- `db_models.py`  
  ORM 表模型定义文件。

- `db_orm.py`  
  ORM 数据访问层，负责学生数据的增删改查。

- `db_storage.py`  
  早期 SQLite 数据访问代码，作为数据库学习过程的一部分保留。

- `db_init.py`  
  数据库初始化脚本，用于创建学生表。

- `db_demo.py`  
  数据库相关演示代码。

---

### 5.3 命令行主线

- `main.py`  
  命令行程序入口。

- `cli.py`  
  命令行交互逻辑。

- `cli_service.py`  
  命令行业务服务层。

- `manager.py`  
  学生对象管理逻辑。

- `student.py`  
  学生实体类。

- `json_storage.py`  
  JSON 文件读写逻辑。

---

### 5.4 测试主线

- `tests/conftest.py`  
  pytest 公共测试夹具文件，负责创建测试客户端和隔离测试数据库。

- `tests/test_api.py`  
  学生接口主流程测试，包括新增、查询、修改、删除和业务错误测试。

- `tests/test_student_dependencies.py`  
  依赖链测试，主要验证路径参数校验和学生存在性检查。

- `tests/test_request_validation.py`  
  请求体验证测试，主要验证缺字段、类型错误、范围错误、字符串长度错误和自定义校验错误。

---

## 6. 环境准备

建议使用虚拟环境运行项目。

在项目根目录执行：

```powershell
python -m venv .venv
```

激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装项目依赖：

```powershell
pip install fastapi uvicorn sqlmodel pytest httpx
```

如果后续项目中维护了 `requirements.txt`，也可以使用：

```powershell
pip install -r requirements.txt
```

---

## 7. 初始化数据库

在项目根目录执行：

```powershell
python db_init.py
```

该命令会初始化 SQLite 数据库和学生表。

---

## 8. 启动项目

启动 FastAPI 服务：

```powershell
uvicorn api:app --reload
```

启动成功后，终端会显示类似：

```text
Uvicorn running on http://127.0.0.1:8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

根路径返回：

```json
{
  "message": "Student Manager API is running"
}
```

---

## 9. 接口文档

### 9.1 Swagger UI

访问：

```text
http://127.0.0.1:8000/docs
```

`/docs` 是 FastAPI 自动生成的可视化接口调试页面，可以查看接口说明、请求参数、请求体示例、响应体示例，并可以直接发送请求进行测试。

---

### 9.2 OpenAPI JSON

访问：

```text
http://127.0.0.1:8000/openapi.json
```

`/openapi.json` 是机器可读的接口总说明书，包含接口路径、请求参数、请求体模型、响应模型、错误响应结构等信息。

---

## 10. 统一错误响应

项目当前已经实现统一错误响应结构。

错误响应格式如下：

```json
{
  "code": 400,
  "message": "请求数据不合法。",
  "errors": [
    {
      "field": null,
      "message": "学号必须是纯数字。"
    }
  ]
}
```

字段说明：

| 字段 | 含义 |
|---|---|
| `code` | HTTP 状态码 |
| `message` | 错误总说明 |
| `errors` | 详细错误列表 |
| `errors[].field` | 出错字段位置 |
| `errors[].message` | 具体错误原因 |

当前已处理的错误类型包括：

- `400`：请求数据不合法
- `404`：目标资源不存在
- `422`：请求参数校验失败

---

## 11. 运行测试

在项目根目录执行：

```powershell
python -m pytest
```

当前预期结果：

```text
21 passed
```

也可以使用简洁模式：

```powershell
python -m pytest -q
```

当前测试已经覆盖：

- 根路径健康检查
- 获取学生列表成功
- 新增学生成功
- 修改学生成功
- 删除学生成功
- 重复学号新增失败
- 修改不存在学生失败
- 删除不存在学生失败
- 路径参数不是纯数字时返回 400
- 学号合法但学生不存在时返回 404
- 请求体缺少字段时返回 422
- 请求体字段类型错误时返回 422
- 请求体字段范围错误时返回 422
- 请求体字符串长度错误时返回 422
- 自定义字段校验错误时返回 422

---

## 12. 当前项目阶段

当前项目已经完成阶段 4 的主要工程化内容：

- FastAPI 后端接口版本
- APIRouter 路由拆分
- Depends 依赖校验
- SQLite 数据库存储
- SQLModel ORM 主线接入
- Pydantic 请求体和响应体模型
- 统一错误响应结构
- 全局异常处理器
- 测试数据库隔离
- 自动化接口测试
- `/docs` 接口文档优化
- `/openapi.json` 接口总说明书优化
- Git / GitHub 版本管理

---

## 13. 学习说明

本项目是一个学习型工程项目，目标不是一次性完成复杂系统，而是通过持续迭代逐步掌握：

- Python 项目模块化
- 后端接口设计
- 数据库访问
- ORM 使用
- 接口文档维护
- 自动化测试
- Git 版本管理
- 工程化项目收口

当前项目已经从最初的命令行版本，逐步演进为一个具备基础工程结构的 FastAPI 后端项目。