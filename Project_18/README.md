# 🧾 Project 18 – Inventory Management System (CLI + MongoDB)

A command-line based **Inventory Management System** built using **Python** and **MongoDB**.  
It allows users to manage products — add, view, update, delete, and search inventory items easily.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![CLI](https://img.shields.io/badge/Interface-Command_Line-black?logo=terminal)

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| ➕ Add Item | Add a new product with name, quantity, and price |
| 👀 View Items | Display all items from the inventory |
| 🔁 Update Item | Modify quantity of existing items |
| 🗑️ Delete Item | Remove items from database |
| 🔍 Search Item | Find items by name instantly |
| 🚪 Exit | Quit the program safely |

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install pymongo
````

### 2️⃣ Setup MongoDB

* Install MongoDB locally **or** use **MongoDB Atlas**.
* Update connection string if needed:

```python
client = MongoClient("mongodb://localhost:27017/")
```

### 3️⃣ Run the App

```bash
python inventory.py
```

---

## 🧭 Command Flow Diagram

```
┌──────────────────────────────┐
│     INVENTORY CLI APP        │
└────────────┬─────────────────┘
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
 [Add]    [View]    [Update]
    │        │        │
    ▼        ▼        ▼
 [Insert] [Read]   [Modify]
             │
             ▼
         [Delete/Search]
```

---

## 🧠 Concepts Practiced

* Python & CLI Menu Design
* CRUD Operations with MongoDB
* Data Validation
* Modular Functions in Python
* Persistent Database Storage

---

## 📄 Example Run

```
==== INVENTORY MANAGEMENT SYSTEM ====
1. Add Item
2. View All Items
3. Update Item Quantity
4. Delete Item
5. Search Item
6. Exit
```

---

## 📦 Database Structure (MongoDB)

```json
{
  "name": "apple",
  "quantity": 10,
  "price": 25.5
}
```

---

## 🪄 Future Enhancements

* Add login system for multiple users
* Implement GUI using Tkinter or FastAPI dashboard
* Add low-stock alerts and export to CSV

