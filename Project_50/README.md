# 🚀 Project_50: Task & Notes Manager

### A Complete Python Backend + CLI Course Project

**Author: Pinaka**

---

## 📌 Project Overview

This project is a complete **full-stack Python system** built using:

* 🐍 FastAPI (Backend API)
* 🍃 MongoDB (Database)
* 🖥 Rich (Beautiful CLI Interface)
* 🌐 Requests (API communication)

You will learn how to:

* Build a REST API
* Connect MongoDB with FastAPI
* Create a CLI frontend
* Perform CRUD operations
* Design structured data models
* Connect API and CLI together

This project simulates a real-world productivity application.

---

# 🏗 Project Architecture

```
MongoDB
   ↑
FastAPI Backend
   ↑
CLI Client (Rich UI)
```

---

# 📦 Features

## ✅ Backend (FastAPI + MongoDB)

* Create Task / Note
* View All Items
* Update Item
* Delete Single Item
* Delete All Items
* Automatic date & time tracking
* Priority system (LOW / MEDIUM / HIGH)
* Tags support
* Due date support

---

## ✅ CLI (Rich Based Interface)

* Animated welcome screen
* Beautiful colored menu
* Table-based task view
* Interactive prompts
* API communication using requests
* Full CRUD support from terminal

---

# 🗄 Database Schema

Each item stored in MongoDB looks like:

```json
{
  "title": "Complete Assignment",
  "description": "Finish math assignment",
  "type": "task",
  "status": "Pending",
  "priority": "HIGH",
  "tags": ["school", "math"],
  "due_date": "2026-02-15",
  "date": "2026-02-12",
  "time": "18:20:11",
  "day": "Thursday",
  "created_at": "now",
  "updated_at": "now"
}
```

---

# 🧠 What You Learn in This Project

## 1️⃣ FastAPI Concepts

* Route creation
* POST / GET / PUT / DELETE
* Request body validation using Pydantic
* Path parameters
* JSONResponse usage
* MongoDB integration
* Partial updates

---

## 2️⃣ MongoDB Concepts

* insert_one()
* find()
* update_one()
* delete_one()
* delete_many()
* ObjectId usage
* Data filtering

---

## 3️⃣ CLI Development with Rich

* Tables
* Panels
* Live animations
* Prompt input handling
* Colored text formatting
* Terminal UI design

---

## 4️⃣ API Communication

* requests.get()
* requests.post()
* requests.put()
* requests.delete()
* JSON payload handling
* Status code checking

---

# ⚙ Installation Guide

---

## 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv requests rich
```

---

## 2️⃣ Setup MongoDB

Create a MongoDB Atlas cluster
Get your connection string

Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 3️⃣ Run the Backend API

```bash
uvicorn main:app --reload --port 8001
```

Visit:

```
http://127.0.0.1:8001/docs
```

Swagger UI will appear.

---

## 4️⃣ Run the CLI Client

Open another terminal:

```bash
python client.py
```

---

# 📋 CLI Menu Options

```
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Delete All
0. Exit
```

---

# 🔄 API Endpoints Summary

| Method | Endpoint     | Description       |
| ------ | ------------ | ----------------- |
| GET    | /            | Health check      |
| POST   | /add         | Add new task/note |
| GET    | /all         | Get all items     |
| PUT    | /update/{id} | Update item       |
| DELETE | /delete/{id} | Delete item       |
| DELETE | /delete-all  | Delete everything |

---

# 🎯 Learning Objectives Achieved

By completing this project, you now understand:

* Backend architecture
* Database integration
* API design principles
* CLI frontend development
* Real-world CRUD systems
* Full application flow
* System structuring

---

**Author: Pinaka**
