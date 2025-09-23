# 📘 Chapter 27 – Git & GitHub Basics

Git and GitHub help you **track code history**, **collaborate with others**, and **publish projects** online.

---

## 🔹 What is Git?
- A **version control system** → tracks changes in code
- Allows you to **undo mistakes**, **work with multiple versions**

## 🔹 What is GitHub?
- A **cloud service** for hosting Git repositories
- Provides **collaboration, issue tracking, pull requests, CI/CD**

---

## 🔹 GitHub Desktop Basics
### 1. Clone a Repository
- Open **GitHub Desktop** → File → Clone Repository
- Paste repo link (e.g., `https://github.com/user/repo.git`)
- Choose a local folder → **Clone**

### 2. Make Changes
- Edit files in your local editor (VS Code, etc.)
- GitHub Desktop will show changes under **Changes**

### 3. Commit & Push
- Write a commit message → Click **Commit to main**
- Click **Push origin** → Uploads changes to GitHub

### 4. Pull Changes
- If someone else updated repo → Click **Fetch origin** → **Pull**

---

## 🔹 Visual Diagram
```

Local PC  <---clone---  GitHub Cloud Repo
↑                         ↓
commit + push         fetch + pull

```

---

## 🧠 Summary
- **Clone** = Download repo  
- **Commit** = Save snapshot of code  
- **Push** = Upload changes to GitHub  
- **Pull** = Download latest changes
