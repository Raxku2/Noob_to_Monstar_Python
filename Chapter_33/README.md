## 📘 Chapter_33 — MongoDB + FastAPI Integration

This chapter demonstrates how to connect **FastAPI** with **MongoDB** using **PyMongo** — enabling a simple web API that stores and retrieves data.

---

### 🧠 **Concept Overview**

* **FastAPI** → lightweight, high-performance web framework.
* **MongoDB** → NoSQL database for flexible data storage.
* **PyMongo** → official MongoDB driver for Python.

---

### ⚙️ **Setup**

#### 1️⃣ Install Required Packages

```bash
pip install fastapi pymongo uvicorn
```

#### 2️⃣ Start MongoDB

* **Local MongoDB:**
  Make sure your local MongoDB server is running at `mongodb://localhost:27017/`.

* **MongoDB Atlas:**
  Get your connection string and replace `uri` with it.

---

### ▶️ **Run the Server**

```bash
uvicorn main:app --reload
```

---

### 🌐 **API Endpoints**

| Method | Endpoint       | Description                |
| ------ | -------------- | -------------------------- |
| GET    | `/`            | Check connection           |
| GET    | `/save/{name}` | Save a new name to MongoDB |
| GET    | `/list`        | Retrieve all stored names  |

---

### 🧪 **Example Usage**

#### ✅ Save a name

```
GET http://127.0.0.1:8000/save/Alice
→ {"inserted_id": "652123...", "message": "Saved name: Alice"}
```

#### 📋 View all names

```
GET http://127.0.0.1:8000/list
→ {"count": 2, "names": ["Alice", "Bob"]}
```

---

### 💡 **Key Learnings**

* Connect FastAPI with MongoDB using **PyMongo**.
* Perform **simple insert and read operations** via API routes.
* Structure a minimal **REST API backend** for databases.

