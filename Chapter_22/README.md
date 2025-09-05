# Chapter 22 – Working with Public APIs

In this chapter, you will learn how to **interact with public APIs** to retrieve data in JSON format and use it in your programs.  

Public APIs are one of the most powerful tools for developers — they allow you to access weather data, cryptocurrency prices, news headlines, space information, and more.

---

## 📚 Learning Objectives
- Understand what an API is and how to use it.
- Learn about **REST APIs** and HTTP verbs (GET, POST).
- Make GET requests to popular free APIs.
- Parse JSON responses.
- Handle errors and rate limits.
- Build a mini project to fetch and display data.

---

## 🛠️ Tech Stack Used
- ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
- ![Requests](https://img.shields.io/badge/Requests-API%20Calls-green)
- ![JSON](https://img.shields.io/badge/JSON-Data%20Format-orange)

---

## 🖼️ Process Flow (ASCII Diagram)

```text
┌──────────────┐
│  Public API  │
└──────┬───────┘
       │ requests.get()
       ▼
┌──────────────┐
│ JSON Response│
└──────┬───────┘
       │ Parse with .json()
       ▼
┌──────────────┐
│   Program    │
│  Displays or │
│  Processes   │
│    Data      │
└──────────────┘
````

---

## 🌎 Examples of Public APIs

* **Weather** → `https://api.weatherapi.com/v1/current.json`
* **Crypto** → `https://api.coindesk.com/v1/bpi/currentprice.json`
* **NASA** → `https://api.nasa.gov/planetary/apod`
* **Joke API** → `https://official-joke-api.appspot.com/jokes/random`

---

## 💡 Professional Mindset:

When working with APIs:

1. Always read the **API documentation**.
2. Check for **authentication** requirements (API keys).
3. Respect **rate limits** (don’t spam requests).
4. Validate and sanitize the data you receive.
5. Build error-handling logic for network issues.


