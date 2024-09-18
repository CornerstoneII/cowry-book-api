# from fastapi.testclient import TestClient
# from frontend.main import app

# client = TestClient(app)

# # Test to check if the API is running
# def test_get_books():
#     response = client.get("/books/")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# # Test to retrieve a book by ID (GET /books/{book_id})
# def test_get_book_by_id():
#     response = client.get("/books/1")
#     assert response.status_code == 200
#     book = response.json()
#     assert "title" in book
#     assert book["id"] == 1

# # Test to search books by filter (GET /books/filter/?category=technology)
# def test_search_books_by_title():
#     response = client.get("/books/filter/?category=Test%20Book")
#     assert response.status_code == 200
#     books = response.json()
#     assert isinstance(books, list)
#     for book in books:
#         assert "Test Book" in book["title"]

# # Test for a non-existing book (GET /books/{book_id})
# def test_get_non_existing_book():
#     response = client.get("/books/9999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Book not found"

