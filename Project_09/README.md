# ⏰ Project 09: Simple Alarm Clock  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![CLI](https://img.shields.io/badge/Interface-CLI-green)]()  
[![Cross-Platform](https://img.shields.io/badge/OS-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey)]()  

---

## 📖 Overview
A **command-line Alarm Clock** built in Python.  
It allows you to set an alarm in 24-hour format (HH:MM). When the system time matches the alarm time, it plays a sound (`sound.mp3`).  

---

## ✨ Features
- ⏳ Set alarm in **24-hour format** (HH:MM).  
- 🔊 Plays audio file when alarm time is reached.  
- ❌ Option to quit alarm with `"Q"`.  
- 🖥️ CLI based – runs on Linux, Windows, and macOS.  

---

## 🛠️ Tech Stack
- **Python 3.x**  
- `datetime` → fetch system time  
- `pygame` → play alarm sound  
- `time` → sleep loop for time checking  

---

## 🚀 User Guide

### 1️⃣ Requirements
- Python 3.x installed  
- Install dependency:
```bash
pip install pygame
````

* Place an alarm sound file in the same folder as:

```
sound.mp3
```

### 2️⃣ Run the Project

```bash
python project.py
```

### 3️⃣ Example Run

```
Enter alerm time (HH:MM in 24hour format): 07:30
time chek hochhe
time chek hochhe
...
alarm bajbe
```

---

## ⚙️ Cross-Platform Notes

* Works on **Windows, Linux, macOS** (requires `pygame`).
* Ensure you have an MP3 file named **sound.mp3** in the same folder.

---

## 🧩 Future Enhancements

* Support **multiple alarms**.
* Snooze option instead of quit.
* Display **digital clock UI** with Tkinter.
* Option to select custom alarm sounds.

---

## 📂 Project Structure

```
Project_09_Simple_Alarm_Clock/
│── README.md        # Documentation
│── project.py       # Main source code
│── practice_set.md  # Challenges
│── solutions.md     # Hints/Solutions
│── sound.mp3        # Alarm sound file (user provided)
```

---

## 📜 License

This project is open-source and free to use.

