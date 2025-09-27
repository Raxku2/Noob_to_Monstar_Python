from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
from fastapi import FastAPI
from os import getenv

load_dotenv()
uri = getenv("MONGO_URI")

client = MongoClient(uri)
db = client["libraryDB"]
books = db["books"]

app = FastAPI()

def add_book(title: str, author: str, year: int) -> str:
    res = books.insert_one({"title": title, "author": author, "year": year})
    return str(res.inserted_id)

def get_books() -> list:
    return list(books.find({}))

def edit_book(id: str, title: str) -> int:
    res = books.update_one({"_id": ObjectId(id)}, {"$set": {"title": title}})
    return res.modified_count

def remove_book(id: str) -> int:
    res = books.delete_one({"_id": ObjectId(id)})
    return res.deleted_count

@app.post("/addbook")
def add(title: str, author: str, year: int):
    return {"status": add_book(title, author, year)}

@app.get("/allbooks")
def show():
    data = get_books()
    for book in data:
        book["_id"] = str(book["_id"])
    return {"data": data}

@app.post("/editbook")
def edit(id: str, title: str):
    return {"status": edit_book(id, title)}

@app.get("/removebook")
def remove(id: str):
    return {"status": remove_book(id)}
