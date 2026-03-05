from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LevelUp Productivity API")

# CORS middleware (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "LevelUp API running"}

# CATEGORY APIs

@app.post("/categories/")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@app.get("/categories/")
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

# TASK APIs

@app.post("/tasks/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get("/tasks/")
def read_tasks(
    category_id: int = None,
    completed: bool = None,
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db, category_id, completed)


@app.put("/tasks/{task_id}/toggle")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    return crud.toggle_task(db, task_id)