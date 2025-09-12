
from pymongo import MongoClient

# Connection string (replace with your MongoDB Atlas details)
uri = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"

# Connect to MongoDB
try:
    client = MongoClient(uri)
    db = client["testDB"]
    collection = db["students"]
    print("✅ Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
