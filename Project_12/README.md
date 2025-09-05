# 💱 Project 12 – Currency Converter (API)

A simple **Command-Line Currency Converter** that fetches live exchange rates from [Open Exchange Rates API](https://open.er-api.com/v6/latest/USD) and converts between any two supported currencies.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-green)
![API](https://img.shields.io/badge/Data-Live%20Exchange%20Rates-orange)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)

---

## ✨ Features
- 🌍 Fetches **real-time exchange rates** from a free API.
- 🔄 Converts between **any two currencies** supported by the API.
- 📜 Displays **all available currencies** for reference.
- ❌ Handles invalid currency codes gracefully.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_12_Currency_Converter
   ````

2. **Install dependencies**

   ```bash
   pip install requests
   ```

3. **Run the program**

   ```bash
   python currency_converter.py
   ```

---

## 🖥️ Usage Example

```bash
you can choose from :
 ['USD', 'EUR', 'GBP', 'INR', 'JPY', ...]

Value: 100
from Currency: USD
to Currency: INR

💰 100 USD = 8321.45 INR
```

---

## 🧠 Key Learnings

* How to consume a **public API** without authentication.
* How to process and store exchange rate data in Python.
* Simple arithmetic to calculate currency conversion.

---

## 🔮 Possible Improvements

* Add **GUI interface** using Tkinter.
* Cache rates locally to avoid multiple API calls.
* Allow batch conversions (convert to multiple currencies at once).

