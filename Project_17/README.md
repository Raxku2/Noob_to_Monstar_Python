# 📝 Project 17 – Registration Form CLI (MongoDB backend)

A **Command-Line Registration System** that stores user data in **MongoDB Atlas**.  
Users can **register with username, email, and password** or **list all registered users**.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![PyMongo](https://img.shields.io/badge/Library-PyMongo-orange)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)
![dotenv](https://img.shields.io/badge/Security-dotenv-important)

---

## ✨ Features
- 📝 Register new users with **name, username, email, and password**.
- 🔐 Passwords are hidden during entry (`getpass`).
- 🛑 Prevents duplicate usernames or emails.
- 📜 List all registered users (without passwords).
- 🌐 Uses **MongoDB Atlas cloud database** as backend.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_17_Registration_Form_CLI
   ````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup MongoDB URI in `.env` file**

   ```env
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
   ```

4. **Run the program**

   ```bash
   python registration_cli.py --reg -n "Arjun" -u "arjun01" -e "arjun@example.com"
   ```

---

## 🖥️ Example Usage

### Register a User

```bash
python registration_cli.py --reg -n "Riya" -u "riya88" -e "riya@example.com"
Password: ******
✅ Registration successful!
```

### List Users

```bash
python registration_cli.py --list
{'name': 'Riya', 'username': 'riya88', 'email': 'riya@example.com'}
{'name': 'Arjun', 'username': 'arjun01', 'email': 'arjun@example.com'}
```

---

## 🧠 Key Learnings

* How to build a **CLI tool** with `argparse`.
* How to use **PyMongo** for database operations.
* How to **securely store API credentials** using `.env`.
* How to safely **hide passwords** in CLI.

---

## 📄 requirements.txt

```
pymongo
python-dotenv
```

---

## 🚀 Possible Improvements

* Add **password hashing** (e.g., bcrypt) instead of storing plain text.
* Add **login authentication** with username + password.
* Add **update/delete user** functionality.
* Create a **GUI version** with Tkinter or Flask.
