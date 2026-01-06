# 💰 Project 30 – Budget Tracker CLI

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Rich](https://img.shields.io/badge/Rich-CLI_UI-purple)
![JSON](https://img.shields.io/badge/Data-JSON-orange)
![CLI](https://img.shields.io/badge/App-CLI-green)

---

## 🧠 Project Overview

The **Budget Tracker CLI** is a **command-line personal finance application** that helps users:

* Track **income**
* Record **expenses**
* View **current balance**
* See **expense summaries by category**

All data is stored locally in a **JSON file**, making it simple, fast, and beginner-friendly — no database required.

---

## 📁 Project Structure

```
Project_30_Budget_Tracker_CLI/
│
├── main.py        # Main CLI application
└── Data.json      # Auto-created expense database
```

📍 Data file is stored automatically at:

```
~/Documents/Expenses/Data.json
```

---

## ✨ Features

* ✅ Add income with source
* ✅ Add expenses with category & notes
* ✅ Auto date tracking
* ✅ View total income, expenses & balance
* ✅ Category-wise expense summary (table view)
* ✅ Rich-powered colorful CLI UI
* ✅ Persistent storage using JSON

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/budget-tracker-cli.git
cd budget-tracker-cli
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install rich
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

## 🧩 How Data is Stored

Data is saved in a JSON file:

```json
{
    "income": [
        {
            "amount": 5000,
            "source": "Salary",
            "date": "2025-01-10"
        }
    ],
    "expenses": [
        {
            "amount": 500,
            "category": "Food",
            "note": "Lunch",
            "date": "2025-01-10"
        }
    ]
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

## 🧠 Core Concepts Used

* File handling (`json`, `os.path`)
* Data persistence
* Python functions
* CLI loops & menus
* `rich` for:

  * Colored text
  * Tables
  * Prompts
* Date handling (`datetime`)
* Garbage collection basics (`gc.collect()`)

---

## 🚀 Possible Improvements

* Monthly budget limits
* Export to CSV
* Charts using `rich` or `matplotlib`
* Password-protected budget file
* Category-wise filtering
* FastAPI version with frontend

---

## 👨‍💻 Author

**Rakesh**
📘 *Project from CodeShiksha – Python Mastery Course*
🎯 Beginner-friendly real-world CLI application


