from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from hashlib import sha256
from os import getenv

# Setup
load_dotenv()
MONGO_URI = getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["auth_demo"]
users = db["user_accounts"]

app = FastAPI(title="Auth API")

# Hash function
def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

# Register route
@app.post("/register")
def register(username: str, password: str):
    if users.find_one({"username": username}):
        return {"status": "error", "message": "Username already exists"}

    hashed_pw = hash_password(password)
    users.insert_one({"username": username, "password": hashed_pw})
    return {"status": "success", "message": "User registered successfully"}

# Login route
@app.post("/login")
def login(username: str, password: str):
    user = users.find_one({"username": username})
    if not user:
        return {"status": "error", "message": "User not found"}

    input_hash = hash_password(password)
    if input_hash == user["password"]:
        return {"status": "success", "message": f"Welcome, {username}!"}
    else:
        return {"status": "error", "message": "Invalid credentials"}
