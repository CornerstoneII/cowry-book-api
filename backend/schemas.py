from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Pydantic model for creating a new book
class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    category: str

# Pydantic model for users with their borrowed books
class UserWithBorrowedBooks(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    borrowed_books: List[int]

# Pydantic model for retreiving book details
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
