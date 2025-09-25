# ⚡ Chapter 30 – FastAPI Basics (Routes, Path Params, Query Params)

FastAPI lets you create APIs quickly using **routes**.  
We can pass data via:
- **Path Parameters** → part of the URL (`/items/5`)
- **Query Parameters** → after `?` in URL (`/search?name=apple`)
- **Request Body** → JSON data (validated with `pydantic` models)

---

## 🔹 Routes
```python
@app.get("/items")
def items():
    return {"data": fake_db}
````

---

## 🔹 Path Parameters

```python
@app.post("/additem/{fruit}")
def additem(fruit: str):
    fake_db.append(fruit)
    return {"status": "Item added successfully"}
```

Usage → `/additem/mango`

---

## 🔹 Query Parameters

```python
@app.get("/search")
def search_item(name: str):
    if name in fake_db:
        return {"found": True, "item": name}
    return {"found": False}
```

Usage → `/search?name=apple`

---

## 🔹 Request Body with Pydantic

```python
from pydantic import BaseModel

class Fruit(BaseModel):
    name: str

@app.post("/addfruit")
def addfruit(fruit: Fruit):
    fake_db.append(fruit.name)
    return {"status": "Item added successfully"}
```

Usage (POST request body):

```json
{
  "name": "grape"
}
```

---

## 🔹 API Docs

* Swagger: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🧠 Summary

* **Path params** → `/additem/mango`
* **Query params** → `/search?name=apple`
* **Request body** → JSON with Pydantic model
