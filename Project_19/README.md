### 📝 Project 18 – Student/Inventory Management System CLI (MongoDB + Rich)

A **Command-Line Management System** for **students or inventory**, powered by **MongoDB** and enhanced with **Rich** for a clean, colorful interface.
Users can **add, view, update, delete, and list entries** with an intuitive menu-driven CLI.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![Rich](https://img.shields.io/badge/Library-Rich-orange)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)

---

## ✨ Features

* ➕ **Add entries** with full details (name, roll, course, year, email).
* 📜 **List all entries** in a formatted table.
* 🔍 **View specific entry** by roll number.
* ✏️ **Update existing entries** easily.
* 🗑️ **Delete entries** with confirmation.
* 🎨 **Colorful CLI** using Rich panels, tables, and prompts.
* 🌐 **MongoDB backend** ensures persistent storage.

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd Project_18_Inventory_Management_CLI
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Setup MongoDB URI (optional, defaults to localhost)**

```bash
export MONGO_URI="mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/"
```

4. **Run the program**

```bash
python inventory_cli.py
```

---

## 🖥️ Example Usage

**Main Menu**

```
STUDENT DATABASE MENU
[1] Add Student
[2] List Students
[3] View Student
[4] Update Student
[5] Delete Student
[0] Exit
```

**Add a Student**

```
Enter name: Riya Sharma
Enter roll number: 101
Enter course: B.Tech
Enter year: 2
Enter email (optional): riya@example.com
✅ Student added successfully!
```

**List Students**

```
ID        Name         Roll  Course  Year  Email
a1b2c3d4  Riya Sharma  101   B.Tech 2     riya@example.com
```

**Update Student**

```
Enter roll number to update: 101
Leave blank to keep current value.
Name [Riya Sharma]: Riya S.
✅ Student updated successfully!
```

**Delete Student**

```
Enter roll number to delete: 101
Are you sure you want to delete Riya S.? [y/n]: y
🗑️ Student deleted successfully!
```

---

## 🧠 Key Learnings

* How to build a **menu-driven CLI** for CRUD operations.
* How to use **PyMongo** for database CRUD operations.
* How to enhance CLI UX using **Rich library** (tables, panels, prompts).
* How to handle user input safely and efficiently.

---

## 📄 requirements.txt

```
pymongo
rich
```

---

## 🚀 Possible Improvements

* Add **search functionality** by name or course.
* Implement **inventory management** features (quantity, price, category).
* Add **export/import** options (CSV/Excel).
* Integrate **login system** for user authentication.
* Create a **GUI version** using Tkinter or Flask.

