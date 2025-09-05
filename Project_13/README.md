# 📊 Project 13 – GitHub Repo Stats Viewer (API)

A **Command-Line Interface (CLI)** tool that fetches live statistics about any GitHub repository using the **GitHub REST API**.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-green)
![GitHub API](https://img.shields.io/badge/API-GitHub%20REST%20API-black?logo=github)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)

---

## ✨ Features
- 🔎 Fetch live repository statistics by entering `owner/repo`
- ⭐ Shows stars, forks, watchers, and open issues count
- 📄 Displays repository description and license type
- ⏳ Shows last updated date
- 🖇️ Displays clone URL for quick access

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project_13_GitHub_Repo_Stats_Viewer
   ````

2. **Install dependencies**

   ```bash
   pip install requests
   ```

3. **Run the program**

   ```bash
   python github_repo_stats.py
   ```

---

## 🖥️ Usage Example

```bash
GitHub Repo Stats Viewer
Enter repository (owner/repo): torvalds/linux

=== GitHub Repository Stats ===
Name: linux
Owner: torvalds
Description: Linux kernel source tree
Stars ⭐: 175000
Forks 🍴: 55000
Watchers 👀: 175000
Open Issues: 350
License: GPL-2.0
Last Updated: 2025-08-17T18:22:45Z
Clone URL: https://github.com/torvalds/linux.git
==============================
```

---

## 🧠 Key Learnings

* How to use **GitHub REST API** without authentication for public repos.
* How to **parse and display JSON data** cleanly.
* How to design a **user-friendly CLI tool**.

---

## 🔮 Possible Improvements

* Support **authentication with a GitHub token** for higher rate limits.
* Add **contributor count** and **latest commit info**.
* Format output as a **table** for better readability.
* Save repo stats to a local file for future reference.

````
