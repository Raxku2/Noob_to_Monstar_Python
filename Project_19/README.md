### 📝 Project 19 – Student Database CLI (MongoDB + Rich)

A **Command-Line Student Management System** with **MongoDB backend** and a **colorful interface using Rich**.
Supports **CRUD operations**: add, view, update, delete, and list students with a clean menu-driven interface.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">  
  <img src="https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb" alt="MongoDB">  
  <img src="https://img.shields.io/badge/Library-Rich-orange" alt="Rich">  
  <img src="https://img.shields.io/badge/Interface-Command%20Line-lightgrey" alt="CLI">  
</p>

---

## ✨ Features

* ➕ **Add students** with name, roll number, course, year, and email.
* 📜 **List all students** in a formatted Rich table.
* 🔍 **View details** of a student by roll number.
* ✏️ **Update student details** easily.
* 🗑️ **Delete students** with confirmation prompt.
* 🎨 **Beautiful, colorful CLI** using Rich panels, tables, and prompts.
* 🌐 **MongoDB backend** ensures persistent storage.

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd Project_19_Student_Database_CLI
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
python student_cli.py
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

* Building **menu-driven CLI applications**.
* Performing **CRUD operations** with MongoDB via PyMongo.
* Using **Rich library** for visually appealing CLI interfaces.
* Handling user inputs safely and efficiently.

---

## 📄 requirements.txt

```
pymongo
rich
```

---

## 🚀 Possible Improvements

* Add **search functionality** by name or course.
* Implement **login/authentication system** for admin access.
* Add **export/import** options (CSV/Excel).
* Extend it into **Inventory or Employee Management System**.
* Create a **GUI version** using Tkinter or Flask.

