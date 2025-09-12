# 📘 Chapter 24 – Connecting Python to MongoDB (PyMongo)

In this chapter, we will learn how to **connect Python applications to MongoDB Atlas** using the `pymongo` library.

---

## 🔹 What is PyMongo?
- PyMongo is the **official Python driver** for MongoDB.
- It allows you to connect to a MongoDB database, insert, update, delete, and query documents.

---

## 🔹 Install PyMongo
```bash
pip install pymongo
````

---

## 🔹 Connection Code Example

```python
from pymongo import MongoClient

# Replace with your MongoDB Atlas connection string
uri = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"

# Create a client
client = MongoClient(uri)

# Select a database
db = client["testDB"]

# Select a collection
collection = db["students"]

print("✅ Connected to MongoDB Atlas!")
```

---

## 🔹 Key Terms

* **Database** → like a container (e.g., `testDB`)
* **Collection** → like a table (e.g., `students`)
* **Document** → like a row (JSON format)

---

## 🧠 Summary

* Install `pymongo`
* Connect using MongoClient and MongoDB Atlas URI
* Choose database → choose collection

