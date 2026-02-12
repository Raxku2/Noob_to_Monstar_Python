from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from datetime import datetime
import os

load_dotenv()

client = MongoClient("")
db = client["todoDB"]
collection = db["todos"]

app = FastAPI(title="Task & Note Manager API")


class TodoCreate(BaseModel):
    title: str
    description: str
    type: str
    priority: str
    tags: list = []
    due_date: str | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    tags: list[str] | None = None
    due_date: str | None = None


# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"status": True, "message": "Task & Note API Running 🚀"}


# CREATE
@app.post("/add")
def add_item(data: TodoCreate):
    now = datetime.now()
    todo = {
        "title": data.title,
        "description": data.description,
        "type": data.type,
        "status": "Pending",
        "priority": data.priority,
        "tags": data.tags,
        "due_date": data.due_date,
        "date": str(now.strftime("%Y-%m-%d")),
        "time": str(now.strftime("%H:%M:%S")),
        "day": str(now.strftime("%A")),
        "created_at": "now",
        "updated_at": "now",
    }

    result = collection.insert_one(todo)
    return JSONResponse(
        {
            "status": 200,
            "message": "Item added Sucessfully",
            "id": str(result.inserted_id),
        }
    )


# READ ALL
@app.get("/all")
def get_all():
    items = []
    for item in collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)

    if not items:
        return JSONResponse({"status": 404, "message": "No data found"})

    print(items)

    return JSONResponse({"status": 200, "data": items})


# UPDATE
@app.put("/update/{item_id}")
def update_item(item_id: str, data: TodoUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    update_data["updated_at"] = str(datetime.now())

    result = collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": update_data},
    )

    if result.matched_count == 0:
        return JSONResponse({"status": 404, "message": "Item not found"})

    return JSONResponse({"status": 200, "message": "Item updated successfully"})


# DELETE  ONLY ONE
@app.delete("/delete/{item_id}")
def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})

    if result.deleted_count == 0:
        return JSONResponse({"status": 404, "message": "Item not found"})

    return JSONResponse({"status": 200, "message": "Item deleted"})


# DELETE ALL DATA
@app.delete("/delete-all")
def delete_all():
    collection.delete_many({})
    return JSONResponse({"status": 200, "message": "All items deleted"})
