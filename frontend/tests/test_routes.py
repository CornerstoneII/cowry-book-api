import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from frontend.main import app  # or backend.main if testing admin routes

client = TestClient(app)

# Test to check if the API is running
def test_read_main():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test to check adding a new book (Admin route)
def test_add_book():
    response = client.post(
        "/admin/books/add/",
        json={"title": "Test Book", "author": "Test Author", "publisher": "Test Publisher", "category": "Test Category"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
