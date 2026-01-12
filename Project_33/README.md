# 🎵 Project_33: Music Player CLI

> **Author:** Pinaka
> **Type:** CLI Application
> **Level:** Intermediate
> **Platform:** Windows · Linux · macOS

---

## 🚀 Overview

**Music Player CLI** is a cross-platform **command-line based music player** written in Python.
It automatically scans your system’s **Music folder**, displays available `.mp3` files, and allows you to **play, pause, resume, stop, and queue songs** using simple keyboard commands.

This project demonstrates **real-world CLI design**, **OS detection**, and **audio playback** using Python.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Rich](https://img.shields.io/badge/Rich-CLI%20UI-green?style=flat-square)
![Pygame](https://img.shields.io/badge/Pygame-Audio-orange?style=flat-square)
![Async](https://img.shields.io/badge/AsyncIO-EventLoop-lightgrey?style=flat-square)
![Cross Platform](https://img.shields.io/badge/Cross--Platform-Windows%20|%20Linux%20|%20macOS-success?style=flat-square)

---

## 📁 Music Folder Detection

The program **automatically selects your system Music directory**:

| OS      | Music Folder            |
| ------- | ----------------------- |
| Windows | `C:\Users\<User>\Music` |
| Linux   | `/home/<user>/Music`    |
| macOS   | `/Users/<user>/Music`   |

⚠️ **Only `.mp3` files are supported**

---

## ✨ Features

* 🎧 Auto-detect system Music folder
* 📜 List all available MP3 files
* ▶️ Play music
* ⏸ Pause music
* 🔁 Resume music
* ⏹ Stop music
* ➕ Add songs to queue
* 📖 Built-in help manual
* 💻 Beautiful CLI UI using `rich`
* 🧠 Real-world CLI interaction design

---

## 📦 Requirements

Create a file named **`requirements.txt`**

```
rich
pygame
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎮 Controls & Commands

| Key  | Action                  |
| ---- | ----------------------- |
| `ls` | List songs              |
| `p`  | Play selected song      |
| `u`  | Pause                   |
| `r`  | Resume                  |
| `a`  | Stop                    |
| `pl` | Pick & play immediately |
| `h`  | Show help manual        |
| `Q`  | Quit player             |

---

## 🧭 User Flow

```
Start App
   ↓
Detect OS
   ↓
Scan Music Folder
   ↓
Show Playlist
   ↓
Select Song by ID
   ↓
Play / Pause / Resume / Stop
```

---

## 🧠 Learning Outcomes

* Cross-platform path handling
* Real CLI UX design
* Audio playback using Python
* Event-driven program flow
* Clean command handling logic
* Rich-based terminal UI

---

## 📄 Notes

* Make sure your **Music folder contains `.mp3` files**
* Large files may take a second to load
* Works offline
* No internet required

---

## 🏁 Conclusion

This project mimics a **real desktop music player**, but entirely inside the terminal.
It’s an excellent demonstration of how **Python CLI apps can feel powerful, modern, and practical**.

---
