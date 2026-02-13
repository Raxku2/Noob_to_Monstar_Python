# 📝 Project_49: Blogging Platform

### FastAPI + MongoDB + CLI + Deployment

**Author: Pinaka**

---

# 📌 Project Overview

This project is a complete **Backend Blogging Platform** built using:

* ⚡ FastAPI (Backend Framework)
* 🍃 MongoDB (Database)
* 🐍 Python
* 🌍 REST API Architecture
* 🖥 CLI Client Application
* 🚀 Deployment Ready Structure

You built a real backend service that:

* Creates blog posts
* Fetches blog posts
* Lists all blogs
* Deletes blog posts
* Connects through a CLI client

This is a full-stack backend system.

---

# 🏗 Project Architecture

```
CLI Client
    ↓
HTTP Requests (requests library)
    ↓
FastAPI Server
    ↓
MongoDB Database
```

---

# 📦 Core Features

## ✅ Create Blog

* Stores user name
* Blog title
* Blog description
* Date & time auto-generated
* MongoDB ObjectId generated

---

## ✅ Get Blog by ID

* Fetch blog using MongoDB ObjectId
* Converts ObjectId → string
* Handles invalid ID format

---

## ✅ Get All Blogs

* Sorted by latest first
* Returns total blog count
* Clean JSON response

---

## ✅ Delete Blog

* Deletes by ObjectId
* Validates ID format
* Returns proper response

---

## ✅ CLI Client Interface

* Menu-based navigation
* Create blog
* View by ID
* View all blogs
* Delete blog
* Terminal styled output

---

# 🗄 Database Structure

Each blog stored in MongoDB:

```json
{
  "_id": "ObjectId",
  "user_name": "Pinaka",
  "title": "My First Blog",
  "description": "This is a blogging platform built using FastAPI.",
  "date": "2026-02-12",
  "time": "18:45:22",
  "created_at": "2026-02-12T18:45:22"
}
```

---

# 🧠 What You Learn in This Project

---

## 1️⃣ FastAPI Backend Development

* Creating routes
* Using async endpoints
* Pydantic models
* Request body validation
* Path parameters
* JSON responses
* Error handling
* ObjectId handling

---

## 2️⃣ MongoDB Integration

* Connecting using environment variables
* insert_one()
* find_one()
* find()
* delete_one()
* Sorting data
* Working with datetime
* ObjectId conversion

---

## 3️⃣ REST API Design

You implemented:

| Method | Route             | Purpose         |
| ------ | ----------------- | --------------- |
| POST   | /create_blog      | Create blog     |
| GET    | /get_blog/{id}    | Get single blog |
| GET    | /get_all_blogs    | List all blogs  |
| DELETE | /delete_blog/{id} | Delete blog     |

This follows proper REST design principles.

---

## 4️⃣ CLI Client Communication

Using:

* `requests.post()`
* `requests.get()`
* `requests.delete()`

You built a terminal-based API consumer.

This simulates how:

* Frontend apps
* Mobile apps
* External services

Communicate with your backend.

---

# ⚙ Installation Guide

---

## 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv requests
```

---

## 2️⃣ Setup Environment Variables

Create `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 3️⃣ Run FastAPI Server

```bash
uvicorn api:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Interactive docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Run CLI Client

```bash
python client.py
```

---

# 🚀 Deployment Guide

You can deploy this API to:

* 🌐 Render
* 🌐 Railway
* 🌐 Fly.io
* 🌐 AWS EC2
* 🌐 DigitalOcean
* 🌐 Heroku alternatives

## Basic Production Command:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Set environment variable on server:

```
MONGO_URI=your_production_uri
```

---

# 🎯 Skills Gained

After this project you understand:

* Real backend development
* Production-ready API design
* Database integration
* REST architecture
* CRUD operations
* Backend deployment workflow
* Client-server communication
* API testing
* Data serialization

---


**Author: Pinaka**
