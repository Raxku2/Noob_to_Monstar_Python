# 🖼️ Project_37: Image Resizer CLI

> **Author:** Pinaka
> **Type:** CLI + GUI Utility
> **Domain:** Image Processing
> **Level:** Beginner → Intermediate

---

## 🚀 Overview

**Image Resizer CLI** is a lightweight command-line tool that allows users to **resize images to custom dimensions** using an intuitive workflow:

* GUI file picker for selecting images
* CLI prompts for width & height
* GUI save dialog for output image

This project demonstrates **real-world desktop utility design** — minimal UI friction with maximum usability.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-orange?style=flat-square)
![Rich](https://img.shields.io/badge/Rich-CLI%20UI-green?style=flat-square)
![Tkinter](https://img.shields.io/badge/Tkinter-File%20Dialog-lightgrey?style=flat-square)
![CLI Tool](https://img.shields.io/badge/CLI-Utility-black?style=flat-square)

---

## 📂 Project Structure

```
Project_37/
├── main.py
└── README.md
```

No database
No config files
Local execution only

---

## ✨ Features

* 🖼️ Supports PNG, JPG, JPEG, BMP, WEBP
* 📂 GUI image file selector
* 📏 Displays original width & height
* ✍ User-defined resize dimensions
* 💾 GUI save dialog
* ⚡ Fast & lightweight
* 🧠 Beginner-friendly logic

---

## 📦 Requirements

Create **`requirements.txt`**

```
rich
pillow
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> `tkinter` is included with standard Python installations.

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧑‍💻 Usage Flow

### Step-by-Step

1. GUI dialog opens → select image
2. Original dimensions are displayed
3. Enter new width and height
4. GUI dialog opens → choose save location
5. Resized image is saved

---

## 🔄 Workflow Diagram

```
Select Image (GUI)
       ↓
Read Image Size
       ↓
User Inputs New Dimensions
       ↓
Resize Image
       ↓
Save Image (GUI)
```

---

## 📸 Supported Formats

* `.png`
* `.jpg`
* `.jpeg`
* `.bmp`
* `.webp`

---

## ⚠️ Notes & Limitations

* Aspect ratio is **not preserved automatically**
* No batch resizing
* No image preview
* GUI dialogs may not work on headless servers

---
