from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from bson import ObjectId


class addData(BaseModel):
    title : str
    content : str


class updateData(BaseModel):
    note_id : str
    new_title : str
    new_content : str

class delData(BaseModel):
    note_id :str 

# 1. Connect to MongoDB
client = MongoClient("URI")  # Change if using Atlas
db = client["NotesDB"]  # Database name
notes_collection = db["Notes"]  # Collection name


app = FastAPI()


@app.get('/')
def homme():
    return RedirectResponse('/docs')



# 2. Functions for CRUD operations

@app.post("/add")
def add_note(data : addData):
    title = data.title
    content = data.content
    note = {"title": title, "content": content}
    result = notes_collection.insert_one(note)
    mesage = (f"Note added with ID: {result.inserted_id}")
    return JSONResponse({'status':200,'message':mesage})



@app.get('/view')
def view_notes():
    dbres = notes_collection.find({})
    notes = []

    for note in dbres:
        note['_id'] = str(note['_id'])
        notes.append(note)

    return JSONResponse({'status':200,'message':'notes found','data':notes})
    

@app.post('/update')
def update_note(data : updateData):
    note_id = data.note_id
    new_title = data.new_title
    new_content = data.new_content

    result = notes_collection.update_one({"_id": ObjectId(note_id)}, {"$set": {"title": new_title, "content": new_content}}
    )
    mesage = (f"Modified count: {result.modified_count}")
    return JSONResponse({'status':200,'message':mesage})


@app.delete('/del')
def delete_note(data: delData):
    note_id = data.note_id
    result = notes_collection.delete_one({"_id": ObjectId(note_id)})
    mesage = (f"Deleted count: {result.deleted_count}")
    return JSONResponse({'status':200,'message':mesage})

