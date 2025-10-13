# 🔐 Chapter 32 – Authentication in FastAPI (with Password Hashing)

In this chapter, we’ll learn **how to implement authentication securely** using:
- **FastAPI** for endpoints  
- **MongoDB** for user data storage  
- **hashlib (SHA256)** for password hashing  

---

## 🔹 Why Hash Passwords?
Never store raw passwords!  
Instead, we store a **hash** (a one-way encoded version).

Example:
```

"hello123"  →  "b1946ac92492d2347c6235b4d2611184"

```

Hashing ensures:
- Even if DB leaks → passwords stay unreadable
- Each login compares **hash of input** with **stored hash**

---

## 🔹 How It Works
```

    ┌──────────────┐
    │ User Signup  │
    └──────┬───────┘
           │
    password → hash(password)
           │
           ▼
    Stored in MongoDB
           │
    ┌──────┴───────┐
    │ User Login   │
    └──────┬───────┘
           │
  input password → hash
           │
   Compare with DB hash → ✅ or ❌
```


---

## 🔹 API Endpoints

| Method | Route      | Description |
|---------|-------------|-------------|
| `POST`  | `/register` | Register new user (hash + store) |
| `POST`  | `/login`    | Verify user using hashed password |

---

## 🧠 Summary
- Use **hashlib.sha256()** to hash passwords  
- Store only the hash in MongoDB  
- Verify login by comparing input hash with stored hash  
- Never print or log raw passwords
