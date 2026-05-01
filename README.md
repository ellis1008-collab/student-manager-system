# 学生信息管理系统

这是一个基于 Python、FastAPI、SQLite、SQLModel ORM、Docker 和阿里云百炼 DashScope 实现的学生信息管理系统项目。

项目最初是一个命令行学生信息管理系统，后续逐步演进为具备后端接口、数据库存储、ORM 操作、统一错误响应、接口文档、自动化测试、Docker 容器化运行和大模型接口能力的学习型后端工程项目。

---

## 1. 项目简介

本项目用于管理学生信息，支持学生数据的新增、查询、修改和删除。

当前项目同时保留了早期命令行版本，并已经完成 FastAPI 后端接口版本。后端版本已经接入 SQLite 数据库和 SQLModel ORM 操作，并补充了统一错误响应结构、接口文档说明、自动化测试、Docker Compose 启动配置和大模型 API 接入能力。

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
- 掌握 Docker 基础容器化运行
- 理解环境变量和 API Key 安全配置
- 初步接入大模型 API
- 建立 Prompt 模板和 AI 接口测试基础
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
- OpenAI Python SDK 兼容接口
- 阿里云百炼 DashScope
- Git / GitHub
- Docker
- Docker Compose

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

### 3.3 大模型接口版本

项目已经接入阿里云百炼 DashScope，并通过 OpenAI 兼容接口调用大模型。

当前 AI 接口：

| 方法 | 路径 | 说明 |
|---|---|---|
| `POST` | `/ai/reply` | 调用百炼模型生成回复 |
| `POST` | `/ai/students/{student_id}/advice` | 根据学生信息生成学习建议 |

AI 接口相关能力：

- 从环境变量读取 `DASHSCOPE_API_KEY`
- 使用 `ai_client.py` 封装模型调用逻辑
- 使用 `prompts.py` 统一管理 Prompt 模板
- 使用 Mock 机制测试 AI 接口，避免测试时真实调用大模型
- 支持 `/docs` 页面直接测试 AI 接口

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
├─ config.py
├─ logging_config.py
├─ json_storage.py
├─ db_storage.py
├─ db_models.py
├─ db_orm.py
├─ db_init.py
├─ db_demo.py
├─ ai_client.py
├─ openai_demo.py
├─ prompts.py
├─ routers/
│  ├─ __init__.py
│  ├─ students.py
│  └─ ai.py
├─ tests/
│  ├─ conftest.py
│  ├─ test_api.py
│  ├─ test_ai.py
│  ├─ test_prompts.py
│  ├─ test_student_dependencies.py
│  └─ test_request_validation.py
├─ data/
│  ├─ students.json
│  └─ students.db
├─ Dockerfile
├─ docker-compose.yml
├─ .dockerignore
├─ .env.example
├─ .gitignore
├─ .cursorignore
├─ requirements.txt
├─ pyproject.toml
└─ README.md
```

说明：

- `data/students.json` 是早期命令行版本使用的演示数据文件。
- `data/students.db` 是本地 SQLite 数据库文件，通常不应该提交到 GitHub。
- `.env` 用于保存本地真实配置，不应该提交到 GitHub。
- `.env.example` 用于说明项目需要哪些环境变量，可以提交到 GitHub。

---

## 5. 核心模块说明

### 5.1 FastAPI 主线

- `api.py`
  FastAPI 应用入口，负责创建 FastAPI 应用、注册路由、配置项目元信息，并实现全局异常处理器。

- `routers/students.py`
  学生相关接口路由文件，负责定义学生的新增、查询、修改和删除接口。

- `routers/ai.py`
  AI 相关接口路由文件，负责定义 `/ai/reply` 和 `/ai/students/{student_id}/advice` 接口。

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

### 5.4 大模型主线

- `ai_client.py`
  封装阿里云百炼 DashScope 的 OpenAI 兼容客户端，负责读取 `DASHSCOPE_API_KEY` 并调用模型。

- `prompts.py`
  集中管理项目中的大模型 Prompt 模板。

- `openai_demo.py`
  命令行演示脚本，用于单独测试大模型调用是否正常。

---

### 5.5 测试主线

- `tests/conftest.py`
  pytest 公共测试夹具文件，负责创建测试客户端和隔离测试数据库。

- `tests/test_api.py`
  学生接口主流程测试，包括新增、查询、修改、删除和业务错误测试。

- `tests/test_student_dependencies.py`
  依赖链测试，主要验证路径参数校验和学生存在性检查。

- `tests/test_request_validation.py`
  请求体验证测试，主要验证缺字段、类型错误、范围错误、字符串长度错误和自定义校验错误。

- `tests/test_ai.py`
  AI 接口测试文件，使用 Mock 机制避免测试时真实调用大模型。

- `tests/test_prompts.py`
  Prompt 模板测试文件，验证 Prompt 构建结果是否包含必要项目上下文。

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
pip install -r requirements.txt
```

