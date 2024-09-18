# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from backend.admin import app
# from db import Base, get_db


# # SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # In-memory SQLite for testing
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Override the get_db dependency for testing
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)

# @pytest.fixture(scope="module")
# def setup_db():
#     Base.metadata.create_all(bind=engine)  # Create the tables
#     yield
#     Base.metadata.drop_all(bind=engine)  # Drop the tables after the test is complete

# def test_add_book(setup_db):
#     response = client.post(
#         "/admin/books/add/",
#         json={"title": "Test Book", "author": "Author Name", "publisher": "Publisher", "category": "Fiction"}
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "Test Book"

# def test_remove_book(setup_db):
#     response = client.delete("/admin/books/1")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Book with ID 1 removed from catalog"

# # Test to check adding a new book (Admin route)
# def test_add_book():
#     response = client.post(
#         "/admin/books/add/",
#         json={"title": "Test Book", "author": "Test Author", "publisher": "Test Publisher", "category": "Test Category"}
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "Test Book"
