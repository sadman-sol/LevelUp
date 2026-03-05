from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    color: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    title: str
    description: str
    category_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True