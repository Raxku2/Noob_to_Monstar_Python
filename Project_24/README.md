# ✅ Project 24 – Task Manager API (FastAPI + MongoDB)

A simple and powerful **Task Management REST API** built using **FastAPI** and **MongoDB**.  
This API supports **Create, Read, Update, and Delete** operations for managing to-do tasks.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.117.1-brightgreen?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![Dotenv](https://img.shields.io/badge/Env-Variables-yellow?logo=dotenv)

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| ➕ Add Task | Create new to-do with title, time, and state |
| 📜 View Tasks | Retrieve all to-dos |
| ✏️ Update Task | Edit title, time, or state |
| ❌ Delete Task | Remove a single to-do |
| 🧹 Delete All | Wipe all tasks from the database |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv pydantic
```

### 4️⃣ Configure MongoDB Connection

In your `.env` file (or inline URI in code):

```bash
MONGO_URI = mongodb+srv://<user>:<password>@cluster-url/
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Access the API documentation at:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🔹 API Endpoints

| Method | Route      | Description              |
| ------ | ---------- | ------------------------ |
| `GET`  | `/`        | API health check         |
| `POST` | `/add`     | Add a new to-do          |
| `GET`  | `/todo`    | Show all to-dos          |
| `POST` | `/update`  | Update an existing to-do |
| `POST` | `/deltodo` | Delete one to-do by ID   |
| `GET`  | `/delall`  | Delete all to-dos        |

---

## 🧩 Request & Response Examples

### ➕ Add a Task

**POST** `/add`

```json
{
  "title": "Learn FastAPI",
  "state": "Pending",
  "time": "10:00 AM"
}
```

✅ Response

```json
{"status": 200, "message": "todo added"}
```

---

### 📜 Get All Tasks

**GET** `/todo`

```json
{
  "status": 200,
  "data": [
    {"_id": "66b0...9f", "title": "Learn FastAPI", "status": "Pending", "time": "10:00 AM"}
  ]
}
```

---

### ✏️ Update Task

**POST** `/update`

```json
{
  "id": "66b0c12345f...",
  "title": "Learn FastAPI Deep Dive",
  "state": "Done",
  "time": "11:00 AM"
}
```

✅ Response

```json
{"status": 200, "message": "todo updated successfully"}
```

---

### ❌ Delete Task

**POST** `/deltodo`

```json
{"id": "66b0c12345f..."}
```

✅ Response

```json
{"status": 200, "message": "Todo deleted successfully"}
```

---

### 🧹 Delete All Tasks

**GET** `/delall`
✅ Response

```json
{"status": 200, "message": "Deleted"}
```

---

## 🧠 Concepts Practiced

* CRUD operations in FastAPI
* MongoDB ObjectId handling with `bson`
* Environment variable usage
* Pydantic data validation
* JSONResponse formatting

---

## 🧩 requirements.txt

```
fastapi==0.117.1
uvicorn==0.37.0
pymongo==4.15.1
pydantic==2.11.9
python-dotenv==1.1.1
bson==0.5.10
```

---

## 🪄 Future Enhancements

* User-based task ownership (Auth integration)
* Add “due date” and “priority” fields
* Add sorting & filtering endpoints
* Web frontend for viewing tasks

---

## 👨‍💻 Credits

**Developed by:** YantraYodha
**Series:** CodeShiksha – Python Bhasha Mastery
**Year:** © 2025

```

