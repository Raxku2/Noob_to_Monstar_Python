
# Chapter 21 – Web Scraping with BeautifulSoup & API Discovery

In this chapter, you will learn **how to extract data from websites** using `BeautifulSoup`, and how to take a professional approach by **checking for available APIs** before scraping raw HTML.

---

## 📚 Learning Objectives
- Understand what web scraping is and where to use it.
- Learn to parse HTML with `BeautifulSoup`.
- Learn to inspect websites and find hidden APIs.
- Use `requests` to fetch data from API endpoints.
- Build a **real-world notifier program** based on MAKAUT notices.

---

## 🛠️ Tech Stack Used
- ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
- ![Requests](https://img.shields.io/badge/Requests-API%20Calls-green)
- ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-yellow)
- ![dotenv](https://img.shields.io/badge/DotEnv-Env%20Vars-orange)
- ![notifypy](https://img.shields.io/badge/Notifypy-Desktop%20Notification-purple)

---

## 🖼️ Process Flow (ASCII Diagram)

```text
┌────────────┐
│   API/HTML │
└─────┬──────┘
      │ requests.get()
      ▼
┌────────────┐
│   Program  │
└─────┬──────┘
      │ Parse JSON or HTML
      ▼
┌──────────────┐
│ Compare Data │ ← Last notice stored in file
└─────┬────────┘
      │
      ├──▶ No change → Sleep → Repeat
      │
      ▼
┌─────────────────────┐
│ Show Notification   │
│ Print Latest Notices│
│ Save New Notice     │
└─────────────────────┘
````

---

## 💡 Professional Mindset:

When solving real-world problems:

1. **Inspect the website** (Check Elements → Network Tab).
2. Look for **hidden API endpoints** to avoid brittle HTML scraping.
3. Always **save state** (last notice, last price, last update).
4. **Notify** the user when something new happens.
5. Make it **repeatable** with loops or schedulers.

---

