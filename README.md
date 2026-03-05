# LevelUp - Personal Productivity API

LevelUp is a FastAPI-based personal productivity API that helps users manage daily tasks by organizing them into life categories such as Work, Health, or Hobby. It provides endpoints to create categories, manage tasks, filter tasks, and track completion status.

## Features
- Category Management: Create categories with a name and color code.
- Task Management: Create tasks with a title, description, completion status, and assign them to a category.
- Filtering: Retrieve tasks by category or by completion status.
- Completion Toggle: Quickly mark a task as completed.

## Project Structure
```
PRODUCTIVITY_API/
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── frontend/
│   └── index.html
├── env/
├── requirements.txt
└── run_steps.txt
```
## Tech Stack
Python, FastAPI, SQLAlchemy, Pydantic, SQLite, HTML

## Installation
1. Clone the repository
git clone https://github.com/sadman-sol/LevelUp.git   
cd levelup-productivity-api

2. Create a virtual environment
python -m venv env

Activate the environment  
Windows: env\Scripts\activate  
Linux/Mac: source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

## Run the API
uvicorn app.main:app --reload

API URL: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs

## Example Endpoints
POST /categories – Create category  
POST /tasks – Create task  
GET /tasks – Get all tasks  
GET /tasks?category_id=1 – Filter by category  
GET /tasks?completed=true – Filter by status  
PATCH /tasks/{task_id}/complete – Mark task completed
