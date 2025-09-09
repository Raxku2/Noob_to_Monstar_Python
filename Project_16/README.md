# 🛒 Project 16 – Amazon Product Price Tracker

A **Python CLI tool** that monitors an Amazon product’s price in real-time using **Requests** + **BeautifulSoup** and sends **desktop notifications** when the price changes.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Library-Requests-green)
![BeautifulSoup](https://img.shields.io/badge/Parser-BeautifulSoup-yellow)
![notifypy](https://img.shields.io/badge/Notifications-desktop-important)

---

## ✨ Features
- 🕵️ Scrapes **Amazon product page** and extracts price + title.
- 🔔 Sends **desktop notifications** for price changes.
- 📉 Detects **price drops** & alerts user.
- 📈 Detects **price increases** as well.
- ⏳ Runs continuously with periodic checks.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_16_Amazon_Product_Price_Tracker
   ````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tracker**

   ```bash
   python price_tracker.py
   ```

---

## 🖥️ Example Usage

```bash
Enter Product Url : https://www.amazon.in/dp/B0D12345
Tracking Start for : Noise Smartwatch X2

Price : 3999
(no change)
(no change)
Price Drop Alert!! 
New Price : 3499
```

A **desktop notification** will also pop up whenever the price changes.

---

## 🧠 Key Learnings

* How to scrape **dynamic e-commerce pages**.
* How to parse HTML tags (`span#productTitle`, `span.a-price-whole`).
* Using `notifypy` to send **cross-platform desktop notifications**.
* Building a **real-world automation tool** with Python.

---

## 📄 requirements.txt

```
requests
beautifulsoup4
notifypy
```

---

## 🚀 Possible Improvements

* Save price history to **CSV or JSON**.
* Send **email or Telegram alerts** for price drops.
* Allow **multiple products tracking** at once.
* Use **headless browsers (Selenium/Playwright)** for products requiring JS rendering.

