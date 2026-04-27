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

- `api:app`：从 `api.py` 文件中找到 `app` 这个 FastAPI 应用对象
- `--host 127.0.0.1`：只允许本机访问
- `--port 8000`：服务运行在 8000 端口
- 不使用 `--reload`：避免生产环境监听文件变化

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

## 12. Docker 容器化运行

本项目已经支持使用 Docker 构建镜像并运行容器。

Docker 可以将 Python 环境、项目依赖、项目代码和启动命令统一打包，减少不同电脑或服务器环境不一致导致的问题。

---

### 12.1 Docker 相关文件说明

项目根目录下包含以下 Docker 相关文件：

| 文件 | 作用 |
|---|---|
| `Dockerfile` | 定义如何构建项目镜像 |
| `.dockerignore` | 定义构建镜像时需要忽略的文件 |

其中：

- `Dockerfile` 用来告诉 Docker 如何安装依赖、复制代码、启动 FastAPI 服务。
- `.dockerignore` 用来避免将 `.venv/`、缓存文件、数据库文件、`.env` 等无关或敏感文件复制进镜像。

---

### 12.2 构建 Docker 镜像

在项目根目录执行：

```powershell
docker build -t student-manager-api:latest .
```

命令说明：

| 部分 | 含义 |
|---|---|
| `docker build` | 构建 Docker 镜像 |
| `-t student-manager-api:latest` | 给镜像命名为 `student-manager-api`，标签为 `latest` |
| `.` | 使用当前目录作为构建上下文 |

构建成功后，可以查看本地镜像：

```powershell
docker images
```

如果看到类似下面内容，说明镜像构建成功：

```text
student-manager-api:latest
```

---

### 12.3 运行 Docker 容器

执行：

```powershell
docker run -d --name student-manager-api-container -p 8000:8000 student-manager-api:latest
```

命令说明：

| 部分 | 含义 |
|---|---|
| `docker run` | 根据镜像创建并运行容器 |
| `-d` | 后台运行容器 |
| `--name student-manager-api-container` | 给容器命名 |
| `-p 8000:8000` | 将本机 8000 端口映射到容器内部 8000 端口 |
| `student-manager-api:latest` | 使用该镜像启动容器 |

启动成功后，访问接口文档：

```text
http://127.0.0.1:8000/docs
```

---

### 12.4 查看正在运行的容器

```powershell
docker ps
```

如果看到：

```text
student-manager-api-container
0.0.0.0:8000->8000/tcp
```

说明容器正在运行，并且端口映射成功。

---

### 12.5 查看容器日志

```powershell
docker logs student-manager-api-container
```

如果看到类似：

```text
Uvicorn running on http://0.0.0.0:8000
GET /docs HTTP/1.1 200 OK
GET /openapi.json HTTP/1.1 200 OK
```

说明 FastAPI 服务已经在 Docker 容器中正常运行。

---

### 12.6 停止并删除容器

停止容器：

```powershell
docker stop student-manager-api-container
```

删除容器：

```powershell
docker rm student-manager-api-container
```

注意：

```text
删除容器不会删除镜像。
```

镜像 `student-manager-api:latest` 仍然保留在本机，可以继续用来重新创建容器。

---

### 12.7 Docker 运行流程总结

完整 Docker 运行流程如下：

```text
Dockerfile
→ docker build
→ 镜像 image
→ docker run
→ 容器 container
→ FastAPI 服务启动
→ 浏览器访问 /docs
```

常用命令汇总：

```powershell
docker build -t student-manager-api:latest .
docker images
docker run -d --name student-manager-api-container -p 8000:8000 student-manager-api:latest
docker ps
docker logs student-manager-api-container
docker stop student-manager-api-container
docker rm student-manager-api-container
```

## 13. Docker 部署前检查与数据持久化

本项目在 Docker 容器中运行时，支持通过环境变量控制运行配置，并支持将本机 `data` 目录挂载到容器内部，实现 SQLite 数据库文件持久化。

