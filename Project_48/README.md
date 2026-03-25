# 💬 Project_48: CLI Chat App

### Real-Time Terminal Chat using Textual + MongoDB

**Author: Pinaka**

---

# 📌 Project Overview

This project is a **real-time CLI Chat Application** built using:

* 🖥 **Textual** (Terminal UI Framework)
* 🍃 **MongoDB** (Database)
* ⚡ **Motor (Async MongoDB Driver)**
* 🐍 **Python Async Programming**

It simulates a **live chat room** directly inside the terminal.

---

# 🏗 Project Architecture

```
User (Terminal UI)
        ↓
Textual App (Frontend in CLI)
        ↓
Async MongoDB (Motor)
        ↓
Database (Messages Collection)
        ↓
Other Users (Polling every second)
```

---

# ✨ Features

## 🔐 Login System

* Modal popup for username
* Simple entry-based authentication
* Default fallback → "Anonymous"

---

## 💬 Real-Time Messaging

* Send messages instantly
* Messages stored in MongoDB
* Live updates every 1 second

---

## 📜 Chat History

* Loads recent messages (last 1 minute)
* Avoids flooding UI with old messages
* Can be modified for full history

---

## 🎨 Styled Terminal UI

* Header & Footer
* Scrollable chat window
* Highlighted usernames
* Message containers with styling

---

## ⚡ Async Architecture

* Non-blocking UI
* Async DB operations
* Smooth user experience

---

# 🗄 Database Structure

Each message stored like:

```json
{
  "_id": "ObjectId",
  "text": "Hello World",
  "author": "Pinaka",
  "timestamp": "2026-03-26T10:30:00"
}
```

---

# 🧠 Concepts You Learn

---

## 1️⃣ Textual (CLI UI Framework)

* Layout using `Vertical`, `Container`
* Widgets: Input, Static, Label
* Modal screens
* Styling with CSS-like syntax
* Live updating UI

---

## 2️⃣ Async Programming

* `async / await`
* Non-blocking operations
* Background polling (`set_interval`)
* Async database queries

---

## 3️⃣ MongoDB with Motor

* Async database connection
* `find()` with filters
* `insert_one()`
* Sorting with timestamps

---

## 4️⃣ Real-Time System Design (Basic)

* Polling approach (every 1 second)
* Timestamp-based fetching
* State tracking (`last_timestamp`)

---

# ⚙ Installation Guide

---

## 1️⃣ Install Dependencies

```bash
pip install textual motor pymongo python-dotenv
```

---

## 2️⃣ Setup Environment Variables

Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 3️⃣ Run the Application

```bash
python main.py
```

---

# 🎮 How to Use

---

## Step 1: Login

* Enter username in popup

## Step 2: Start Chatting

* Type message → Press Enter

## Step 3: Live Updates

* Messages appear automatically
* Other users’ messages also visible

---

# 🔄 How Real-Time Works

* App checks DB every **1 second**
* Fetches messages newer than `last_timestamp`
* Updates UI dynamically

```python
self.set_interval(1.0, self.fetch_new_messages)
```

---

# 🎨 UI Design Highlights

* Chat messages styled with:

  * Colored usernames
  * Bold formatting
  * Container boxes

* Scrollable chat window

* Clean terminal layout

---

# 🚀 Advanced Improvements

Take this to the next level:

---

## 🔥 Real-Time Upgrade

* Replace polling with **WebSockets**
* Instant message delivery

---

## 👥 Multi-Room Chat

* Create chat rooms
* Join/leave rooms

---

## 🔐 Authentication System

* Password login
* JWT authentication

---

## 🧾 Message Features

* Edit messages
* Delete messages
* Reply system
* Reactions (👍 ❤️)

---

## 📦 Performance Improvements

* Pagination for messages
* Load older messages on scroll

---

## 🎨 UI Enhancements

* Emojis support
* Typing indicators
* Message timestamps display

---

**Author: Pinaka**
