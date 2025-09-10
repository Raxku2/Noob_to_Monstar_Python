# 📘 Chapter\_23: MongoDB Atlas Setup

## 1️⃣ What is DBMS?

A **Database Management System (DBMS)** is software that allows users to **store, manage, and retrieve data** efficiently.

* Without DBMS → Data is stored in files, difficult to query, not secure.
* With DBMS → Data is structured, searchable, secure, and scalable.

---

## 2️⃣ Why Use DBMS?

✅ Organizes large amounts of data
✅ Allows **fast queries** and retrieval
✅ Supports **multi-user access**
✅ Ensures **data security & backup**
✅ Provides **scalability** for applications

---

## 3️⃣ Types of DBMS

* **Relational (SQL)** → MySQL, PostgreSQL
* **Non-Relational (NoSQL)** → MongoDB, Redis
* **Cloud Databases** → Firebase, MongoDB Atlas

---

## 4️⃣ MongoDB & Atlas

MongoDB is a **NoSQL database** where data is stored in **collections** (similar to tables) and **documents** (similar to rows).

MongoDB **Atlas** is a **cloud database service** that lets you use MongoDB without installing it locally.

---

## 5️⃣ Visual Diagram

```
+-------------------+         +-------------------+
|   Application     | <-----> |   MongoDB Atlas   |
|  (Python/JS/Java) |         |   Cloud Database  |
+-------------------+         +-------------------+
          |                             |
          |       Internet (Cloud)      |
          v                             v
  +-------------------+         +-------------------+
  |   Collections     |         |    Documents      |
  |  (like Tables)    |         |  (like JSON data) |
  +-------------------+         +-------------------+
```

---

## 6️⃣ Setup Guide for MongoDB Atlas

### 🔹 Step 1: Create Account

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas).
2. Sign up with **Google** or **Email**.

### 🔹 Step 2: Login

* After signing up, log in to the **Atlas Dashboard**.

### 🔹 Step 3: Create a Project

* Click **New Project** → Give it a name → Click **Create Project**.

### 🔹 Step 4: Deploy a Cluster

* Choose **Build a Cluster** → Select **Free Tier** (M0 Sandbox).
* Select **Cloud Provider** (AWS/Azure/GCP).
* Choose a **Region** (nearest to you).
* Click **Create Cluster**.

### 🔹 Step 5: Create a Database User

* Go to **Database Access** → Click **Add New Database User**.
* Set username & password.
* Choose **Read & Write to Any Database**.

### 🔹 Step 6: Whitelist Your IP

* Go to **Network Access** → Add your IP (0.0.0.0/0 for open access).

### 🔹 Step 7: Connect to Your Database

* Go to **Clusters** → Click **Connect**.
* Choose **Connect Your Application**.
* Copy the connection string (looks like 👇):

```
mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/test
```

* Replace `<username>` and `<password>` with your credentials.

---

## 7️⃣ Test Connection with Python

```python
from pymongo import MongoClient

# Replace with your connection string
uri = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"
client = MongoClient(uri)

db = client["testDB"]
collection = db["students"]

# Insert data
collection.insert_one({"name": "Rahul", "age": 21})

# Fetch data
for student in collection.find():
    print(student)
```

