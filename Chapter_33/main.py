from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
db = client['db']
coll = db['nam']



@app.get("/")
def home():
    return {"status": "ok", "message": "hello"}


@app.get("/save/{name}")
def home(name):
    status = coll.insert_one({'name':name})
    print(status.inserted_id)
    return {"status": str(status.inserted_id), "message": f"hello {name}"}
