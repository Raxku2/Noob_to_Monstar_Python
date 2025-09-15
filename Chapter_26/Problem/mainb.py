from pymongo import MongoClient

URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"
client = MongoClient(URI)

db = client["salesDB"]
orders = db["orders"]

# Insert data
orders.insert_many([
    {"customer": "Alice", "amount": 500, "city": "Kolkata"},
    {"customer": "Bob", "amount": 1200, "city": "Delhi"},
    {"customer": "Charlie", "amount": 700, "city": "Kolkata"},
    {"customer": "David", "amount": 900, "city": "Mumbai"},
    {"customer": "Eva", "amount": 1500, "city": "Delhi"},
])
print("✅ Inserted 5 orders")

# Create Index
orders.create_index("city")
print("✅ Index created on city")

# Query orders with amount > 800
print("\n📖 Orders with amount > 800:")
for order in orders.find({"amount": {"$gt": 800}}):
    print(order)

# Aggregation - total sales per city
print("\n📊 Total Sales Per City:")
pipeline = [
    {"$group": {"_id": "$city", "total_sales": {"$sum": "$amount"}}},
    {"$sort": {"total_sales": -1}}
]
for result in orders.aggregate(pipeline):
    print(result)
