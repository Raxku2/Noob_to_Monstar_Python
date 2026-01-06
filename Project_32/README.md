
# 🧠 Project 32 – Quiz App CLI (API Based)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![API](https://img.shields.io/badge/API-OpenTDB-orange)
![Rich](https://img.shields.io/badge/Rich-CLI_UI-purple)
![CLI](https://img.shields.io/badge/App-CLI-green)

---

## 🧠 Project Overview

**Quiz App CLI** is a **command-line based quiz application** that fetches **real-time questions from an online API** and lets users answer them interactively.

The app:

* Fetches MCQ questions from **Open Trivia DB**
* Displays questions in a colorful CLI
* Randomizes answer options
* Calculates score in real time
* Allows quitting anytime

> 📌 This project teaches **API consumption + CLI UX + logic building**.

---

## 📁 Project Structure

```
Project_32_Quiz_App/
│
├── main.py
└── requirements.txt
```

---

## ✨ Features

* Live questions from Open Trivia Database
* Multiple Choice Questions (MCQs)
* Option shuffling for fairness
* Score tracking
* Quit anytime (`Q`)
* Clean & colorful CLI using Rich
* No database, no async, no advanced concepts

---

## 🌐 API Used

**Open Trivia Database (OpenTDB)**
Free & open quiz API

Example endpoint:

```
https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple
```

* Category: Computers (18)
* Difficulty: Easy
* Question Type: Multiple Choice
* Questions per quiz: 10

---

## ⚙️ Prerequisites

* Python **3.10+**
* Internet connection
* Basic Python knowledge

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/quiz-app-cli.git
cd quiz-app-cli
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install requests rich
```

---

## ▶️ Run the Quiz App

```bash
python main.py
```

---

## 🖥️ Gameplay Flow

1. A question is fetched from the API
2. Question is displayed with 4 options
3. User selects:

   * `1 / 2 / 3 / 4` → Answer
   * `Q` → Quit quiz
4. Score updates automatically
5. Final score shown at the end

---

## 📌 Example Output

```
What does CPU stand for?

1. Central Processing Unit
2. Computer Personal Unit
3. Central Program Utility
4. Control Processing User

Choose Correct Option: 1
✔ Correct!
```

---

## 🧮 Scoring System

* ✅ Correct answer → +1 point
* ❌ Wrong answer → 0 point
* `Q` → Exit & show current score

---

## 🧠 Concepts Covered

* REST API consumption (`requests`)
* JSON parsing
* Generator functions (`yield`)
* Randomization (`shuffle`)
* HTML entity decoding (`html.unescape`)
* CLI interaction with Rich
* Input validation
* Memory cleanup (`gc.collect`)
* Real-time logic building

---

## 🧪 requirements.txt

```txt
requests
rich
```

---

## 🚀 Possible Enhancements

* Difficulty selection (easy / medium / hard)
* Category selection menu
* Timer-based questions
* High-score saving (JSON / DB)
* MongoDB leaderboard
* FastAPI quiz backend
* Web-based quiz frontend

---

## 👨‍💻 Author

**(Pinaka)[https://github.com/raxku2]**

📘 *CodeShiksha – Python Mastery Course*
🎯 Beginner-friendly API + CLI Project
