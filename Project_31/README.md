
# 💰 Project 31 – Expense Manager CLI (MongoDB Backend)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb)
![Rich](https://img.shields.io/badge/Rich-CLI_UI-purple)
![CLI](https://img.shields.io/badge/App-CLI-orange)

---

## 🧠 Project Overview

**Expense Manager CLI** is a **database-powered command-line application** that allows users to manage:

* ✅ Income records
* ✅ Expense records
* ✅ Total balance calculation
* ✅ Category-wise expense summary

Unlike the previous JSON-based version, this project **uses MongoDB** for permanent, scalable storage.

> 📌 This project introduces students to **real-world database usage in CLI apps**.

---

## 📁 Project Structure

```
Project_31_Expense_Manager_DB/
│
├── main.py          # Main CLI application
└── requirements.txt # Python dependencies
```

---

## ✨ Features

* Add income entries
* Add expense entries with category & notes
* Automatic date recording
* View total income, expenses & balance
* Category-wise expense summary (table)
* MongoDB-based persistent storage
* Rich-powered colorful CLI interface

---

## ⚙️ Prerequisites

* Python **3.10+**
* MongoDB

  * Local MongoDB **OR**
  * MongoDB Atlas
* Basic knowledge of CLI & Python functions

---

## 🔌 MongoDB Setup

### Option 1️⃣ Local MongoDB

```bash
mongodb://localhost:27017
```

### Option 2️⃣ MongoDB Atlas

1. Create a cluster
2. Create database user
3. Whitelist IP
4. Copy connection string

Update in `main.py`:

```python
MONGO_URI = "your_mongodb_connection_string"
```

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/expense-manager-db.git
cd expense-manager-db
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install rich pymongo
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 🖥️ CLI Menu

```
====== Budget Tracker CLI ======
1. Add Income
2. Add Expense
3. View Balance
4. Expense Summary
5. Exit
```

---

## 🗃️ Database Schema (MongoDB)

All records are stored in **one collection** using a `type` field.

### 📌 Income Document

```json
{
  "type": "i",
  "amount": 5000,
  "source": "Salary",
  "date": "2025-01-12"
}
```

### 📌 Expense Document

```json
{
  "type": "e",
  "amount": 500,
  "source": "Food",
  "note": "Lunch",
  "date": "2025-01-12"
}
```

---

## 📊 Expense Summary Output

```
┌───────────┬────────┐
│ Category  │ Amount │
├───────────┼────────┤
│ Food      │ 1200   │
│ Travel    │ 800    │
│ Shopping  │ 1500   │
└───────────┴────────┘
```

---

## 🧠 Concepts Covered

* MongoDB CRUD operations
* PyMongo (`insert_one`, `find`)
* Data aggregation using Python
* CLI menu loop
* Rich:

  * Tables
  * Prompts
  * Styled output
* Date handling (`datetime`)
* Database-backed application design

---

## 🆚 Project 30 vs Project 31

| Feature          | Project 30 | Project 31 |
| ---------------- | ---------- | ---------- |
| Storage          | JSON File  | MongoDB    |
| Scalability      | ❌ Limited  | ✅ High     |
| Database Skills  | ❌ No       | ✅ Yes      |
| Real-world Ready | ⚠️         | ✅          |

---

## 🚀 Possible Enhancements

* Monthly reports
* Date range filters
* User-based expenses
* Export to CSV
* FastAPI + Web UI version
* Authentication layer

---

## 👨‍💻 Author

**[Pinaka](https://github.com/raxku2)**

📘 *CodeShiksha – Python Mastery Course*
🎯 Beginner-friendly real-world database project

