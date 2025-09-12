from pymongo import MongoClient

# Replace with your MongoDB URI
URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"
client = MongoClient(URI)

db = client["libraryDB"]
books = db["books"]

# CREATE
book_list = [
    {"title": "Python 101", "author": "Guido", "year": 2020},
    {"title": "Learning MongoDB", "author": "Dwight", "year": 2021},
    {"title": "Data Science", "author": "Smith", "year": 2019}
]
books.insert_many(book_list)
print("✅ Inserted 3 books")

# READ
print("\n📖 All Books:")
for book in books.find():
    print(book)

# UPDATE
books.update_one({"title": "Python 101"}, {"$set": {"year": 2023}})
print("\n✏️ Updated Python 101 year → 2023")

# DELETE
books.delete_one({"title": "Data Science"})
print("\n🗑️ Deleted Data Science")
