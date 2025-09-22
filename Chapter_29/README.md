# ⚡ Chapter 29 – FastAPI Setup & Hello World

FastAPI is a modern **Python web framework** for building APIs quickly, with automatic **documentation** and **validation**.

---

## 🔹 Why FastAPI?
✅ Super fast → built on **Starlette** and **Pydantic**  
✅ Automatic **API docs** at `/docs` and `/redoc`  
✅ Easy to build **CRUD APIs**  
✅ Async support for high performance  

---

## 🔹 Install FastAPI
```bash
pip install fastapi uvicorn
````

---

## 🔹 Create First FastAPI App

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"hello": "world", "name": "Rakesh"}
```

---

## 🔹 Run the Server

```bash
uvicorn main:app --reload
```

---

## 🔹 Visit Endpoints

* `http://127.0.0.1:8000/` → Home
* `http://127.0.0.1:8000/about` → About
* `http://127.0.0.1:8000/members` → Example members endpoint
* `http://127.0.0.1:8000/sum/5/10` → Path params sum

---

## 🔹 API Docs

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🔑 CRUD Mapping

```
Create   -> POST
Read     -> GET
Update   -> PUT / PATCH
Delete   -> DELETE
```

---

## 🧠 Summary

* Install FastAPI + uvicorn
* Create endpoints with `@app.get()` and `@app.post()`
* Run server → visit Swagger docs
