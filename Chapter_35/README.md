# 📘 Chapter_35: Advanced CLI with `argparse` & `click`

**Author: Pinaka**

---

## 🎯 Why This Chapter Matters

Till now, your CLI programs mostly used:

* `input()`
* menus
* infinite loops

That’s **interactive CLI**.

Now we move to **professional CLI tools** — like `git`, `pip`, `docker`.

These tools work like:

```bash
python app.py --add --name Rakesh --age 22
```

This chapter teaches:

* how real-world CLIs are designed
* how to read arguments from terminal
* how to build clean, scalable CLI tools

---

## 🧠 CLI Vibe Shift

### Old mindset

> “Ask user again and again”

### New mindset

> “User gives everything in one command”

This is **automation-friendly**, **scriptable**, and **industry-standard**.

---

# 🟢 Part 1: `argparse` (Standard Library)

`argparse` comes **built-in with Python**.
No installation needed.

---

## 🧩 Basic Structure of argparse

### 🧠 Vibe

> “Define what arguments I accept, then parse them”

---

### 🧾 Skeleton

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()

print(args.name)
```

---

### ▶ Run

```bash
python app.py --name Rakesh
```

---

## 🟢 Example 1: Greeting CLI

### 🧾 Code

```python
from argparse import ArgumentParser

parser = ArgumentParser(description="Greeting CLI")
parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int)

args = parser.parse_args()

print(f"Hello {args.name}")
if args.age:
    print(f"You are {args.age} years old")
```

---

### ▶ Run

```bash
python greet.py --name Pinaka --age 25
```

---

## 🟢 Example 2: Flag Arguments

### 🧠 Vibe

> “Option ON or OFF”

---

### 🧾 Code

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--debug", action="store_true")

args = parser.parse_args()

if args.debug:
    print("Debug mode ON")
else:
    print("Normal mode")
```

---

### ▶ Run

```bash
python app.py --debug
```

---

## 🟢 Example 3: CLI Calculator

### 🧾 Code

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--a", type=int, required=True)
parser.add_argument("--b", type=int, required=True)
parser.add_argument("--op", choices=["+", "-", "*", "/"], required=True)

args = parser.parse_args()

if args.op == "+":
    print(args.a + args.b)
elif args.op == "-":
    print(args.a - args.b)
elif args.op == "*":
    print(args.a * args.b)
elif args.op == "/":
    print(args.a / args.b)
```

---

### ▶ Run

```bash
python calc.py --a 10 --b 5 --op *
```

---

## 🔴 When to Use argparse

✅ System scripts
✅ Dev tools
✅ Automation
✅ Backend utilities
❌ Fancy UX

---

# 🔵 Part 2: `click` (Modern & Clean)

`click` is **external**, but very powerful and clean.

---

## 📦 Install click

```bash
pip install click
```

---

## 🧠 click Philosophy

> “Functions become commands”

No manual parsing.
No boilerplate.

---

## 🟢 Example 1: Hello CLI

### 🧾 Code

```python
import click

@click.command()
@click.option("--name", prompt="Your name")
def hello(name):
    click.echo(f"Hello {name}")

hello()
```

---

### ▶ Run

```bash
python app.py --name Pinaka
```

or

```bash
python app.py
```

(click will ask interactively)

---

## 🟢 Example 2: CLI Calculator with click

```python
import click

@click.command()
@click.option("--a", type=int)
@click.option("--b", type=int)
@click.option("--op", type=click.Choice(["+", "-", "*", "/"]))
def calc(a, b, op):
    if op == "+":
        click.echo(a + b)
    elif op == "-":
        click.echo(a - b)
    elif op == "*":
        click.echo(a * b)
    elif op == "/":
        click.echo(a / b)

calc()
```

---

## 🟢 Example 3: Multiple Commands (Real Tool Style)

```python
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
def add(name):
    click.echo(f"Added {name}")

@cli.command()
def list():
    click.echo("Listing items")

cli()
```

---

### ▶ Run

```bash
python app.py add apple
python app.py list
```

---

## 🧠 argparse vs click (Clear Difference)

| Feature         | argparse | click     |
| --------------- | -------- | --------- |
| Built-in        | ✅        | ❌         |
| Boilerplate     | More     | Very less |
| Readability     | Medium   | High      |
| Prompt support  | ❌        | ✅         |
| Nested commands | Hard     | Easy      |
| Industry usage  | High     | Very High |

---

## 🧪 Practice Challenges (Must Do)

### 🟡 Challenge 1 (argparse)

Build a CLI:

```
--add income
--amount 500
--source salary
```

---

### 🟡 Challenge 2 (click)

Build a CLI:

```
python todo.py add "Buy milk"
python todo.py list
```

---

### 🔴 Challenge 3 (Real-world)

Convert one of your old menu-based CLIs into:

* argparse version OR
* click version

👉 Suggested:

* Expense Manager
* Email Sender
* File Tool

---

