# 📄 Project_36: PDF Merger CLI

> **Author:** Pinaka
> **Type:** CLI + Minimal GUI Tool
> **Domain:** Document Automation
> **Level:** Intermediate

---

## 🚀 Overview

**PDF Merger CLI** is a powerful command-line based PDF utility that allows users to:

* Merge multiple PDF files
* Slice (extract specific page ranges)
* Save output using a file-save dialog

Although primarily a **CLI application**, it smartly uses **GUI file dialogs** for file selection to improve user experience.

This project reflects how **real desktop utilities** are designed — CLI logic with GUI assistance.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Rich](https://img.shields.io/badge/Rich-CLI%20UI-green?style=flat-square)
![PyPDF](https://img.shields.io/badge/PyPDF-PDF%20Processing-orange?style=flat-square)
![Tkinter](https://img.shields.io/badge/Tkinter-File%20Dialog-lightgrey?style=flat-square)
![CLI Tool](https://img.shields.io/badge/CLI-Utility-black?style=flat-square)

---

## 📂 Project Files

```
Project_36/
├── main.py
└── README.md
```

No database
No config files
Pure local execution

---

## ✨ Features

* 📎 Merge multiple PDF files
* ✂ Slice (extract) specific page ranges
* 📂 GUI-based file picker (no typing paths)
* 💾 GUI save dialog for output file
* 📊 Shows total page count
* 🧠 Memory-efficient processing
* 🖥️ Clean terminal UI with Rich

---

## 📦 Requirements

Create **`requirements.txt`**

```
rich
pypdf
```

> `tkinter` comes pre-installed with Python (Windows/macOS/Linux)

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

## 🎮 Menu Options

| Option | Action            |
| ------ | ----------------- |
| `1`    | Merge PDFs        |
| `2`    | Slice (Cut Pages) |
| `h`    | Help              |
| `Q`    | Exit              |

---

## 🔀 Merge PDFs (Option 1)

### Workflow:

1. Select a PDF file
2. Choose whether to slice pages or keep full document
3. Repeat for multiple PDFs
4. Save merged output

✔ Pages are appended **in selected order**

---

## ✂ Slice PDF (Option 2)

### Workflow:

1. Select a PDF file
2. View total page count
3. Enter start & end page
4. Save sliced PDF

📌 Useful for extracting chapters, assignments, notes, etc.

---

## 🧠 Internal Logic (Simplified)

```
Select PDF
   ↓
Read page count
   ↓
Slice or full copy
   ↓
Append to writer
   ↓
Save output
```

---

## ⚠️ Notes & Limitations

* Works only with **PDF files**
* No password-protected PDF support
* No preview (CLI-focused)
* GUI dialogs may not work on headless servers

---

## 🧠 Learning Outcomes

* PDF file manipulation
* Mixing CLI + GUI design
* Memory-efficient document processing
* Page-level data handling
* Real-world automation mindset

---

