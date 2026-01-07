# 📰 Project 34 – News Aggregator CLI

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-green)
![Requests](https://img.shields.io/badge/Requests-HTTP_Client-orange)
![Rich](https://img.shields.io/badge/Rich-CLI_UI-purple)
![CLI](https://img.shields.io/badge/App-CLI-brightgreen)

---

## 📌 Project Overview

**News Aggregator CLI** is a **command-line application** that scrapes the latest news headlines from **BBC News (India section)** and displays them in a **beautiful tabular format** using Rich.

This project demonstrates:

* Real-world web scraping
* HTML parsing
* Clean CLI presentation
* Structured data extraction

> 🧠 This project is ideal after learning **Requests + BeautifulSoup + Rich**.

---

## 📁 Project Structure

```
Project_34_News_Aggregator_CLI/
│
├── main.py
└── requirements.txt
```

---

## ✨ Features

* Fetches **latest BBC India news**
* Scrapes:

  * Update time
  * Headline
  * Short description
  * News URL
* Displays news in a **rich table**
* Clickable links in terminal (supported terminals)
* No API key required
* Beginner-friendly & synchronous Python

---

## 🌐 Data Source

**BBC News – India Section**

```
https://www.bbc.com/news/world/asia/india
```

⚠️ This project is for **educational purposes only**.

---

## ⚙️ Prerequisites

* Python **3.10+**
* Internet connection
* Basic Python & HTML knowledge

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/news-aggregator-cli.git
cd news-aggregator-cli
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install requests beautifulsoup4 lxml rich
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 🖥️ Output Preview

```
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Updated on    ┃ Headline            ┃ Description         ┃ URL                 ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
┃ 2 hours ago   ┃ Major news headline ┃ Short description   ┃ https://bbc.com/...  ┃
└───────────────┴─────────────────────┴─────────────────────┴─────────────────────┘
```

---

## 🧠 How It Works

1. Sends HTTP request to BBC News
2. Parses HTML using **BeautifulSoup**
3. Locates the main news section using `data-testid`
4. Extracts:

   * Timestamp
   * Headline
   * Description
   * Relative link
5. Converts links to absolute URLs
6. Displays everything in a **Rich Table**

---

## 🧪 requirements.txt

```txt
requests
beautifulsoup4
lxml
rich
```

---

## 🧠 Concepts Covered

* Web Scraping fundamentals
* HTML parsing
* Attribute-based element selection
* Rich tables & CLI formatting
* HTTP requests
* Data cleaning
* Real-world scraping logic

---

## ⚠️ Limitations

* Website structure changes may break scraper
* Depends on BBC’s HTML layout
* No pagination or category selection

---

## 🚀 Possible Enhancements

* Multiple news sources (CNN, NDTV, TOI)
* Category selector (Politics, Tech, Sports)
* Save news to JSON / CSV
* MongoDB news storage
* Email / desktop notifications
* FastAPI backend
* Scheduled scraping (cron)

---

## 👨‍💻 Author

**Pinaka**
📘 *CodeShiksha – Python Mastery Course*
🧑‍💻 CLI + Web Scraping Project
