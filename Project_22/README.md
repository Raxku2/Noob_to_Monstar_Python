# 📝 Project 22 – Blog API with FastAPI & MongoDB

A simple **REST API** to create and retrieve blog posts using **FastAPI** and **MongoDB**.  
This project is a beginner-friendly example showing how to use FastAPI with Pydantic models and MongoDB.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.117-green?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-darkgreen?logo=mongodb)
![Dotenv](https://img.shields.io/badge/Env-Variables-yellow?logo=dotenv)

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 🏠 Home Route | Health check for API status |
| ✍️ Create Blog | Add new blog post with title, body, and author |
| 📜 Read Blogs | Fetch all blogs from MongoDB |
| 📂 MongoDB Backend | Stores blogs in `blogDB.myblog` collection |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Project
```bash
git clone https://github.com/yourusername/blog-api-fastapi.git
cd blog-api-fastapi
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```bash
MONGO_URI=mongodb+srv://your_mongo_user:password@cluster-url/
```

### 5️⃣ Run the API

```bash
uvicorn main:app --reload
```

Visit: 👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🔹 API Endpoints

| Method | Route   | Description             |
| ------ | ------- | ----------------------- |
| `GET`  | `/`     | Check if API is running |
| `POST` | `/post` | Create a new blog post  |
| `GET`  | `/blog` | Retrieve all blog posts |

---

## 🧱 Example JSON Request

**POST** `/post`

```json
{
  "title": "My First Blog",
  "body": "This is a simple blog created with FastAPI.",
  "author": "Rakesh"
}
```

Response:

```json
{
  "status": "66bc8f...12",
  "message": "Data inserted"
}
```

---

## 🧾 Example Response for `/blog`

```json
{
  "status": "ok",
  "data": [
    {
      "title": "My First Blog",
      "body": "This is a simple blog created with FastAPI.",
      "author": "Rakesh"
    }
  ]
}
```

---

## 📄 requirements.txt

```
fastapi==0.117.1
uvicorn==0.37.0
pymongo==4.15.1
python-dotenv==1.0.1
pydantic==2.11.9
```

---

## 🧠 Concepts Practiced

* Using **Pydantic models** for request validation
* Connecting FastAPI to **MongoDB Atlas**
* Designing basic **REST API endpoints**
* Managing environment variables securely

---

## 🪄 Future Enhancements

* Add update & delete routes
* Add authentication for admin users
* Integrate front-end or mobile app
