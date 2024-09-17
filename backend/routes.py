from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models import Book, Borrow, User, BorrowRequest
from db import SessionLocal
from typing import List
import backend.schemas as schemas
from datetime import date, timedelta

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Add a New Book
@router.post("/admin/books/add/")
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        publisher=book.publisher,
        category=book.category,
        is_available=True,  # Books are available when added
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# 2. Remove a Book
@router.delete("/admin/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": f"Book with ID {book_id} removed from catalog"}

# 3. List all Users
@router.get("/admin/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 4. List Users and their Borrowed Books
@router.get("/admin/users/borrowed-books/", response_model=List[schemas.UserWithBorrowedBooks])
def list_users_with_borrowed_books(db: Session = Depends(get_db)):
    users = db.query(User).all()
    result = []
    for user in users:
        borrowed_books = db.query(Borrow).filter(Borrow.user_id == user.id).all()
        user_data = {
            "id": user.id,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
            "borrowed_books": [borrow.book_id for borrow in borrowed_books]
        }
        result.append(user_data)
    return result

# 5. List Unavailable Books (show when they will be available)
@router.get("/admin/books/unavailable/")
def unavailable_books(db: Session = Depends(get_db)):
    unavailable_books = db.query(Book).filter(Book.is_available == False).all()
    result = []
    for book in unavailable_books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "available_on": book.available_on  # Return when the book will be available
        })
    return result

# 6. Borrow a Book by User ID
@router.post("/admin/users/{user_id}/borrow-book/{book_id}")
def borrow_book(user_id: int, book_id: int, borrow_request: BorrowRequest, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or not book.is_available:
        raise HTTPException(status_code=404, detail="Book is unavailable")

    # Mark book as borrowed and set the return date
    book.is_available = False
    book.available_on = date.today() + timedelta(days=borrow_request.days)

    # Record the borrow transaction
    borrow = Borrow(user_id=user_id, book_id=book.id, borrow_date=date.today(), return_date=book.available_on)
    db.add(borrow)
    db.commit()

    return {"message": "Book borrowed successfully", "return_date": book.available_on}