# 📊 Project_44: Data Analysis Mini Tasks (CSV Parsing & Filtering)

**Author: Pinaka**

---

## 🎯 Project Overview

This project is a **CLI-based CSV Analytics Tool** that allows users to:

* 📂 Select a CSV file
* 📊 View metadata (rows, columns)
* 🔍 Sort data by a selected column
* 💾 Save filtered results
* 🎨 View everything beautifully using `rich`

It combines:

* `csv` → CSV parsing
* `tkinter` → File selection dialog
* `rich` → Styled CLI output
* `DictReader` → Dictionary-based row access

This is a **real-world beginner data analysis tool**.

---

# 🧠 What This Project Teaches

* Reading CSV files properly
* Working with structured tabular data
* Sorting dictionaries
* Handling user input safely
* CLI UI styling
* Saving processed data
* Mini data pipeline thinking

---

# 🏗️ Project Flow (Step-by-Step Thinking)

```
1. User selects CSV file
2. Load file into memory
3. Show summary (rows + columns)
4. Ask which column to sort
5. Ask ascending/descending
6. Sort data
7. Display table
8. Ask if user wants to save
9. Save filtered data
```

Simple. Clean. Practical.

---

# 📦 Required Installation

```bash
pip install rich
```

No need to install tkinter (comes pre-installed with Python in most systems).

---

# 🔍 Code Breakdown

---

## 1️⃣ Loading CSV

```python
reader = csv.DictReader(f)
```

This converts:

```
name,age,city
John,25,Delhi
```

Into:

```python
{
  "name": "John",
  "age": "25",
  "city": "Delhi"
}
```

Each row becomes a dictionary.

✔ Clean
✔ Flexible
✔ Easy column access

---

## 2️⃣ Getting CSV Info

```python
data_count = len(rows)
column_count = len(headers)
```

Gives:

* Total rows
* Total columns
* Column names

---

## 3️⃣ Sorting Data

```python
sorted(rows, key=lambda x: x[column])
```

This sorts rows based on selected column.

⚠ Important:

Right now sorting is **string-based**.

If numbers exist:

```
1, 10, 2
```

It sorts like:

```
1, 10, 2
```

Not numerically.

---

### 🚀 Improvement (Optional Upgrade)

For numeric sorting:

```python
key=lambda x: float(x[column]) if x[column].replace('.', '', 1).isdigit() else x[column]
```

This makes sorting smarter.

---

## 4️⃣ Printing Table with Rich

```python
table = Table(
    title=title,
    show_lines=True,
    box=box.SIMPLE_HEAVY
)
```

This makes your CLI look professional.

Each column:

```python
table.add_column(header, style="cyan")
```

Each row:

```python
table.add_row(*(str(row[h]) for h in headers))
```

Beautiful output. No manual formatting needed.

---

## 5️⃣ Saving Filtered Data

Uses:

```python
csv.DictWriter
```

Preserves structure and headers.

Automatically creates:

```
filtered_data.csv
```

inside selected folder.

---

# 💡 Mini Data Analysis Tasks You Can Practice

Try modifying this tool to:

---

### 🟢 Task 1: Filter by Value

Add feature:

* Show rows where `city == Delhi`

---

### 🟢 Task 2: Top 5 Rows Only

After sorting:

```python
filtered_data = filtered_data[:5]
```

---

### 🟢 Task 3: Column Statistics

Add:

* Min value
* Max value
* Average

For numeric columns.

---

### 🟢 Task 4: Multi-Column Sort

Sort by:

* age
* then name

---

### 🟢 Task 5: Search Feature

Ask user:

```
Enter keyword:
```

Return rows containing that word.

---

# 🧪 Real-World Applications

This logic applies to:

* Sales reports
* Student marksheets
* Expense tracking
* Log filtering
* Stock price CSV
* Survey results
* HR records

This is how basic data tools are built.

---

# ⚠ Limitations of Current Version

* Loads entire file into memory
* No numeric detection
* No filtering condition (only sorting)
* No large file optimization

But for beginner → intermediate level, this is excellent.

---

# 🏆 Skill Level

| Skill               | Level             |
| ------------------- | ----------------- |
| CSV Parsing         | Beginner+         |
| Sorting             | Intermediate      |
| CLI Styling         | Intermediate      |
| Data Handling       | Intermediate      |
| Real-World Thinking | Advanced Beginner |

---

# 🧠 Problem-Solving Prompts for This Project

Ask yourself:

* What is the structure of CSV internally?
* Why use DictReader over reader?
* Why convert everything to string before printing?
* What happens if column doesn’t exist?
* What if file is empty?
* What if column contains mixed data types?

These are real engineer questions.

---
