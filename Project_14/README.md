# 📰 Project 14 – News Headlines Scraper (BeautifulSoup)

A **Python CLI project** that scrapes the latest **national news headlines** from [The Hindu](https://www.thehindu.com/news/national/) using **Requests** and **BeautifulSoup**.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Library-Requests-green)
![BeautifulSoup](https://img.shields.io/badge/Parser-BeautifulSoup4-yellow)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)

---

## ✨ Features
- 🔍 Scrapes **real-time headlines** from The Hindu's national news section.
- 🧹 Automatically **cleans and formats** headline text.
- 🖥️ Displays headlines in a **numbered list** for easy reading.
- 🧠 Demonstrates how to **find and parse HTML tags** with BeautifulSoup.

---

## 📦 Installation & Setup

1. **Clone the project**
   ```bash
   git clone <your-repo-url>
   cd Project_14_News_Headlines_Scraper
   ````

2. **Install dependencies**

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the script**

   ```bash
   python news_scraper.py
   ```

---

## 🖥️ Example Output

```bash
Fetching latest headlines from The Hindu...

1 . Supreme Court to hear key case on electoral bonds today
2 . PM addresses G20 meeting on climate change
3 . New Parliament session likely to begin next week
4 . Government issues new digital privacy guidelines
5 . Heavy rains predicted in Southern states
```

---

## 🧠 Key Learnings

* Using **requests** to fetch HTML content.
* Parsing and **navigating DOM elements** using BeautifulSoup.
* Extracting text from anchor (`<a>`) tags.
* Writing a **clean and robust CLI script**.

---

## 🚀 Possible Improvements

* Include headline URLs for direct reading.
* Scrape multiple sections (e.g., international, sports).
* Export results to **JSON** or **CSV** for later use.
* Add **desktop notifications** for breaking news.

---