如果没有使用 `requirements.txt`，也可以手动安装主要依赖：

```powershell
pip install fastapi uvicorn sqlmodel pytest httpx openai
```

---

## 7. 初始化数据库

在项目根目录执行：

```powershell
python db_init.py
```

该命令会初始化 SQLite 数据库和学生表。

如果使用 Docker Compose 启动项目，项目启动时也会自动创建数据库目录和数据表。

---

## 8. 启动项目

### 8.1 开发环境启动

开发阶段可以使用 `--reload` 参数启动服务：

```powershell
uvicorn api:app --reload
```

`--reload` 的作用是监听代码变化，保存代码后自动重启服务，适合本地开发和调试。

启动成功后，访问：

```text
http://127.0.0.1:8000
```

接口文档地址：

```text
http://127.0.0.1:8000/docs
```

---

### 8.2 生产风格启动

生产环境不建议使用 `--reload`，可以使用下面的方式启动：

```powershell
uvicorn api:app --host 127.0.0.1 --port 8000
```

含义：

| 部分 | 含义 |
|---|---|
| `api:app` | 从 `api.py` 文件中找到 `app` 这个 FastAPI 应用对象 |
| `--host 127.0.0.1` | 只允许本机访问 |
| `--port 8000` | 服务运行在 8000 端口 |
| 不使用 `--reload` | 避免生产环境监听文件变化 |

访问地址：

```text
http://127.0.0.1:8000/docs
```

---

### 8.3 端口说明

如果 8000 端口被占用，可以换成 8001：

```powershell
uvicorn api:app --host 127.0.0.1 --port 8001
```

对应访问地址也要改成：

```text
http://127.0.0.1:8001/docs
```

端口可以理解为服务的门牌号：

```text
127.0.0.1:8000
```

表示访问本机 8000 端口上的服务。

---

### 8.4 `127.0.0.1` 和 `0.0.0.0` 的区别

| Host | 含义 | 常见用途 |
|---|---|---|
| `127.0.0.1` | 只允许本机访问 | 本地开发、本地测试 |
| `0.0.0.0` | 监听所有网络入口 | Docker、服务器部署、局域网访问 |

本地学习和开发阶段，优先使用：

```powershell
uvicorn api:app --host 127.0.0.1 --port 8000
```

Docker 或服务器部署时，通常会使用：

```powershell
uvicorn api:app --host 0.0.0.0 --port 8000
```

注意：`0.0.0.0` 可能触发 Windows 防火墙提示，因为它允许外部设备尝试访问当前服务。

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

| 状态码 | 含义 |
|---|---|
| `400` | 请求数据不合法 |
| `404` | 目标资源不存在 |
| `422` | 请求参数校验失败 |
| `502` | 大模型服务调用失败 |

---

## 11. 运行测试

在项目根目录执行：

```powershell
python -m pytest
```

当前测试结果：

