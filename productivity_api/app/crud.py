from sqlalchemy.orm import Session
from . import models, schemas


# CATEGORY
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session):
    return db.query(models.Category).all()


# TASK
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, category_id=None, completed=None):
    query = db.query(models.Task)

    if category_id:
        query = query.filter(models.Task.category_id == category_id)

    if completed is not None:
        query = query.filter(models.Task.completed == completed)

    return query.all()


def toggle_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    task.completed = not task.completed
    db.commit()
    db.refresh(task)
    return task