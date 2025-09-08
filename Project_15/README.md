# 💼 Project 15 – Job Listings Scraper (SerpAPI + CSV)

A Python CLI tool that fetches **real-time job listings** from [SerpAPI Google Jobs Engine](https://serpapi.com/google-jobs-api) and **saves them to a CSV file** for offline reference.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Library-Requests-green)
![dotenv](https://img.shields.io/badge/Security-dotenv-important)
![CSV](https://img.shields.io/badge/Output-CSV%20File-orange)

---

## ✨ Features
- 🔍 Fetch job listings by **role** and **location**.
- 💾 Saves results to a **jobs.csv** file.
- 🧹 Clean and well-formatted CLI output.
- 🔑 API key stored securely in `.env` file.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_15_Job_Listings_Scraper
   ````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**

   ```env
   API_KEY=your_serpapi_key_here
   ```

4. **Run the scraper**

   ```bash
   python job_scraper.py
   ```

---

## 🖥️ Example Output

```bash
Enter Location: Kolkata
Enter Role: Python Developer

One job posting found at TCS, in Kolkata, for Python Developer | Apply: [{'link': 'https://apply-link.com'}]

One job posting found at Infosys, in Kolkata, for Backend Developer | Apply: [{'link': 'https://apply-link.com'}]
```

And a file `jobs.csv` will be created like:

```csv
company_name,location,title,apply_options
TCS,Kolkata,Python Developer,"[{'link': 'https://apply-link.com'}]"
Infosys,Kolkata,Backend Developer,"[{'link': 'https://apply-link.com'}]"
```

---

## 🧠 Key Learnings

* How to work with **SerpAPI** and process API responses.
* Writing job data to **CSV files** using Python.
* Managing **API keys** securely with `dotenv`.

---

## 📄 requirements.txt

```
requests
python-dotenv
```

---

## 🚀 Possible Improvements

* Add support for **multiple pages** of job results.
* Allow user to **filter by remote/onsite jobs**.
* Schedule periodic runs and **send notifications** for new job postings.
