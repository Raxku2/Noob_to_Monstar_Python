# 📝 Practice Problem – FastAPI Basics

## Problem
Create a FastAPI app with the following routes:

1. `GET /books` → Returns a list of books (use a fake list).
2. `POST /addbook/{title}` → Add a new book using **path parameter**.
3. `GET /searchbook` → Search for a book by **query parameter** (`title`).
4. `POST /addbookjson` → Add a book using **request body** (with `title` and `author`).

---

## Example Output

### 1. `/books`
```json
{"data": ["1984", "Python 101"]}
````

### 2. `/addbook/AI`

```json
{"status": "Book added successfully"}
```

### 3. `/searchbook?title=1984`

```json
{"found": true, "title": "1984"}
```

### 4. `/addbookjson`

Request Body:

```json
{"title": "MongoDB Guide", "author": "Dwight"}
```

Response:

```json
{"status": "Book added successfully"}
```