---

### 13.1 环境变量配置

项目通过 `config.py` 读取环境变量：

| 环境变量 | 默认值 | 作用 |
|---|---|---|
| `STUDENT_DB_PATH` | `data/students.db` | 设置学生数据库文件路径 |
| `LOG_LEVEL` | `INFO` | 设置日志输出等级 |

示例：

```powershell
docker run -d --name student-manager-api-container -p 8000:8000 -e LOG_LEVEL=INFO student-manager-api:latest
```

其中：

```text
-e LOG_LEVEL=INFO
```

表示向容器传入日志等级配置。

---

### 13.2 容器内数据库自动初始化

项目启动时会自动创建数据库目录和数据表。

启动流程包括：

```text
FastAPI 启动
→ 读取配置
→ 创建 data 目录
→ 创建 students 表
→ 启动接口服务
```

这样可以避免 Docker 容器中出现：

```text
sqlite3.OperationalError: no such table: students
```

即使容器中没有提前准备好的 `students.db` 文件，项目也可以在启动时自动初始化数据库结构。

---

### 13.3 容器数据丢失问题

默认情况下，如果数据库文件只保存在容器内部：

```text
/app/data/students.db
```

那么删除容器后，容器内部的数据也会丢失。

区别如下：

| 操作 | 数据是否保留 |
|---|---|
| `docker stop 容器名` | 保留 |
| `docker start 容器名` | 保留 |
| `docker rm 容器名` | 容器内部数据丢失 |

因此，重要数据不应该只保存在容器内部。

---

### 13.4 挂载 data 目录实现数据持久化

推荐在运行容器时，将本机项目目录下的 `data` 目录挂载到容器内部：

```powershell
docker run -d --name data-persist-test -p 8000:8000 -v "${PWD}\data:/app/data" student-manager-api:latest
```

其中：

| 部分 | 含义 |
|---|---|
| `-v` | 挂载目录 |
| `${PWD}\data` | 本机当前项目下的 `data` 目录 |
| `/app/data` | 容器内部的 `data` 目录 |

挂载后：

```text
容器读写 /app/data/students.db
实际就是读写本机 data/students.db
```

这样即使删除容器，数据库文件仍然保留在本机项目的 `data` 目录中。

---

### 13.5 更安全的本地端口绑定

本地开发和部署前检查时，推荐使用：

```powershell
-p 127.0.0.1:8000:8000
```

完整示例：

```powershell
docker run -d --name deploy-check -p 127.0.0.1:8000:8000 -e LOG_LEVEL=INFO -v "${PWD}\data:/app/data" student-manager-api:latest
```

含义：

```text
只允许本机通过 127.0.0.1:8000 访问服务
不主动暴露给局域网其他设备
```

访问地址：

```text
http://127.0.0.1:8000/docs
```

---

### 13.6 Docker 部署前检查流程

部署前可以按以下流程检查项目是否正常：

```powershell
python -m pytest
docker build -t student-manager-api:latest .
docker images
docker rm -f deploy-check
docker run -d --name deploy-check -p 127.0.0.1:8000:8000 -e LOG_LEVEL=INFO -v "${PWD}\data:/app/data" student-manager-api:latest
docker ps
docker logs deploy-check
```

然后浏览器访问：

```text
http://127.0.0.1:8000/docs
```

至少检查：

```text
GET /students/
POST /students/
```

检查完成后，停止并删除检查容器：

```powershell
docker stop deploy-check
docker rm deploy-check
```

---

### 13.7 Docker 运行配置总结

完整链路如下：

```text
读取环境变量
→ 自动初始化数据库
→ 挂载 data 目录
→ 启动 FastAPI 容器
→ 访问 /docs
→ 验证接口
→ 停止并删除检查容器
```

推荐的本地部署前检查命令：

