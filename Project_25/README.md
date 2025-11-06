# 🔗 Project 25 – URL Shortener API (FastAPI + MongoDB)

A fully functional **URL Shortener** built with **FastAPI** and **MongoDB**.  
This API converts long URLs into short, shareable tokens and automatically redirects users when they visit the short link.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.117.1-brightgreen?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![Dotenv](https://img.shields.io/badge/Env-Variables-yellow?logo=dotenv)
![Redirect](https://img.shields.io/badge/Feature-URL_Redirects-orange?logo=link)

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 🧾 Shorten URLs | Converts long URLs into 10-character short tokens |
| 🔁 Redirect | Automatically redirects users to the original link |
| 🔐 Unique Tokens | Uses secure random generator from Python’s `secrets` |
| 💾 Database | Stores URL-token pairs in MongoDB |
| ⚡ Quick Docs | `/` route redirects directly to FastAPI Docs |

---

## 🧱 Project Structure
```

Project_25_URL_Shortener_API/
│
├── main.py
├── requirements.txt
└── .env

````

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/url-shortener-api.git
cd url-shortener-api
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variable

Create a `.env` file:

```
MONGO_URI=mongodb+srv://your_user:password@cluster-url/
```

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

Visit 👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🔹 API Endpoints

| Method | Route      | Description               |
| ------ | ---------- | ------------------------- |
| `GET`  | `/`        | Redirects to API Docs     |
| `POST` | `/short`   | Shorten a URL             |
| `GET`  | `/{token}` | Redirects to original URL |

---

## 🧩 Usage Examples

### ➕ Create Short URL

**POST** `/short`

```json
{
  "url": "https://www.python.org/downloads/release/python-3110/"
}
```

✅ Response:

```json
{
  "status": 200,
  "message": "recorded",
  "url": "http://localhost:8000/Zx9AB12kLm"
}
```

---

### 🔁 Redirect

Open your browser:

```
http://localhost:8000/Zx9AB12kLm
```

You’ll be redirected instantly to the original link.

---

## ⚙️ How It Works

```
┌───────────────┐
│  Long URL     │
└──────┬────────┘
       │
       ▼
[ FastAPI POST /short ]
       │
  Generates Random Token
       │
  Saves {token:url} in MongoDB
       │
       ▼
Returns short link → /{token}
       │
       ▼
[ GET /{token} → Redirects user ]
```

---

## 🧠 Concepts Practiced

* Working with `secrets` & `string` modules for random tokens
* Using MongoDB CRUD with PyMongo
* Redirecting with `RedirectResponse`
* Input validation using Pydantic
* Safe error handling and try-catch patterns

---

## 📄 requirements.txt

```
fastapi==0.117.1
uvicorn==0.37.0
pymongo==4.15.1
python-dotenv==1.1.1
pydantic==2.11.9
```

---

## 🪄 Future Enhancements

* Add analytics (click count, timestamp, IP)
* Add expiration date for short links
* Add custom aliases (user-defined tokens)
* Create web frontend to generate short links

---

## 👨‍💻 Credits

**Developed by:** [Pinaka](https://github.com/Raxku2)
**Course:** CodeShiksha – Python Bhasha Mastery
**Year:** © 2025
