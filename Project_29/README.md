# 📝 Project_29: Markdown Note-Taker

> **Author:** Pinaka
> **Type:** Full-Stack Project
> **Backend:** FastAPI + MongoDB
> **Frontend:** Preact + Markdown
> **Purpose:** Learning Markdown, APIs, Databases, Frontend-Backend Integration

---

## 🚀 Project Overview

**Markdown Note-Taker** is a simple full-stack application where:

* Users write notes in **Markdown**
* Notes are **previewed live**
* Notes are **saved in MongoDB**
* Notes can be **listed and reopened**

This project demonstrates how real-world note apps work internally.

---

## 🧠 Architecture

```
Frontend (Preact)
   ↓  HTTP (Fetch API)
Backend (FastAPI)
   ↓
MongoDB (Notes Storage)
```

---

## 📁 Project Structure

```
Project_29/
│
├── backend/
│   └── main.py
│
└── frontend/
    ├── App.jsx
    └── components/
        ├── Editor.jsx
        └── Menu.jsx
```

---

## ⚙️ Backend Setup (FastAPI)

### 🔹 Requirements

* Python **3.8+**
* MongoDB (Local or Atlas)

### 🔹 Install Dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

---

### 🔹 Environment Variable (`.env`)

Create a `.env` file in backend folder:

```env
MONGO_URI=mongodb://localhost:27017
```

(or MongoDB Atlas URI)

---

### 🔹 Run Backend Server

```bash
uvicorn main:app --reload --port 8001
```

---

### 🔹 Backend Endpoints

| Method | Endpoint         | Purpose               |
| ------ | ---------------- | --------------------- |
| GET    | `/`              | Redirect to Swagger   |
| GET    | `/health`        | API + DB health check |
| POST   | `/doc`           | Create new document   |
| GET    | `/doc?doc_id=ID` | Fetch document        |
| GET    | `/documents`     | List all documents    |

---

### 🔹 Example Document in MongoDB

```json
{
  "_id": "ObjectId",
  "title": "My Note",
  "doc": "# Hello Markdown"
}
```

---

## 🎨 Frontend Setup (Preact)

### 🔹 Requirements

* Node.js **18+**
* Internet (for CDN `marked`)

---

### 🔹 Markdown Renderer Used

```js
marked.parse(text)
```

This converts Markdown → HTML live.

---

### 🔹 Start Frontend

If using Vite / Preact dev server:

```bash
npm install
npm run dev
```

Frontend runs usually at:

```
http://localhost:5173
```

---

## ✍️ Editor Page (`/editor`)

### Features:

* Markdown textarea (left)
* Live preview (right)
* Save document to MongoDB
* Open document using ID

---

## 📚 Menu Page (`/menu`)

### Features:

* List all saved documents
* Shows:

  * Document title
  * Document ID (used to open)

---

## 🔁 How Data Flows

### Create Document

```
Frontend → POST /doc → MongoDB
```

### Open Document

```
Frontend → GET /doc?doc_id=xxx → MongoDB → Editor
```

### List Documents

```
Frontend → GET /documents → MongoDB
```

---

## 🧪 Example Workflow

1. Open `/editor`
2. Write Markdown:

   ```md
   # My First Note
   **Bold text**
   ```
3. Click **Save**
4. Go to **Menu**
5. Copy document ID
6. Open again in Editor


---

## 🏁 Conclusion

This project is a **perfect beginner full-stack project** combining:

* 🐍 Python backend
* 🌐 JavaScript frontend
* 🗄️ Database storage
* ✍️ Markdown editing

Ideal for **college labs, offline classes, and portfolio building**.

---
