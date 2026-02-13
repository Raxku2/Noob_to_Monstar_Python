# 💸 Project_52: Finance Tracker App

### A Complete MongoDB + Rich CLI Financial Management System

**Author: Pinaka**

---

## 📌 Project Overview

The **Finance Tracker CLI** is a real-world terminal-based financial management system built using:

* 🐍 Python
* 🍃 MongoDB
* 🎨 Rich (Beautiful CLI UI)
* 🔐 dotenv (Environment configuration)

This project teaches you how to build a **persistent financial tracking system** using a database and professional CLI interface.

You are not just storing numbers.
You are building a real financial system.

---

# 🏗 Project Architecture

```
User (CLI)
   ↓
Rich Styled Interface
   ↓
Python Business Logic
   ↓
MongoDB Database
```

---

# 📦 Core Features

## ✅ Income Management

* Add income entries
* Categorize income
* Add notes
* Timestamp tracking

## ✅ Expense Management

* Add expense entries
* Categorize spending
* Add notes
* Automatic date recording

## ✅ Transaction Viewer

* Styled transaction table
* Colored income/expense rows
* Date formatting
* Clean display format

## ✅ Monthly Summary

* Automatic month detection
* Total income calculation
* Total expense calculation
* Savings calculation

## ✅ Balance Checker

* Total income
* Total expense
* Net balance
* Savings/Loss indicator

## ✅ Animated Welcome Screen

* Dynamic colored animation
* Professional CLI introduction
* Live rendering with Rich

---

# 🗄 Database Structure

Each transaction stored in MongoDB:

```json
{
  "type": "income",
  "amount": 5000,
  "category": "Freelancing",
  "note": "Website project payment",
  "created_at": "2026-02-12T18:30:21"
}
```

Types:

* `"income"`
* `"expense"`

---

# 🧠 What You Learn in This Project

---

## 1️⃣ MongoDB Integration

* Connecting using `MongoClient`
* Using environment variables
* insert_one()
* find()
* Iterating documents
* Working with datetime fields

---

## 2️⃣ CLI UI Design with Rich

* Console rendering
* Panels
* Tables
* Live animations
* Color formatting
* Alignment
* Styled headers
* Clean menu layout

---

## 3️⃣ Financial Logic Implementation

* Total income calculation
* Expense tracking
* Monthly filtering
* Savings calculation
* Balance computation
* Data validation checks

---

## 4️⃣ Environment Configuration

Using `.env` file:

```
MONGO_URI=your_mongodb_connection_string
DB_NAME=financeDB
```

This keeps credentials secure and professional.

---

# ⚙ Installation Guide

---

## 1️⃣ Install Dependencies

```bash
pip install pymongo python-dotenv rich
```

---

## 2️⃣ Setup MongoDB

Create a MongoDB Atlas cluster
Copy your connection string

Create a `.env` file in project root:

```
MONGO_URI=your_connection_string
DB_NAME=your_database_name
```

---

## 3️⃣ Run the Application

```bash
python main.py
```

---

# 📋 Main Menu Options

```
1️⃣ Add Income
2️⃣ Add Expense
3️⃣ View Transactions
4️⃣ Monthly Summary
5️⃣ Check Balance
0️⃣ Exit
```

---

# 💰 Financial Calculations

## Balance Formula:

```
Balance = Total Income - Total Expense
```

## Savings Logic:

* Positive → Saving
* Negative → Loss
* Zero → Break-even

---

# 🎯 Skills Gained

After completing this project, you now understand:

* CLI-based financial systems
* Persistent database storage
* Monthly data filtering
* Structured financial reporting
* Rich UI design principles
* Real-world system architecture
* Clean terminal UX design

---

**Author: Pinaka**
