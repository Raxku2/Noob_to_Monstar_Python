# 🗒️ Project 26 – Notes App API (FastAPI + MongoDB)

A simple yet powerful **Notes Management API** built with **FastAPI** and **MongoDB**.  
You can **create**, **read**, **update**, and **delete** notes easily through API endpoints.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.117.1-brightgreen?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![Pydantic](https://img.shields.io/badge/Data_Validation-Pydantic-blue?logo=pydantic)
![CRUD](https://img.shields.io/badge/Feature-CRUD_Operations-orange?logo=fastapi)

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 📝 Add Notes | Create and store notes in MongoDB |
| 📜 View Notes | Retrieve all stored notes |
| ✏️ Update Notes | Modify title and content of existing notes |
| 🗑️ Delete Notes | Remove a specific note by ID |
| ⚡ Auto Docs | FastAPI auto-generates Swagger Docs |

---

## 🧱 Project Structure
```

Project_26_Notes_App/
│
├── main.py
├── requirements.txt
└── .env

````

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/notes-app-api.git
cd notes-app-api
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file:

```
MONGO_URI=mongodb+srv://your_user:password@cluster-url/
```

### 5️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Visit 👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** to explore Swagger UI.

---

## 🔹 API Endpoints

| Method   | Endpoint  | Description    |
| -------- | --------- | -------------- |
| `POST`   | `/add`    | Add a new note |
| `GET`    | `/view`   | View all notes |
| `POST`   | `/update` | Update a note  |
| `DELETE` | `/del`    | Delete a note  |

---

## 🧩 Example Usage

### ➕ Add Note

**POST** `/add`

```json
{
  "title": "Meeting Notes",
  "content": "Discussed project milestones and next steps."
}
```

✅ Response:

```json
{
  "status": 200,
  "message": "Note added with ID: 670c3b9c8b1aee..."
}
```

---

### 📜 View Notes

**GET** `/view`
✅ Response:

```json
{
  "status": 200,
  "message": "notes found",
  "data": [
    {
      "_id": "670c3b9c8b1aee...",
      "title": "Meeting Notes",
      "content": "Discussed project milestones and next steps."
    }
  ]
}
```

---

### ✏️ Update Note

**POST** `/update`

```json
{
  "note_id": "670c3b9c8b1aee...",
  "new_title": "Updated Meeting Notes",
  "new_content": "Added next sprint goals."
}
```

✅ Response:

```json
{
  "status": 200,
  "message": "Modified count: 1"
}
```

---

### 🗑️ Delete Note

**DELETE** `/del`

```json
{
  "note_id": "670c3b9c8b1aee..."
}
```

✅ Response:

```json
{
  "status": 200,
  "message": "Deleted count: 1"
}
```

---

## ⚙️ requirements.txt

```
fastapi==0.117.1
uvicorn==0.37.0
pymongo==4.15.1
python-dotenv==1.1.1
pydantic==2.11.9
bson==0.5.10
```

---

## 🧠 Concepts Practiced

* CRUD operations using **PyMongo**
* Converting `ObjectId` to string for JSON serialization
* Structuring RESTful API routes
* Using Pydantic models for input validation
* Managing MongoDB database connections

---

## 🪄 Future Enhancements

* Add **user authentication** (login-based notes)
* Implement **search** and **filtering** for notes
* Add **timestamps** for created/updated notes
* Build a simple **React or HTML frontend**

---

## 👨‍💻 Author

**YantraYodha**
🎓 *A project from CodeShiksha Python Mastery Course (2025)*
🚀 Empowering students to build real-world apps with Python.