```powershell
docker run -d --name deploy-check -p 127.0.0.1:8000:8000 -e LOG_LEVEL=INFO -v "${PWD}\data:/app/data" student-manager-api:latest
```

## 14. Docker Compose 启动项目

本项目支持使用 Docker Compose 管理容器启动配置。

Docker Compose 可以把原本较长的 `docker run` 命令整理到 `docker-compose.yml` 文件中，统一管理镜像构建、容器名称、端口映射、环境变量和数据挂载配置。

---

### 14.1 Docker Compose 配置文件

项目根目录下包含：

```text
→ docker-compose.yml
```

该文件用于定义 FastAPI 服务的容器运行方式。

当前配置包含：

| 配置项 | 作用 |
|---|---|
| `build` | 根据当前目录下的 `Dockerfile` 构建镜像 |
| `image` | 指定镜像名称 |
| `container_name` | 指定容器名称 |
| `ports` | 设置端口映射 |
| `environment` | 设置环境变量 |
| `volumes` | 挂载本机 `data` 目录到容器内部 |

---

### 14.2 启动服务

在项目根目录执行：

```powershell
→ docker compose up -d
```

含义：

| 部分 | 含义 |
|---|---|
| `docker compose` | 使用 Docker Compose |
| `up` | 根据 `docker-compose.yml` 创建并启动服务 |
| `-d` | 后台运行容器 |

启动成功后，可以访问：

```text
→ http://127.0.0.1:8000/docs
```

---

### 14.3 查看服务状态

```powershell
→ docker compose ps
```

如果看到类似：

```text
→ student-manager-api-compose
→ 127.0.0.1:8000->8000/tcp
```

说明容器已经正常运行，并且本机端口已经映射到容器端口。

---

### 14.4 查看服务日志

```powershell
→ docker compose logs app
```

正常情况下可以看到类似：

```text
→ Student Manager API starting...
→ Uvicorn running on http://0.0.0.0:8000
```

这说明 FastAPI 服务已经在容器内启动成功。

---

### 14.5 验证环境变量

可以进入容器查看环境变量：

```powershell
→ docker compose exec app printenv LOG_LEVEL
→ docker compose exec app printenv STUDENT_DB_PATH
```

预期输出：

```text
→ INFO
→ data/students.db
```

也可以验证 Python 项目是否真正读取到了配置：

```powershell
→ docker compose exec app python -c "from config import settings; print(settings.log_level); print(settings.database_path)"
```

预期输出：

```text
→ INFO
→ data/students.db
```

---

### 14.6 验证 data 目录挂载

执行：

```powershell
→ docker compose exec app ls -l /app/data
```

如果能看到：

```text
→ students.db
```

说明本机 `data` 目录已经成功挂载到容器内部的 `/app/data`。

这意味着容器读写：

```text
→ /app/data/students.db
```

实际就是读写本机项目目录下的：

```text
→ data/students.db
```

---

### 14.7 停止并删除 Compose 服务

```powershell
→ docker compose down
```

该命令会停止并删除由 Docker Compose 创建的容器和默认网络。

注意：

```text
→ docker compose down 不会删除本机 data/students.db
```

因为数据库文件保存在本机 `data` 目录中，不只存在于容器内部。

---

### 14.8 Docker Compose 常用命令汇总

```powershell
→ docker compose config
→ docker compose up -d
→ docker compose ps
→ docker compose logs app
→ docker compose exec app printenv LOG_LEVEL
→ docker compose exec app printenv STUDENT_DB_PATH
→ docker compose exec app ls -l /app/data
→ docker compose down
```

完整运行流程：

```text
→ 编写 docker-compose.yml
→ docker compose config 检查配置
→ docker compose up -d 启动服务
→ docker compose ps 查看容器状态
→ docker compose logs app 查看日志
→ 浏览器访问 /docs
→ 验证接口
→ docker compose down 停止并清理容器
```

## 15. 当前项目阶段

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

## 16. 学习说明

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