# 📧 Project_41: CLI Email Sender

> **Author:** Pinaka
> **Type:** Command Line Utility
> **Purpose:** Educational / Offline Learning
> **Domain:** Networking, Automation, Python CLI Tools

---

## 🚀 Overview

**CLI Email Sender** is a Python-based command-line tool that allows you to send emails directly from the terminal using **Gmail SMTP (SSL)**.

It demonstrates:

* Secure email sending
* Environment variable handling
* Command-line arguments
* SMTP authentication
* Real-world automation use case

---

## 🧠 How It Works (High Level)

1. Loads credentials from `.env`
2. Accepts email details via CLI arguments
3. Creates an email using `EmailMessage`
4. Sends email securely via **Gmail SMTP (SSL)**

---

## 📦 Requirements

### 🔹 Python Version

* Python **3.8 or higher**

Check:

```bash
python --version
```

---

### 🔹 Required Libraries

Install dependencies:

```bash
pip install python-dotenv
```

All other modules used are **built-in**.

---

## 🔐 Gmail Setup (IMPORTANT)

Gmail **does NOT allow normal password login** for SMTP.

You **must use an App Password**.

### Step-by-step:

1. Go to **Google Account**
2. Enable **2-Step Verification**
3. Open **App Passwords**
4. Select:

   * App → Mail
   * Device → Other
5. Generate password (16 characters)

---

## 📄 Environment File (`.env`)

Create a file named `.env` in the project folder.

```env
EMAIL_API=your_gmail_app_password_here
```

⚠️ **Never share this file publicly**

---

## 🧾 Code Configuration

Inside the script:

```python
MY_EMAIL = "your_email@gmail.com"
```

Replace with **your Gmail address** (same one used for App Password).

---

## ▶️ How to Run

Run from terminal:

```bash
python main.py --to receiver@gmail.com --sb "Test Mail" --msg "Hello from CLI"
```

### Arguments Explained

| Argument | Description            |
| -------- | ---------------------- |
| `--to`   | Receiver email address |
| `--sb`   | Email subject          |
| `--msg`  | Email body message     |

All arguments are **required**.

---

## ✅ Successful Output

```text
sent
```

Email will appear instantly in receiver inbox.

---

## ❌ Common Errors & Fixes

### ❌ Authentication Error

* App password incorrect
* 2FA not enabled

✅ Fix: Regenerate App Password

---

### ❌ Module Not Found

```text
ModuleNotFoundError: dotenv
```

✅ Fix:

```bash
pip install python-dotenv
```

---

### ❌ Email Not Sent

* Check internet
* Check `.env` file
* Ensure correct Gmail address

---

## 🎯 Learning Outcomes

Students learn:

* SMTP basics
* Email automation
* Secure credentials handling
* CLI tools using `argparse`
* Real-world Python automation

---

## 🔮 Real-World Use Cases

* Automated alerts
* Server notifications
* Backup status emails
* CI/CD pipeline messages
* System monitoring tools
