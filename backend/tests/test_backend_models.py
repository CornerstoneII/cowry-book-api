# from backend.models import Book
# from db import Base, engine
# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# def test_create_book():
#     new_book = Book(title="Unit Test Book", author="Test Author", publisher="Test Publisher", category="Testing", is_available=True)
#     session.add(new_book)
#     session.commit()

#     fetched_book = session.query(Book).filter(Book.title == "Unit Test Book").first()
#     assert fetched_book is not None
#     assert fetched_book.title == "Unit Test Book"
