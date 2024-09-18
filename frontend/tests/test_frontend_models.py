import pytest
from frontend.models import Book
from db import SessionLocal

# Fixture to set up and tear down the database session
@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Test to create a book instance
def test_create_book(db_session):
    book = Book(title="Test Book", author="Test Author", publisher="Test Publisher", category="Test Category", is_available=True)
    db_session.add(book)
    db_session.commit()
    assert book.id is not None

# Test to query books by category
def test_query_books_by_category(db_session):
    books = db_session.query(Book).filter(Book.category == "Test Category").all()
    assert len(books) > 0

# Test to update a book record
def test_update_book(db_session):
    book = db_session.query(Book).filter(Book.id == 1).first()
    book.title = "Updated Title"
    db_session.commit()
    updated_book = db_session.query(Book).filter(Book.id == 1).first()
    assert updated_book.title == "Updated Title"

# Test to delete a book record
def test_delete_book(db_session):
    book = db_session.query(Book).filter(Book.id == 1).first()
    db_session.delete(book)
    db_session.commit()
    deleted_book = db_session.query(Book).filter(Book.id == 1).first()
    assert deleted_book is None
