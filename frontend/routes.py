from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from frontend.models import User, Book, Borrow
from db import SessionLocal
from pydantic import BaseModel
from datetime import date, timedelta
from typing import List, Optional  # Import List and Optional
import frontend.schemas as schemas

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request validation
class UserEnroll(BaseModel):
    firstname: str
    lastname: str
    email: str

class BorrowRequest(BaseModel):
    user_id: int
    days: int

# 1. Enroll User
@router.post("/users/enroll/")
def enroll_user(user: UserEnroll, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(firstname=user.firstname, lastname=user.lastname, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 2. List All Books
@router.get("/books/", response_model=List[schemas.Book])
def list_books(db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.is_available == True).all()
    return books

# 3. Get Single Book by ID
@router.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# 4. Filter Books
@router.get("/books/filter/", response_model=List[schemas.Book])
def filter_books(publisher: Optional[str] = None, category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Book).filter(Book.is_available == True)
    if publisher:
        query = query.filter(Book.publisher == publisher)
    if category:
        query = query.filter(Book.category == category)
    return query.all()

# 5. Borrow Book
@router.post("/books/borrow/{book_id}")
def borrow_book(book_id: int, borrow_request: BorrowRequest, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or not book.is_available:
        raise HTTPException(status_code=404, detail="Book is unavailable")

    # Mark book as borrowed and set the return date
    book.is_available = False
    book.available_on = date.today() + timedelta(days=borrow_request.days)

    # Record the borrow transaction
    borrow = Borrow(user_id=borrow_request.user_id, book_id=book.id, borrow_date=date.today(), return_date=book.available_on)
    db.add(borrow)
    db.commit()

    return {"message": "Book borrowed successfully", "return_date": book.available_on}
