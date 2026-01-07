from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
load_dotenv()
todoClient = MongoClient('')
db = todoClient['todoDB']
coll = db['jskdhaf']

class add(BaseModel):
    title: str
    state: str = 'Pending'
    time: str

class update(BaseModel):
    id: str
    title: str = ''
    state: str = ''
    time: str = ''

app = FastAPI()
@app.get('/')
def home():
    return JSONResponse({"status":'true', 'message':"Hello!!"})

# create todo
@app.post("/add") 
def add_todo(data: add):
    title = data.title
    time = data.time
    state = data.state

    status = coll.insert_one({"title":title,"status":state,'time':time})

    if status.inserted_id:
        return JSONResponse({"status":200,"message":'todo added'})

    return 0

# show todo
@app.get("/todo") 
def add_todo():
    dbdata = coll.find({})
    data = list(dbdata)

    if data:
        # Convert _id from ObjectId to string for each document
        for item in data:
            if '_id' in item:
                item['_id'] = str(item['_id'])
        
        return JSONResponse({"status": 200, "data": data})
    else:
        return JSONResponse({"status": 400, "message": "Data not found"})

# edit todo
@app.post("/update") 
def add_todo(data: update):
    id = data.id
    
    # Build update document based on available data
    title = data.title
    time = data.time
    state = data.state
    update_doc = {}
    
    if title and title != '':
        update_doc["title"] = title
    
    if time and time != '':
        update_doc["time"] = time
    
    if state and state != '':
        update_doc["status"] = state
    
    # Check if there's anything to update
    if not update_doc:
        return JSONResponse({"status": 400, "message": "No valid data provided for update"})
    
    # Perform the update
    status = coll.update_one(
        {"_id": ObjectId(id)},  # Convert to ObjectId if using MongoDB's default _id
        {"$set": update_doc}
    )
    
    if status.modified_count > 0:
        return JSONResponse({"status": 200, "message": "todo updated successfully"})
    elif status.matched_count > 0:
        return JSONResponse({"status": 200, "message": "todo found but no changes made"})
    else:
        return JSONResponse({"status": 404, "message": "todo not found"})
    
# delete todo
@app.post('/deltodo')
def delete_todo(data: update):
    try:
        id = data.id
        
        # For ObjectId
        result = coll.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count > 0:
            return JSONResponse({
                "status": 200, 
                "message": "Todo deleted successfully"
            })
        else:
            return JSONResponse({
                "status": 404, 
                "message": "Todo not found"
            })
            
    except Exception as e:
        return JSONResponse({
            "status": 500, 
            "message": f"Error deleting todo: {str(e)}"
        })

# delete all
@app.get('/delall')
def delall():
    status = coll.delete_many({})
    if status.deleted_count:
        return JSONResponse({"status": 200, "message": "Deleted"})

    return 0
