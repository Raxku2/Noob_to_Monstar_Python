# 📊 Project_39: Log Analyzer CLI

> **Author:** Pinaka
> **Type:** Command Line Tool
> **Domain:** System Monitoring / DevOps / Cybersecurity Basics
> **Purpose:** Educational & Offline Learning

---

## 🚀 Overview

The **Log Analyzer CLI** is a Python-based command-line tool that reads and analyzes system log files.

It automatically:

* Parses structured log entries
* Counts log levels (INFO, ERROR, WARNING, DEBUG)
* Tracks IP address frequency
* Extracts detailed ERROR logs
* Detects malformed (invalid) log lines
* Generates a readable summary report
* Saves a detailed report to a file

This project demonstrates **real-world log processing**, commonly used in **servers, DevOps, SOC, and backend systems**.

---

## 📂 Expected Log Format

Each log line must follow this format:

```
YYYY-MM-DD HH:MM:SS LEVEL MESSAGE IP
```

### Example:

```
2025-01-10 14:23:11 ERROR Database connection failed 192.168.1.10
2025-01-10 14:24:05 INFO User logged in 192.168.1.15
```

---

## 🛠️ Technologies Used

* **Python 3**
* `re` (Regular Expressions)
* `collections.Counter`
* `datetime`
* File handling

No third-party libraries required.

---

## 📦 Installation Guide

### 1️⃣ Install Python

Ensure Python **3.8 or higher** is installed.

Check version:

```bash
python --version
```

or

```bash
python3 --version
```

---

### 2️⃣ Prepare Log File

Create or place a log file named:

```
system.log
```

in the **same directory** as the script.

---

## ▶️ How to Run

From the project directory:

```bash
python main.py
```

(or the filename used for the script)

---

## 🧠 What the Program Does

### 🔍 Parsing Phase

* Reads log file line-by-line
* Uses **regular expressions** to extract:

  * Timestamp
  * Log level
  * Message
  * IP address
* Skips empty lines
* Counts malformed entries

---

### 📊 Analysis Phase

Tracks:

* Log level counts
* Top IP addresses
* Error details (time, IP, message)
* Malformed log lines

---

### 📄 Reporting Phase

#### Terminal Output:

* Log level summary
* Top 5 IP addresses
* Total ERROR count
* Malformed line count

#### File Output:

Creates:

```
report.txt
```

Containing:

* Log level summary
* All IP statistics
* Full ERROR log list
* Malformed line count

---

## 📁 Output Example (Terminal)

```
====== LOG ANALYSIS REPORT ======

Log Level Summary:
  INFO: 120
  ERROR: 12
  WARNING: 8

Top IP Addresses:
  192.168.1.10: 25
  192.168.1.15: 18

Total ERRORs: 12
Malformed log lines: 3
```

---

## 📄 Output File (`report.txt`)

```
LOG ANALYSIS REPORT

Log Levels:
INFO: 120
ERROR: 12
WARNING: 8

Top IPs:
192.168.1.10: 25
192.168.1.15: 18

Errors:
2025-01-10 14:23:11 | 192.168.1.10 | Database connection failed

Malformed lines: 3
```

---

## 🎯 Learning Outcomes

Students will learn:

* Log file structure
* Regex-based parsing
* Real-world file processing
* Data aggregation with `Counter`
* Error tracking & reporting
* Writing CLI analytics tools

---

## ⚠️ Important Notes

* Log file **must follow the expected format**
* Invalid lines are safely counted, not crashed
* Encoding issues are handled gracefully
* Works well for large log files

---
