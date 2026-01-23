# 🎨 Chapter_36: CLI UI Styling with `rich`

**Author: Pinaka**

---

## 🎯 Why This Chapter Matters

Until now, your CLI tools were **functional**.
Now we make them **beautiful, readable, and professional**.

Modern CLI tools like:

* `pip`
* `poetry`
* `docker`
* `rich-cli`

👉 all use **styled terminal output**.

This chapter teaches you how to:

* add colors & formatting
* show tables, progress bars
* display errors nicely
* make CLI tools feel *alive*

---

## 🧠 CLI Vibe Upgrade

### Before

```text
Total income: 5000
Total expense: 3200
Balance: 1800
```

### After

```text
✔ Total Income: ₹5000
✖ Total Expense: ₹3200
★ Balance: ₹1800
```

Same logic.
Better **UX**.

---

# 📦 Installing rich

```bash
pip install rich
```

---

## 🟢 Basic rich Setup

```python
from rich import print
```

Yes — rich **replaces print()**.

---

## 🎨 Colors & Styles

### 🧾 Syntax

```python
print("[red]Error[/]")
print("[green]Success[/]")
print("[bold blue]Important[/]")
print("[white on red]Danger[/]")
```

---

### 🧪 Example

```python
from rich import print

print("[green]✔ Task completed[/]")
print("[red]✖ Task failed[/]")
print("[yellow bold]⚠ Warning[/]")
```

---

## 🟢 Emojis (Work Everywhere)

```python
print(":rocket: Launching app")
print(":white_check_mark: Done")
print(":warning: Something went wrong")
```

---

## 🧠 Rich Styling Cheat Sheet

| Style      | Example          |
| ---------- | ---------------- |
| Color      | red, green, blue |
| Bold       | bold             |
| Background | on red           |
| Italic     | italic           |
| Blink      | blink            |
| Underline  | underline        |

---

## 📊 Tables (Very Important)

Tables are **core for CLI dashboards**.

---

### 🧾 Basic Table

```python
from rich.table import Table
from rich import print

table = Table(title="Students")

table.add_column("Name")
table.add_column("Marks")

table.add_row("Rakesh", "90")
table.add_row("Amit", "85")

print(table)
```

---

### 🧠 Where Tables Are Used

* Expense summaries
* API data
* Logs
* Reports
* Portfolio trackers

(You already used this — now you understand it deeply)

---

## ⏳ Progress Bars

### 🧾 Example

```python
from rich.progress import track
import time

for step in track(range(10), description="Processing..."):
    time.sleep(0.5)
```

---

### 🧠 Use Cases

* File uploads
* Downloads
* Data processing
* Background jobs

---

## 🖥 Console Object (Advanced Control)

```python
from rich.console import Console

console = Console()
console.print("Hello", style="bold green")
```

---

### Clear Screen

```python
console.clear()
```

Perfect for:

* dashboards
* live refresh CLIs
* menus

---

## 🚨 Tracebacks (Developer Friendly Errors)

Instead of ugly Python errors 👇
Use this:

```python
from rich.traceback import install
install()
```

Now errors are:

* colored
* readable
* highlighted

👉 **Always use this in CLI projects**

---

## 🟢 Prompt with rich

```python
from rich.prompt import Prompt

name = Prompt.ask("Enter your name")
age = Prompt.ask("Age", default="18")
```

---

### Prompt with Choices

```python
choice = Prompt.ask(
    "Choose option",
    choices=["1", "2", "3"],
    default="3"
)
```

---

## 🧠 Rich Prompt vs input()

| input()       | Prompt          |
| ------------- | --------------- |
| Plain         | Styled          |
| No validation | Validation      |
| No default    | Default support |

---

## 🧾 Status Messages

```python
from rich.console import Console
from time import sleep

console = Console()

with console.status("Loading data...", spinner="dots"):
    sleep(2)

console.print("[green]Loaded successfully[/]")
```

---

## 📄 Markdown Rendering in CLI

```python
from rich.markdown import Markdown
from rich import print

md = Markdown("""
# Welcome
- Item 1
- Item 2
""")

print(md)
```

Used in:

* help screens
* manuals
* docs inside CLI

(You used this in Music Player 👌)

---

## 🧠 Rich = UI Layer Only

Important rule:

> **rich never replaces logic**
> It only replaces how output looks

---

## 🧪 Mini Practice Tasks

### 🟡 Task 1

Make a **styled menu** using:

* colors
* emojis
* Prompt.ask

---

### 🟡 Task 2

Convert any old `print()` output into:

* colored
* bold
* table-based

---

### 🔴 Task 3 (Recommended)

Take one of your CLIs:

* Budget Tracker
* Expense Manager
* Portfolio Tracker

Add:

* tables
* colored status messages
* clean error outputs

---
