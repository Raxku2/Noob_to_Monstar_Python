# 🧩 Practice Task – Authentication with Hashing

## Problem
Build a FastAPI-based authentication system using **hashing**.

### Features:
1. `POST /signup` → Takes `email`, `password`, hashes the password, and saves to DB.
2. `POST /signin` → Compares hashed password with DB and returns success or failure.
3. `GET /users` → Show all registered users (excluding password field).

---

### Example Flow

#### Register:
```

POST /signup?email=[test@abc.com](mailto:test@abc.com)&password=1234
→ {"status": "success", "message": "User registered"}

```

#### Login:
```

POST /signin?email=[test@abc.com](mailto:test@abc.com)&password=1234
→ {"status": "success", "message": "Welcome [test@abc.com](mailto:test@abc.com)!"}

```

#### Wrong Login:
```

POST /signin?email=[test@abc.com](mailto:test@abc.com)&password=wrong
→ {"status": "error", "message": "Invalid password"}

```

#### Get Users:
```

GET /users
→ [{"email": "[test@abc.com](mailto:test@abc.com)"}]

```
