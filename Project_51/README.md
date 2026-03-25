# 📄 Project_51: Portfolio & Resume Manager API

### Build Your Own Developer Portfolio Backend

**Author: Pinaka**

---

# 📌 Project Overview

This project is a **complete Portfolio & Resume Management API** built using:

* ⚡ FastAPI (Backend Framework)
* 🍃 MongoDB (Database)
* 🐍 Python
* 🌐 REST API Architecture

It allows you to create and manage:

* Skills
* Projects
* User Profile
* Education
* Experience

This is essentially a **backend for your personal portfolio website or resume system**.

---

# 🏗 Project Architecture

```
Client (CLI / Web / Mobile)
        ↓
FastAPI Backend
        ↓
MongoDB Database
        ↓
Structured Resume Data
```

---

# ✨ Core Modules

---

# 🧠 1. Skills Module

Manage all your skills like:

* Python
* IoT
* Web Development
* Machine Learning

## 📌 Endpoints

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| POST   | /skills/           | Add Skill          |
| PUT    | /skills/           | Edit Skill         |
| DELETE | /skills/           | Delete Skill       |
| GET    | /skills/           | Get All Skills     |
| GET    | /skills/catagories | Skills by Category |

---

## 📦 Example Skill Object

```json
{
  "name": "Python",
  "category": "Programming",
  "level": "Advanced"
}
```

---

# 🧠 2. Projects Module

Store your portfolio projects.

## 📌 Endpoints

| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| POST   | /projects/           | Create Project       |
| PUT    | /projects/           | Edit Project         |
| DELETE | /projects/           | Delete Project       |
| GET    | /projects/           | Get All Projects     |
| GET    | /projects/catagories | Projects by Category |

---

## 📦 Example Project Object

```json
{
  "title": "IoT Weather Station",
  "description": "ESP8266 based weather tracker",
  "tech_stack": ["Python", "MicroPython", "Firebase"],
  "category": "IoT"
}
```

---

# 👤 3. User Info Module

Your core profile data.

## 📌 Endpoints

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | /user/{user_id} | Get User Info    |
| POST   | /user/{user_id} | Create User Info |
| PUT    | /user/{user_id} | Update User Info |
| DELETE | /user/{user_id} | Delete User      |

---

## 📦 Example User Object

```json
{
  "name": "Pinaka",
  "email": "example@email.com",
  "bio": "Developer & Educator",
  "location": "India"
}
```

---

# 🎓 4. Education Module

Track academic details.

## 📌 Endpoints

| Method | Endpoint                           | Description      |
| ------ | ---------------------------------- | ---------------- |
| GET    | /user/education/{user_id}          | Get Education    |
| POST   | /user/education/{user_id}          | Add Education    |
| PUT    | /user/education/{user_id}/{edu_id} | Update Education |
| DELETE | /user/education/{user_id}/{edu_id} | Delete Education |

---

## 📦 Example Education Object

```json
{
  "degree": "B.Tech",
  "field": "Electronics",
  "institution": "Abacus Institute",
  "year": "2026"
}
```

---

# 💼 5. Experience Module

Professional or internship experience.

## 📌 Endpoints

| Method | Endpoint                            | Description       |
| ------ | ----------------------------------- | ----------------- |
| GET    | /user/experience/{user_id}          | Get Experience    |
| POST   | /user/experience/{user_id}          | Add Experience    |
| PUT    | /user/experience/{user_id}/{exp_id} | Update Experience |
| DELETE | /user/experience/{user_id}/{exp_id} | Delete Experience |

---

## 📦 Example Experience Object

```json
{
  "company": "Startup XYZ",
  "role": "Backend Developer",
  "duration": "6 months",
  "description": "Built APIs using FastAPI"
}
```

---

# 🧠 What You Learn

---

## 1️⃣ API Design at Scale

* Multiple modules
* Organized endpoints
* Resource-based routing

---

## 2️⃣ Database Structuring

* Relationships between:

  * User → Education
  * User → Experience
  * User → Skills
  * User → Projects

---

## 3️⃣ CRUD Operations

You implemented full CRUD for:

* Skills
* Projects
* User Data
* Education
* Experience

---

## 4️⃣ RESTful Thinking

You structured APIs like real-world systems:

* `/user/{id}`
* `/projects/`
* `/skills/`

---

## 5️⃣ Backend for Real Product

This API can directly power:

* Portfolio website
* Resume builder
* Developer profile system
* Freelance profile platform

---

# ⚙ Installation Guide

---

## 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

---

## 2️⃣ Setup Environment Variables

Create `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 3️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

## 4️⃣ Access API Docs

```
http://127.0.0.1:8000/docs
```

---

# 🚀 Real-World Use Cases

You can use this API to build:

* 🌐 Personal Portfolio Website
* 📄 Resume Generator
* 💼 Job Profile Dashboard
* 🧑‍💻 Developer Portfolio SaaS
* 🎓 Student Profile System

---

# 🔥 Advanced Improvements

Take it further:

---

## 🔐 Authentication

* JWT login system
* User accounts

---

## 📄 Resume Export

* Generate PDF resumes
* Download feature

---

## 🌐 Frontend Integration

* React / Next.js frontend
* Portfolio website UI

---

## 🔎 Search & Filters

* Search skills/projects
* Filter by category

---

## 📊 Analytics

* Track profile views
* Project popularity

---

## ☁ Deployment

* Deploy on cloud (Render / AWS)
* Connect custom domain


---

**Author: Pinaka**
