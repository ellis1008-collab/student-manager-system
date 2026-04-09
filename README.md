Student Information Management System

This is a student information management system project built with Python and FastAPI.

Features

Add student records

View all student records

Query a student by student ID

Update student information

Delete student information


Current Project Status

The command-line version has been completed

The basic FastAPI backend version has been completed

The current data layer is mainly based on JSON file storage

The project has been uploaded to GitHub for the first time


Tech Stack

Python

FastAPI

Git

GitHub

JSON


Project Structure

api.py: API entry module

main.py: Program entry file

cli.py: Command-line interaction module

student.py: Student data model module

manager.py: Student management module

service.py: Service layer module

storage.py: Data read/write module

data/: Data file directory


How to Run

1. Install the dependencies


2. Enter the project directory


3. Run:

uvicorn api:app --reload


4. Open the browser and visit:

http://127.0.0.1:8000/docs



Implemented API Endpoints

GET /students

GET /students/{student_id}

POST /students

PUT /students/{student_id}

DELETE /students/{student_id}


Future Plans

Standardize the error response format

Upgrade the data layer from JSON to SQLite

Introduce a testing system

Continue improving the project into a more standardized FastAPI architecture

The system has completed its first GitHub remote hosting setup
