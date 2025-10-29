# 🔐 Project 23 – User Authentication API (FastAPI + MongoDB + Frontend UI)

This project demonstrates a **secure login system** using:
- **FastAPI** for backend API  
- **MongoDB** for user credential storage  
- **Frontend (HTML + JS)** for login UI  
- **Password hashing (SHA256 + Base64)** for encryption  
- **Token generation** for session validation  

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.120.0-brightgreen?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![HTML5](https://img.shields.io/badge/Frontend-HTML5-orange?logo=html5)
![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-yellow?logo=javascript)

---

## 🧱 Folder Structure

```

Project_23_User_Authentication_API/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
└── frontend/
├── assets/
│   └── favicon.png
└── index.html

````

---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
````

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup MongoDB Connection

Create a `.env` file inside `/backend`:

```bash
USER_DB_URI=mongodb+srv://your_user:password@cluster-url/
```

### 4️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server runs at 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔹 API Endpoints

| Method | Route    | Description                         |
| ------ | -------- | ----------------------------------- |
| `GET`  | `/`      | API Health check                    |
| `POST` | `/login` | Validate credentials & return token |

---

### 🧩 Request Example

**POST** `/login`

```json
{
  "email": "user@mail.com",
  "passwd": "U1FsdGVkX19..."
}
```

### ✅ Success Response

```json
{
  "message": "logged in",
  "token": "a4d5b238d1d60b8ce91a09f1e41e7aa0b2a3e45b",
  "status": 200
}
```

### ❌ Error Responses

```json
{"message": "Invalid Password", "status": 403}
{"message": "invalid username", "status": 404}
```

---

## 🔐 How Password Hashing Works

1. **Frontend (JS)** → hashes password using:

   ```js
   const hashBuffer = await crypto.subtle.digest('SHA-256', data)
   const base64Hash = btoa(String.fromCharCode(...new Uint8Array(hashBuffer)))
   ```
2. **Backend (Python)** → hashes stored password using:

   ```python
   hash_bytes = hashlib.sha256(data).digest()
   base64_hash = base64.b64encode(hash_bytes).decode('ascii')
   ```
3. Both are compared directly — no raw passwords are sent or stored.

---

## ⚙️ Token System

Each successful login returns a **unique 40-character token**:

```python
token = secrets.token_hex(20)
```

Tokens can be used in future for protected routes or session validation.

---

## 🖥️ Frontend Setup

### 1️⃣ Open `frontend/index.html` in browser

No server needed — it connects to the backend API at:

```
http://127.0.0.1:8000/login
```

### 2️⃣ UI Flow

* User enters email & password
* Password hashed in browser (client-side)
* Sent to backend for verification
* On success → displays **“Logged In”** message
* On error → shows message from API

---

## 📸 UI Preview (Text Diagram)

```
+------------------------------------------------+
| LOGO                             About         |
|------------------------------------------------|
|                                                |
|          [ E-Mail Input Field ]                |
|          [ Password Input Field ]              |
|               [ Login Button ]                 |
|                                                |
|  Loading... / Logged In / Error!! messages     |
|                                                |
+------------------------------------------------+
| © 2025 YantraYodha | CodeShiksha Python Mastery |
+------------------------------------------------+
```

---

## 📄 requirements.txt

```
annotated-doc==0.0.3
annotated-types==0.7.0
anyio==4.11.0
click==8.3.0
dnspython==2.8.0
dotenv==0.9.9
fastapi==0.120.0
h11==0.16.0
idna==3.11
pydantic==2.12.3
pydantic_core==2.41.4
pymongo==4.15.3
python-dotenv==1.1.1
python-stdnum==2.1
sniffio==1.3.1
starlette==0.48.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.38.0
```

---

## 🧠 Concepts Covered

* Password hashing (SHA-256 + Base64)
* Token-based authentication
* Client-side hashing with Web Crypto API
* Cross-Origin setup with CORS middleware
* Integration of HTML frontend and FastAPI backend
* Secure MongoDB credential validation

---

## 🪄 Future Improvements

* JWT-based session authentication
* Token expiry and refresh system
* Password reset / registration API
* Email verification flow
* Integration with FastAPI’s OAuth2

---

## 👨‍💻 Credits

**Developed by:** [Pinaka](https://github.com/raxku2)
**Project Series:** [CodeShiksha – Python Bhasha Mastery](https://github.com/Raxku2/Noob_to_Monstar_Python/tree/main)
**Year:** © 2025

---

✅ **What this project teaches**
- Full-stack authentication workflow  
- Practical CORS setup  
- Secure credential handling  
- Hash comparison logic  
- FastAPI + MongoDB integration in production-ready structure  
