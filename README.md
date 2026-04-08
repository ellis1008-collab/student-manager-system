# 学生信息管理系统

这是一个基于 Python 和 FastAPI 实现的学生信息管理系统项目。

## 项目功能
- 添加学生
- 查看所有学生
- 按学号查询学生
- 修改学生信息
- 删除学生信息

## 当前项目状态
- 已完成命令行版本
- 已完成 FastAPI 基础后端化
- 当前数据层主要基于 JSON 文件存储
- 已完成项目首次上传到 GitHub

## 技术栈
- Python
- FastAPI
- Git
- GitHub
- JSON

## 项目结构
- `api.py`：接口入口模块文件
- `main.py`：程序入口文件
- `cli.py`：命令行交互模块文件
- `student.py`：学生数据模型模块文件
- `manager.py`：学生管理模块文件
- `service.py`：服务层模块文件
- `storage.py`：数据读写模块文件
- `data/`：数据文件目录

## 运行方式
1. 安装依赖
2. 进入项目目录
3. 运行：
   `uvicorn api:app --reload`
4. 打开浏览器访问：
   `http://127.0.0.1:8000/docs`

## 当前已实现接口
- `GET /students`
- `GET /students/{student_id}`
- `POST /students`
- `PUT /students/{student_id}`
- `DELETE /students/{student_id}`

## 后续计划
- 统一错误响应格式
- 将数据层从 JSON 升级到 SQLite
- 引入测试体系
- 继续推进更正规的 FastAPI 工程结构
