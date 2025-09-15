
from pymongo import MongoClient

# Replace with your MongoDB URI
URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"
client = MongoClient(URI)

db = client["schoolDB"]
students = db["students"]

# Insert sample data
sample_data = [
    {"name": "Amit", "age": 22, "city": "Kolkata"},
    {"name": "Riya", "age": 19, "city": "Delhi"},
    {"name": "Arjun", "age": 24, "city": "Kolkata"},
    {"name": "Sneha", "age": 21, "city": "Mumbai"},
]
students.insert_many(sample_data)

# Create Index
students.create_index("city")
print("✅ Index created on city field")

# Query Example
print("\n📖 Students older than 20:")
for s in students.find({"age": {"$gt": 20}}):
    print(s)

# Aggregation Example
print("\n📊 Students grouped by city:")
pipeline = [
    {"$group": {"_id": "$city", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}}
]
for result in students.aggregate(pipeline):
    print(result)
