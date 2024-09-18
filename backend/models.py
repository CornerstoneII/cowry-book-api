from sqlalchemy import Column, String, Boolean, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)

class Book(Base):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    category = Column(String)
    is_available = Column(Boolean, default=True)
    available_on = Column(Date, nullable=True)

class Borrow(Base):
    __tablename__ = "borrows"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    borrow_date = Column(Date)
    return_date = Column(Date)

    user = relationship("User")
    book = relationship("Book")

# Define the Pydantic model for the borrow request
class BorrowRequest(BaseModel):
    days: int