# 📁 Project_28: File Sharing App (CLI)

> **Author:** Pinaka
> **Type:** CLI + WebSocket App
> **Level:** Advanced
> **Architecture:** Client–Server
> **Protocol:** WebSocket

---

## 🚀 Overview

This project is a **real-time file sharing system** built using **FastAPI WebSockets** and **Python CLI clients**.

It allows:

* One **Sender** to upload a file
* Multiple **Receivers** to receive the file **live**
* Chunk-based binary streaming
* Automatic reconnect for receivers

This mimics how **real production file streaming systems** work.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-WebSocket-green?style=flat-square)
![WebSocket](https://img.shields.io/badge/WebSocket-Realtime-orange?style=flat-square)
![AsyncIO](https://img.shields.io/badge/AsyncIO-EventLoop-lightgrey?style=flat-square)
![CLI](https://img.shields.io/badge/CLI-Terminal-black?style=flat-square)

---

## 🧱 Architecture

```
            ┌──────────────┐
            │   Sender CLI │
            └──────┬───────┘
                   │
                   │ WebSocket
                   ▼
        ┌────────────────────────┐
        │   FastAPI WebSocket API │
        │  /sender    /receiver  │
        └──────┬───────────┬─────┘
               │           │
               ▼           ▼
        Receiver CLI   Receiver CLI
```

---

## 📂 Project Structure

```
Project_28/
├── api/
│   └── main.py        # FastAPI WebSocket server
├── client/
│   ├── sender.py     # File sender CLI
│   └── receiver.py   # File receiver CLI
└── README.md
```

---

## ✨ Features

* 📤 Send any file (binary safe)
* 📥 Receive files in real time
* 🔄 Chunk-based streaming
* 👥 Multiple receivers supported
* ♻ Auto-reconnect receiver
* 🧠 Minimal & clean protocol
* 🖥️ CLI-first design

---

## 📦 Requirements

### Server

```
fastapi
uvicorn
```

### Client

```
websockets
```

Install with:

```bash
pip install fastapi uvicorn websockets
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📥 Receiver CLI (Download Files)

```bash
python receiver.py
```

* Automatically connects to server
* Waits for incoming files
* Saves files as:

  ```
  rcv_<original_filename>
  ```
* Auto-reconnects if connection drops

---

## 📤 Sender CLI (Upload File)

```bash
python sender.py
```

Enter full file path:

```
/home/user/Documents/test.pdf
```

✔ File will be streamed to **all connected receivers**

---

## 🔄 Data Transfer Protocol

| Signal             | Meaning                |
| ------------------ | ---------------------- |
| `START:<filename>` | File transfer begins   |
| Binary chunks      | File data              |
| `__end__`          | File transfer complete |
| `END`              | Receiver closes file   |

---

## 🧠 Professional Mindset (Important)

### ❌ Naive Approach

* Sending file in one piece
* Blocking sockets
* No reconnect logic

### ✅ Production Approach (This Project)

* Chunk streaming
* Binary-safe transfer
* Receiver reconnection
* Server fan-out to multiple clients
* Stateless sender

---

## ⚠️ Limitations (Intentional for Learning)

* No encryption
* No authentication
* No resume support
* No file validation

👉 These are **next-level enhancements**, not beginner concepts.

---

## 🧪 Testing Tips

* Start **server**
* Start **multiple receivers**
* Send **large files**
* Disconnect receiver → auto reconnect works

---

## 🏁 Conclusion

This project demonstrates:

* **Real networking concepts**
* **How file streaming actually works**
* **Why WebSockets are used**
* **How to think like a backend engineer**

It is **far beyond a basic Python project** and suitable for:

* Resume
* Portfolio
* Interview discussion

---