```text
36 passed
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
- AI 接口正常响应测试
- AI 接口异常响应测试
- Prompt 模板构建测试
- 测试期间禁止真实调用大模型

---

## 12. Docker 容器化运行

本项目支持使用 Docker 和 Docker Compose 在本地启动 FastAPI 后端服务。

Docker 的作用是把 Python 环境、项目依赖、项目代码和启动命令统一打包，减少不同电脑或服务器环境不一致导致的问题。

---

### 12.1 Docker 相关文件

项目根目录下包含以下 Docker 相关文件：

| 文件 | 作用 |
|---|---|
| `Dockerfile` | 定义如何构建项目镜像 |
| `docker-compose.yml` | 定义容器启动配置 |
| `.dockerignore` | 定义构建镜像时忽略哪些文件 |
| `.env.example` | 提供环境变量配置示例 |

`.dockerignore` 中已经排除了 `.venv/`、`.git/`、`.env`、缓存文件和数据库文件，避免把无关文件或敏感配置打包进镜像。

---

### 12.2 使用 Docker Compose 启动项目

推荐使用 Docker Compose 启动项目。

在项目根目录执行：

```powershell
docker compose up --build
```

该命令会根据 `Dockerfile` 和 `docker-compose.yml` 构建并启动服务。

启动成功后，访问：

```text
http://127.0.0.1:8000/docs
```

如果需要后台运行，可以使用：

```powershell
docker compose up -d --build
```

---

### 12.3 查看服务状态和日志

查看服务状态：

```powershell
docker compose ps
```

查看服务日志：

```powershell
docker compose logs app
```

如果日志中看到类似内容，说明服务启动正常：

```text
Application startup complete.
Uvicorn running on http://0.0.0.0:8000
```

---

### 12.4 停止 Docker 服务

如果当前终端正在前台运行 Docker Compose，可以按：

```text
Ctrl + C
```

停止服务。

如果是后台运行，可以执行：

```powershell
docker compose down
```

该命令会停止并删除由 Docker Compose 创建的容器和默认网络。

---

### 12.5 数据持久化说明

项目通过 `docker-compose.yml` 将本机 `data` 目录挂载到容器内部：

```text
./data:/app/data
```

这表示：

```text
容器内部读写 /app/data
实际对应本机项目目录下的 data 目录
```

因此，即使容器被删除，本机 `data` 目录中的数据库文件仍然可以保留。

---

## 13. 环境变量与安全配置

本项目通过环境变量管理配置。

项目中提供了：

```text
.env.example
```

作为环境变量示例文件。

首次本地运行时，可以复制一份 `.env`：

```powershell
Copy-Item .env.example .env
```

`.env.example` 可以提交到 GitHub，用于说明项目需要哪些环境变量。

`.env` 通常保存本地真实配置，例如 API Key、数据库路径等，不应该提交到 GitHub。

---

### 13.1 当前环境变量

| 环境变量 | 作用 |
|---|---|
| `STUDENT_DB_PATH` | 设置学生数据库文件路径 |
| `LOG_LEVEL` | 设置日志输出等级 |
| `DASHSCOPE_API_KEY` | 阿里云百炼 DashScope API Key |

---

### 13.2 API Key 安全规则

API Key 属于敏感信息，不能直接写入代码、README、测试文件或提交到 GitHub。

禁止这样写：

```python
api_key = "sk-xxx"
```

正确做法是从环境变量读取：

```python
api_key = os.getenv("DASHSCOPE_API_KEY")
```

本项目当前已经采用环境变量读取方式。

---

### 13.3 Windows PowerShell 配置百炼 API Key

在 Windows PowerShell 中，可以使用下面命令配置用户级环境变量：

```powershell
setx DASHSCOPE_API_KEY "你的真实百炼API_KEY"
```

配置完成后，需要重新打开 VS Code 或重新打开终端，让新的环境变量生效。

安全检查是否配置成功：

```powershell
python -c "import os; print('DASHSCOPE_API_KEY 已配置' if os.getenv('DASHSCOPE_API_KEY') else 'DASHSCOPE_API_KEY 未配置')"
```

注意：不要直接打印真实 API Key。

---

### 13.4 不应该提交的内容

以下内容不应该提交到 GitHub：

```text
.env
.venv/
__pycache__/
.pytest_cache/
data/*.db
.claude/
.vscode/
```

本项目已经在 `.gitignore` 和 `.dockerignore` 中排除了这些内容。

---

## 14. 大模型接口能力

本项目已经接入阿里云百炼 DashScope，并通过 OpenAI 兼容接口进行调用。

这里的 OpenAI 兼容接口，意思是：

```text
当前实际使用的是阿里云百炼模型，
但代码调用方式兼容 OpenAI Python SDK 的接口格式。
```

---

### 14.1 相关文件

| 文件 | 作用 |
|---|---|
| `ai_client.py` | 封装百炼 OpenAI 兼容客户端，负责读取 `DASHSCOPE_API_KEY` 并调用模型 |
| `prompts.py` | 集中管理大模型 Prompt 模板 |
| `routers/ai.py` | AI 接口路由文件 |
| `openai_demo.py` | 命令行演示脚本，用于单独测试大模型调用 |
| `tests/test_ai.py` | AI 接口测试文件 |
| `tests/test_prompts.py` | Prompt 模板测试文件 |

---

### 14.2 当前 AI 接口

| 方法 | 路径 | 说明 |
|---|---|---|
| `POST` | `/ai/reply` | 调用百炼模型生成回复 |
| `POST` | `/ai/students/{student_id}/advice` | 根据学生信息生成学习建议 |

---

### 14.3 `/ai/reply` 示例

请求体示例：

```json
{
  "prompt": "请用一句话介绍 FastAPI。"
}
```

响应体示例：

```json
{
  "reply": "FastAPI 是一个用于构建高性能 Python Web API 的现代框架。"
}
```

---

### 14.4 `/ai/students/{student_id}/advice` 示例

请求路径示例：

```text
POST /ai/students/001/advice
```

接口作用：

```text
根据指定学生的信息，调用大模型生成学习建议。
```

注意：该接口需要提前配置 `DASHSCOPE_API_KEY`，否则无法真实调用百炼模型服务。

---

### 14.5 Prompt 工程基础

项目中的用户原始输入不会直接发送给大模型，而是会先通过 `prompts.py` 进行包装。

当前 Prompt 构建函数：

```python
build_student_manager_prompt(user_prompt: str) -> str
```

它的作用是：

- 接收用户原始问题
- 加入学生信息管理系统项目背景
- 加入 Python 后端开发学习助手角色
- 加入中文回答、结合项目、不编造不存在功能等约束
- 返回最终发送给大模型的完整 Prompt

这样可以让 AI 回复更加稳定、贴合项目上下文。

---

### 14.6 AI 接口测试与 Mock 机制

本项目为 AI 接口补充了自动化测试，并通过 Mock 机制避免测试时真实调用阿里云百炼大模型。

测试重点包括：

- `/ai/reply` 正常返回时，接口返回 `200`
- 大模型调用异常时，接口返回对应错误响应
- `prompt` 为空字符串时，接口返回 `422`
- `prompt` 超过最大长度时，接口返回 `422`
- 测试期间禁止真实创建百炼客户端，避免误调用真实 API

这样可以保证测试稳定运行，同时避免消耗真实 API 额度。

---

## 15. 当前项目阶段

当前项目已经完成学生信息管理系统的主要工程化收尾内容。

已完成能力包括：

- 命令行版本
- FastAPI 后端接口版本
- APIRouter 路由拆分
- Depends 依赖校验
- SQLite 数据库存储
- SQLModel ORM 主线接入
- Pydantic 请求体和响应体模型
- 统一错误响应结构
- 全局异常处理器
- 自动化接口测试
- `/docs` Swagger UI 接口文档
- `/openapi.json` OpenAPI 接口总说明书
- Git / GitHub 基础版本管理
- `.gitignore` 与 `.dockerignore` 安全基线
- `.env.example` 配置模板
- Dockerfile 容器化构建
- Docker Compose 启动配置
- 阿里云百炼 DashScope 大模型接口接入
- Prompt 模板拆分
- AI 接口 Mock 测试

当前推荐启动方式：

```powershell
docker compose up --build
```

当前推荐接口访问地址：

```text
http://127.0.0.1:8000/docs
```

---

## 16. 学习说明

本项目是一个学习型工程项目。

项目目标不是一次性完成复杂系统，而是通过持续迭代逐步掌握：

- Python 项目模块化
- 后端接口设计
- 数据库访问
- ORM 使用
- 接口文档维护
- 自动化测试
- Git 版本管理
- Docker 基础部署
- 大模型 API 接入
- Prompt 工程基础

当前项目已经从最初的命令行版本，逐步演进为一个具备基础工程结构的 FastAPI 后端项目。
