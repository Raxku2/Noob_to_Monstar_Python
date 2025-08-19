
# 📂 Chapter 18: Virtual Environment

### **notes.md**

````markdown
# Chapter 18: Virtual Environment (venv)

## 🌍 What is a Virtual Environment?
- A **self-contained folder** with its own Python interpreter + libraries.
- Keeps dependencies isolated from the global Python installation.

---

## 💡 Why use venv?
- Avoids conflicts between projects.
- Allows different versions of libraries for different projects.
- Keeps global Python clean.

---

## 🖥️ Creating venv

```bash
python -m venv myenv
````

👉 This creates a folder `myenv/` containing a new Python environment.

---

## ⚡ Activating venv

### 🔹 Windows (CMD/PowerShell)

```bash
myenv\Scripts\activate
```

### 🔹 Linux / Mac

```bash
source myenv/bin/activate
```

👉 After activation, you’ll see `(myenv)` prefix in terminal.

---

## ⏹️ Deactivating venv

```bash
deactivate
```

---

## 📦 Installing Packages inside venv

```bash
pip install requests
pip list
```

---

## 🔄 Visual Representation (ASCII Diagram)

```
+-----------------------------+
| Global Python Installation  |
|   - system libraries        |
|   - global site-packages    |
+-------------+---------------+
              |
              v
     +-------------------+
     |  Virtual Env      |
     |  (myenv/)         |
     |   - Python copy   |
     |   - pip           |
     |   - local libs    |
     +-------------------+
```

👉 Each project can have its **own venv** with independent packages.

---

## 📝 Quick Commands Cheat Sheet

| Action          | Windows                  | Mac/Linux                   |
| --------------- | ------------------------ | --------------------------- |
| Create venv     | `python -m venv myenv`   | `python3 -m venv myenv`     |
| Activate venv   | `myenv\Scripts\activate` | `source myenv/bin/activate` |
| Deactivate venv | `deactivate`             | `deactivate`                |
| Install package | `pip install <pkg>`      | `pip install <pkg>`         |
| List packages   | `pip list`               | `pip list`                  |



