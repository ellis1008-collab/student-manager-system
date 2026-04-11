```markdown
# Student Information Management System

This is a student information management system project built with Python and FastAPI.

The project still keeps the earlier command-line version, while the current main development path is gradually moving toward an API version based on FastAPI and SQLite.

## Features

- Add a student
- View all students
- Query a student by student ID
- Update student information
- Delete student information

## Current Project Status

- Completed the command-line version
- Completed the basic FastAPI backend version
- Integrated SQLite database support
- Completed the database-based CRUD workflow
- Implemented a unified error response structure
- Supports visual database inspection with DB Browser for SQLite

## Project Structure

### 1. Command-Line Version Files

- `main.py`: entry point for the command-line program
- `manager.py`: student management logic
- `storage.py`: JSON file read/write logic
- `data/students.json`: data file for the command-line version

### 2. FastAPI + SQLite Version Files

- `api.py`: FastAPI application entry point
- `service.py`: service layer for business logic
- `db_storage.py`: database storage layer for SQLite operations
- `db_init.py`: database initialization script
- `data/students.db`: SQLite database file

## How to Run

### 1. Run the Command-Line Version

Run the following command in the project directory:

```bash
python main.py