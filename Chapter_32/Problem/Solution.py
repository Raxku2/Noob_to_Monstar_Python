from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from hashlib import sha256
from os import getenv

load_dotenv()
MONGO_URI = getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["auth_practice"]
coll = db["users"]

app = FastAPI(title="Auth Practice")

def hash_pw(pw: str) -> str:
    return sha256(pw.encode()).hexdigest()

@app.post("/signup")
def signup(email: str, password: str):
    if coll.find_one({"email": email}):
        return {"status": "error", "message": "Email already exists"}
    
    hashed = hash_pw(password)
    coll.insert_one({"email": email, "password": hashed})
    return {"status": "success", "message": "User registered"}

@app.post("/signin")
def signin(email: str, password: str):
    user = coll.find_one({"email": email})
    if not user:
        return {"status": "error", "message": "User not found"}
    
    if hash_pw(password) == user["password"]:
        return {"status": "success", "message": f"Welcome {email}!"}
    else:
        return {"status": "error", "message": "Invalid password"}

@app.get("/users")
def users():
    all_users = coll.find({}, {"_id": 0, "password": 0})
    return list(all_users)
