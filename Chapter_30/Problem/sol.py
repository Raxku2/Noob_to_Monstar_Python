
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_books = ["1984", "Python 101"]

@app.get("/books")
def get_books():
    return {"data": fake_books}

@app.post("/addbook/{title}")
def add_book(title: str):
    fake_books.append(title)
    return {"status": "Book added successfully"}

@app.get("/searchbook")
def search_book(title: str):
    if title in fake_books:
        return {"found": True, "title": title}
    return {"found": False}

class Book(BaseModel):
    title: str
    author: str

@app.post("/addbookjson")
def add_book_json(book: Book):
    fake_books.append(book.title)
    return {"status": "Book added successfully", "book": book.dict()}
