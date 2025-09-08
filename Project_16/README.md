# 💼 Project 16 – Job Search API Tool (SerpAPI)

A **Python CLI tool** that uses [SerpAPI](https://serpapi.com/) to fetch **real-time job listings** for any role and location.  
Displays job title, company, location, and application link directly in the terminal.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Library-Requests-green)
![SerpAPI](https://img.shields.io/badge/API-SerpAPI-orange)
![dotenv](https://img.shields.io/badge/Security-dotenv-important)

---

## ✨ Features
- 🔍 Search for **real jobs** by role and location.
- 🌐 Uses **SerpAPI Google Jobs engine**.
- 📜 Displays company name, job title, and apply link.
- 🔑 Securely stores API key in `.env` file.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_16_Job_Search_API_Tool
   ````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project folder:

   ```env
   API_KEY=your_serpapi_key_here
   ```

4. **Run the program**

   ```bash
   python job_search.py
   ```

---

## 🖥️ Example Output

```bash
Enter Location: Kolkata
Enter Role: Python Developer

One job posting found at TCS, in Kolkata, for Python Developer | Apply: [{'link': 'https://apply-link.com'}]

One job posting found at Infosys, in Kolkata, for Backend Developer | Apply: [{'link': 'https://apply-link.com'}]
```

---

## 🧠 Key Learnings

* How to use **SerpAPI** to retrieve structured job data.
* How to work with `.env` files for secure API key storage.
* How to format API responses for human-friendly display.

---

## 📄 requirements.txt

```
requests
python-dotenv
```

---

## 🚀 Possible Improvements

* Add **filtering** by salary, date, or job type (remote/on-site).
* Save results to a **CSV or JSON** file for later reference.
* Add **email or Telegram notifications** for new jobs matching criteria.
