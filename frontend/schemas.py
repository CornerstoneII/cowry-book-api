from pydantic import BaseModel
from typing import Optional
from datetime import date

# Pydantic model for creating a new user
class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str

    class Config:
        orm_mode = True  # This allows returning ORM models from the database directly

# Pydantic model for adding a new book
class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    category: str

# Pydantic model for retreiving any book
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    category: str
    is_available: bool
    available_on: Optional[date]

    class Config:
        orm_mode = True
