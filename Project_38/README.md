# 📥 Project_38: YouTube Downloader CLI

> **Author:** Pinaka
> **Purpose:** Offline learning & classroom demonstration
> **Type:** CLI Utility with GUI Folder Picker
> **Domain:** Media Download Automation

---

## 🚀 Overview

This project demonstrates how to build a **simple YouTube video downloader** using Python.
The application:

* Takes a **YouTube video URL** from the user
* Opens a **GUI folder selector** for download location
* Downloads the **best available quality** video automatically
* Saves the file using the video title as filename

⚠️ **Important:**
This project is intended **strictly for educational purposes** (offline classes, learning automation, understanding third-party libraries).

---

## 🛠️ Technologies Used

* **Python 3**
* **yt-dlp** (YouTube download engine)
* **tkinter** (GUI folder picker)
* **OS Path utilities**

---

## 📂 Project Behavior (No Code Exposure)

```
User enters YouTube URL
        ↓
GUI opens to select download folder
        ↓
yt-dlp fetches best quality stream
        ↓
Video downloaded with title as filename
```

---

## 📦 Installation Guide

### 1️⃣ Install Python

Ensure Python **3.9 or higher** is installed.

Check version:

```bash
python --version
```

or

```bash
python3 --version
```

---

### 2️⃣ Install Required Dependency

Install **yt-dlp** using pip:

```bash
pip install yt-dlp
```

If pip is not available:

```bash
python -m pip install yt-dlp
```

---

### 3️⃣ Verify tkinter Availability

`tkinter` comes **pre-installed** with standard Python distributions.

To verify:

```bash
python -c "import tkinter"
```

If no error appears → ✔ Ready

---

## ▶️ How to Run (Offline / Classroom)

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the script:

```bash
python main.py
```

---

## 🧑‍💻 Usage Instructions

1. **Paste YouTube Video URL** when prompted
2. A **folder selection window** will open
3. Choose where the video should be saved
4. The video downloads automatically
5. Terminal shows **“Download completed!”** on success

---

## 📁 Output File Format

* Filename → YouTube video title
* Extension → auto-selected (`.mp4`, `.webm`, etc.)
* Quality → **Best available**

Example:

```
My Favorite Song.mp4
```

---

## ⚠️ Important Notes (Teaching Context)

* Internet connection required
* Download speed depends on network
* Some videos may be unavailable due to region or restrictions
* Private / age-restricted videos may fail
* GUI folder picker may not work on headless servers

---

## 📚 Learning Outcomes

Students will understand:

* Using third-party Python libraries
* Automating media downloads
* Handling user input safely
* Combining CLI + GUI workflows
* File path templating
* Real-world Python scripting

---

## ❗ Legal & Ethical Disclaimer

This project is for **educational use only**.

Downloading copyrighted content may violate:

* YouTube Terms of Service
* Local copyright laws

**Always use responsibly and ethically.**

---
