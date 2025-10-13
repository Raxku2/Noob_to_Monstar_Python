### 📝 Project 20 – Notes App CLI (Python + MongoDB)

A **simple command-line Notes App** that stores notes in **MongoDB**.
Supports **CRUD operations**: add, view, update, and delete notes in a persistent database.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">  
  <img src="https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb" alt="MongoDB">  
  <img src="https://img.shields.io/badge/Interface-Command%20Line-lightgrey" alt="CLI">  
</p>

---

## ✨ Features

* 📝 **Add notes** with title and content.
* 📜 **View all notes** in a clean list.
* ✏️ **Update existing notes** by ID.
* 🗑️ **Delete notes** by ID.
* 🌐 **Persistent storage** using MongoDB.
* 💻 **Simple CLI interface** for beginner-friendly usage.

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd Project_20_Notes_App_CLI
```

2. **Install dependencies**

```bash
pip install pymongo
```

3. **Setup MongoDB**

* **Local:** Default URI `"mongodb://localhost:27017/"`
* **Atlas:** Replace the URI in `MongoClient()` with your Atlas URI.

4. **Run the app**

```bash
python notes_app.py
```

---

## 🖥️ Example Usage

**Main Menu**

```
--- Notes App ---
1. Add Note
2. View Notes
3. Update Note
4. Delete Note
5. Exit
```

**Add a Note**

```
Enter note title: Shopping List
Enter note content: Milk, Eggs, Bread
Note added with ID: 6512bd43d9caa6e02c990b0a
```

**View Notes**

```
ID: 6512bd43d9caa6e02c990b0a, Title: Shopping List, Content: Milk, Eggs, Bread
```

**Update a Note**

```
Enter the ID of the note to update: 6512bd43d9caa6e02c990b0a
Enter new title: Grocery List
Enter new content: Milk, Eggs, Bread, Butter
Modified count: 1
```

**Delete a Note**

```
Enter the ID of the note to delete: 6512bd43d9caa6e02c990b0a
Deleted count: 1
```

---

## 🧠 Key Learnings

* Performing **CRUD operations** with MongoDB.
* Building a **simple CLI application** in Python.
* Handling **user input safely and persistently**.
* Learning basics of **database connection, insertion, updates, and deletion**.

---

## 📄 requirements.txt

```
pymongo
```

---

## 🚀 Possible Improvements

* Use **Rich library** for better CLI visualization.
* Implement **search and filter** notes functionality.
* Add **login/authentication** for multiple users.
* Support **tags or categories** for notes.
* Add **export/import** options (CSV/JSON).

