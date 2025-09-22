# 📝 Practice Problem – FastAPI Hello World

## Problem
Create a FastAPI app with the following endpoints:

1. `/hello/{name}` → Returns a JSON response:  
   ```json
   {"message": "Hello, <name>!"}
   ````

2. `/square/{number}` → Returns the square of the given number.

---

## Expected Output

### Example 1

```bash
http://127.0.0.1:8000/hello/Riya
{"message": "Hello, Riya!"}
```

### Example 2

```bash
http://127.0.0.1:8000/square/7
{"square": 49}
```

