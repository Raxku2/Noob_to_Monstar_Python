# 🔑 Project 10: Password Generator  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![CLI](https://img.shields.io/badge/Interface-CLI-green)]()  
[![Cross-Platform](https://img.shields.io/badge/OS-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey)]()  

---

## 📖 Overview
A **Password Generator CLI Tool** that creates secure passwords of custom length, with optional special characters.  
The password is automatically copied to the clipboard and a notification is displayed.  

---

## ✨ Features
- 🔒 Generate secure random passwords  
- ⚡ Option to include/exclude special characters  
- 📋 Auto-copy password to clipboard  
- 🔔 Desktop notification after generation  
- 🌍 Cross-platform support (Linux, Windows, macOS)  

---

## 🛠️ Tech Stack
- **Python 3.x**
- `random` → generate characters
- `pyperclip` → clipboard handling
- `subprocess` → desktop notifications

---

## 🚀 User Guide

### 1️⃣ Requirements
- Python 3.x installed
- Install dependencies:
```
pip install pyperclip
````

### 2️⃣ Run the Project

```
python main.py
```

### 3️⃣ Example Run

```
Enter Password length: 12
Do you want special character? y/n: y
Generated Password: A3p!Qz8xRk@D
Copied to clipboard ✅
```

---

## ⚙️ Cross-Platform Notes

* **Linux** → requires `xclip` or `xsel` for clipboard, and `notify-send` for notifications.
* **Windows** → pyperclip works with default `clip`.
* **macOS** → pyperclip uses `pbcopy` internally.

---

## 🧩 Future Enhancements

* Exclude similar characters (0/O, 1/l).
* Strength meter for password.
* Generate multiple passwords at once.
* GUI support with Tkinter.

---

## 📂 Project Structure

```
Project_10_Password_Generator/
│── README.md        # Documentation
│── project.py       # Main source code
│── practice_set.md  # Challenges
│── solutions.md     # Hints/Solutions
```

