from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
from fastapi import FastAPI

app = FastAPI()


load_dotenv()
from os import getenv

uri = getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri)


db = client["students"]
coll = db["all_students"]


def add_data(name: dict, roll: int, marks: int) -> str:
    """db te student data add kore"""
    res = coll.insert_one({"name": name, "roll": roll, "marks": marks})
    return str(res.inserted_id)


def show_data() -> list:
    """student data show kore"""
    res = coll.find({})
    return list(res)


def edit_data(id: str, name: str):
    res = coll.update_one({"_id": ObjectId(id)}, {"$set": {"name": name}})
    return res.modified_count


def delete_data(id: str):
    res = coll.delete_one({"_id": ObjectId(id)})
    return int(res.deleted_count)


@app.get("/")
def home():
    return "Hello!!"


@app.get("/show")
def show():
    alldata = show_data()
    res: list = []
    for data in alldata:
        data["_id"] = str(data["_id"])
        res.append(data)
    return {"data": res}


@app.post("/add")
def add(name: str, roll: int, marks: int):
    res = add_data(name=name, roll=roll, marks=marks)

    return {"status": res}


@app.post("/edit")
def edit(id: str, name: str):
    res = edit_data(id, name)
    return {"status": res}


@app.get("/remove")
def remove(id: str):
    res = delete_data(id)
    return {"status": res}
