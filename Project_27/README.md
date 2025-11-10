# 💬 Project 27 – CLI Chat App (Socket Programming)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-WebSocket-green?logo=fastapi)
![HTML5](https://img.shields.io/badge/Frontend-HTML5-orange?logo=html5)
![RealTime](https://img.shields.io/badge/Feature-Realtime_Chat-blue?logo=websocket)
![Socket](https://img.shields.io/badge/Protocol-WebSocket-red?logo=socketdotio)

---

## 🧠 Overview

This project demonstrates **real-time chat** communication using **FastAPI’s WebSocket** feature.
Messages sent by any connected client are broadcasted instantly to all users — a simple **group chat** over a local WebSocket server.

---

## 📁 Project Structure

```
Project_27_CLI_Chat_App/
│
├── main.py               # FastAPI WebSocket backend
├── index.html            # Simple chat frontend
└── requirements.txt      # Dependencies list
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Raxku2/Noob_to_Monstar_Python/edit/main/Project_27.git
cd cli-chat-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧩 How It Works

* Clients connect via a **WebSocket endpoint** `/msg`.
* Each message is broadcasted to all connected clients.
* The `/send` route allows sending messages from any HTTP client (even curl or JS `fetch()`).
* HTML frontend connects automatically using JavaScript WebSocket.

---

## 🖥️ Frontend (index.html)

The frontend is a **minimal chat UI** that:

* Connects to `ws://127.0.0.1:8000/msg`
* Displays connection status (🟢 connected / 🔴 disconnected)
* Sends messages using `/send?msg=...`
* Auto-scrolls message log

---

## 🧠 Backend Code (main.py)

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

connections = []

@app.websocket('/msg')
async def message(websck: WebSocket):
    await websck.accept()
    connections.append(websck)
    try:
        while True:
            data = await websck.receive_text()
    except WebSocketDisconnect:
        connections.remove(websck)

@app.get('/send')
async def send(msg: str):
    for conn in connections:
        await conn.send_text(msg)
    return {"status": "ok", "message": msg}
```

---

## 🧩 Frontend Snippet

```html
<script>
const BASEAPI = "http://127.0.0.1:8000";
const socket = new WebSocket("ws://127.0.0.1:8000/msg");

socket.onmessage = e => {
    const message = document.createElement('p');
    message.textContent = '> ' + e.data;
    document.getElementById('msgbox').appendChild(message);
};
</script>
```

---

## 🧾 requirements.txt

```
fastapi==0.117.1
uvicorn==0.37.0
anyio==4.11.0
h11==0.16.0
idna==3.10
sniffio==1.3.1
```

---

## 🧪 Test the Chat

1. Open **two terminals or browsers** with `index.html`.
2. Type a message → It appears on **both screens** instantly!
3. You’ve built a **real-time communication system**. 🔥

---

## 🚀 Future Enhancements

* Add **username** and **message timestamps**
* Persist chat history in MongoDB
* Build a **React/Vue chat UI**
* Deploy with **WebSocket support on Render or Railway**

---

## 👨‍💻 Author

**YantraYodha**
💡 *Project from CodeShiksha Python Mastery Course (2025)*
🧩 Real-world implementation of Socket Programming using FastAPI.
