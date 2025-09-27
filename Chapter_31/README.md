# ⚡ Chapter 31 – CRUD with FastAPI & MongoDB

In this chapter, we build a **Student Management API** using:
- **FastAPI** for REST API endpoints
- **MongoDB Atlas** for database storage
- **PyMongo** for database queries

---

## 🔹 CRUD Mapping
- **Create** → `POST /add`
- **Read** → `GET /show`
- **Update** → `POST /edit`
- **Delete** → `GET /remove`

---

## 🔹 API Endpoints

### 1. Show All Students
```http
GET /show
````

Response:

```json
{
  "data": [
    {"_id": "66abc123", "name": "Riya", "roll": 101, "marks": 85}
  ]
}
```

---

### 2. Add Student

```http
POST /add?name=Riya&roll=101&marks=85
```

Response:

```json
{"status": "66abc123"}
```

---

### 3. Edit Student

```http
POST /edit?id=66abc123&name=Riya Singh
```

Response:

```json
{"status": 1}
```

---

### 4. Delete Student

```http
GET /remove?id=66abc123
```

Response:

```json
{"status": 1}
```

---

## 🔹 Flow Diagram

```
Client ---> FastAPI Routes ---> PyMongo ---> MongoDB Atlas
```

---

## 🧠 Summary

* **FastAPI + MongoDB** is powerful for backend APIs
* CRUD maps to `POST/GET` endpoints
* ObjectId must be **converted to string** for JSON responses

