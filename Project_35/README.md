# 📊 Project_35: Portfolio Tracker CLI

> **Author:** Pinaka
> **Type:** CLI Application
> **Domain:** Finance / Stock Market
> **Level:** Intermediate–Advanced

---

## 🚀 Overview

**Portfolio Tracker CLI** is a command-line application that helps users **track Indian stock investments live**.

It allows you to:

* Add/remove stocks
* Fetch **live market prices**
* Calculate **profit/loss (P/L)**
* View portfolio with **auto-refresh**

This project reflects **real-world retail portfolio tracking logic**, similar to what broker apps do internally.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Rich](https://img.shields.io/badge/Rich-CLI%20UI-green?style=flat-square)
![yFinance](https://img.shields.io/badge/yFinance-Market%20Data-orange?style=flat-square)
![Finance](https://img.shields.io/badge/Finance-Stock%20Market-success?style=flat-square)
![CLI](https://img.shields.io/badge/CLI-Terminal-black?style=flat-square)

---

## 📂 Project Files

```
Project_35/
├── main.py
├── portfolio.json
└── README.md
```

* `portfolio.json` → stores your holdings locally
* No database required
* Fully offline storage + online price fetch

---

## ✨ Features

* 📈 Track Indian stocks (NSE)
* 🔄 Live price updates (every 2 minutes)
* 💾 Persistent portfolio storage
* ➕ Add stocks
* ➖ Remove stocks
* 💰 Real-time Profit/Loss calculation
* 🧠 Clean financial logic
* 🖥️ Beautiful terminal UI

---

## 📦 Requirements

Create **`requirements.txt`**

```
rich
yfinance
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎮 Menu Options

| Option | Action                |
| ------ | --------------------- |
| 1      | Add Stock             |
| 2      | Remove Stock          |
| 3      | View Portfolio (Live) |
| 4      | Exit                  |

---

## 📥 Adding a Stock

Example:

```
Symbol: TCS.NS
Quantity: 10
Buy Price: 3500
```

📌 Uses **NSE symbols** (`.NS` required)

---

## 📊 Live Portfolio View

* Fetches **real-time prices**
* Auto-refresh every **2 minutes**
* Displays:

  * Buy price
  * Current price
  * Individual P/L
  * Total portfolio P/L

Stop live view with:

```
Ctrl + C
```

---

## 🧠 Financial Logic Explained

### Profit / Loss Formula

```
P/L = (Current Price - Buy Price) × Quantity
```

* Green → Profit
* Red → Loss

This is **exactly how brokers calculate unrealized P/L**.

---

## ⚠️ Notes & Limitations

* Uses free Yahoo Finance data
* Short-term price delay possible
* Internet required for live prices
* Not suitable for high-frequency trading

---

## 🧠 Learning Outcomes

* Financial data handling
* Live market polling
* Persistent local storage
* CLI UX design
* Stock symbol standards (NSE)
* Clean business logic separation

---
