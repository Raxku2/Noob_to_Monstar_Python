# 📝 Practice Problem – CRUD with FastAPI & MongoDB

## Problem
Build an API to manage **library books** using FastAPI + MongoDB.

1. Create a database `libraryDB` and collection `books`.
2. Add API routes:
   - `POST /addbook` → Add book (title, author, year)
   - `GET /allbooks` → Show all books
   - `POST /editbook` → Update book title by id
   - `GET /removebook` → Delete a book by id

---

## Expected Output

### Add Book
```json
{"status": "66bcd123"}
````

### Show All Books

```json
{
  "data": [
    {"_id": "66bcd123", "title": "Python 101", "author": "Guido", "year": 2020}
  ]
}
```

### Edit Book

```json
{"status": 1}
```

### Remove Book

```json
{"status": 1}
```

