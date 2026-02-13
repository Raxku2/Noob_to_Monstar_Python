from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.live import Live
import os
import time


load_dotenv()
console = Console()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["transactions"]


def animate_welcome():
    colors = ["red", "orange1", "yellow", "green", "cyan", "blue", "magenta"]

    title_text = "💸 FINANCE TRACKER CLI"
    subtitle_text = "Track your Income • Expense • Savings"

    with Live(console=console, refresh_per_second=10, screen=True) as live:
        for _ in range(2):
            for color in colors:
                title = Text(title_text, justify="center", style=f"bold {color}")
                subtitle = Text(subtitle_text, justify="center", style="white")

                panel = Panel(
                    Align.center(title + "\n\n" + subtitle),
                    title=f"[bold {color}]WELCOME[/bold {color}]",
                    border_style=color,
                    padding=(2, 6),
                )

                live.update(panel)
                time.sleep(0.12)

    time.sleep(0.5)


def add_income():
    console.clear()

    console.print("[bold cyan]➕ Add Income[/bold cyan]\n")

    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    data = {
        "type": "income",
        "amount": amount,
        "category": category,
        "note": note,
        "created_at": datetime.now(),
    }

    collection.insert_one(data)
    console.print("\n[green]✅ Income added successfully[/green]")
    input("\nPress Enter to return to menu...")


def add_expense():
    console.clear()

    console.print("[bold red]➖ Add Expense[/bold red]\n")

    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    data = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "note": note,
        "created_at": datetime.now(),
    }

    collection.insert_one(data)
    console.print("\n[green]✅ Expense added successfully[/green]")
    input("\nPress Enter to return to menu...")


def view_transactions():
    console.clear()

    transactions = list(collection.find())

    if not transactions:
        console.print(
            Panel(
                "No transactions found",
                title="Transactions",
                style="red",
            )
        )
        input("\nPress Enter to return to menu...")
        return

    table = Table(
        title="📊 All Transactions",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Type", style="bold", width=10)
    table.add_column("Amount (₹)", justify="right", width=12)
    table.add_column("Category", style="cyan", width=14)
    table.add_column("Note", style="white")
    table.add_column("Date", style="dim", width=12)

    for t in transactions:
        tx_type = t.get("type", "").upper()
        amount = float(t.get("amount", 0))
        category = t.get("category", "-")
        note = t.get("note", "-")

        created_at = t.get("created_at")
        date_str = (
            created_at.strftime("%Y-%m-%d") if isinstance(created_at, datetime) else "-"
        )

        # color logic
        if tx_type == "INCOME":
            type_text = "[green]INCOME[/green]"
        else:
            type_text = "[red]EXPENSE[/red]"

        table.add_row(
            type_text,
            f"{amount:.2f}",
            category,
            note,
            date_str,
        )

    console.print(table)
    input("\nPress Enter to return to menu...")


def monthly_summary():
    console.clear()

    now = datetime.now()
    current_month = now.strftime("%Y-%m")
    month_title = now.strftime("%B %Y")

    total_income = 0.0
    total_expense = 0.0
    count = 0

    for t in collection.find():
        created_at = t.get("created_at")
        if not isinstance(created_at, datetime):
            continue

        if created_at.strftime("%Y-%m") != current_month:
            continue

        amount = float(t.get("amount", 0))
        if t.get("type") == "income":
            total_income += amount
            count += 1
        elif t.get("type") == "expense":
            total_expense += amount
            count += 1

    if count == 0:
        console.print(
            Panel(
                f"No transactions found for {month_title}",
                title="📅 Monthly Summary",
                style="yellow",
            )
        )
        input("\nPress Enter to return to menu...")
        return

    savings = total_income - total_expense

    table = Table(
        title=f"📅 Monthly Summary — {month_title}",
        header_style="bold cyan",
    )
    table.add_column("Type", style="bold")
    table.add_column("Amount (₹)", justify="right")

    table.add_row("Total Income", f"[green]{total_income:.2f}[/green]")
    table.add_row("Total Expense", f"[red]{total_expense:.2f}[/red]")
    table.add_row(
        "Savings",
        (
            f"[green]{savings:.2f}[/green]"
            if savings >= 0
            else f"[red]{savings:.2f}[/red]"
        ),
    )

    console.print(table)
    input("\nPress Enter to return to menu...")


def check_balance():
    console.clear()

    total_income = 0.0
    total_expense = 0.0
    count = 0

    transactions = collection.find()

    for t in transactions:
        if "type" not in t or "amount" not in t:
            continue

        amount = float(t["amount"])

        if t["type"] == "income":
            total_income += amount
            count += 1
        elif t["type"] == "expense":
            total_expense += amount
            count += 1

    if count == 0:
        console.print(
            Panel("No transactions found", title="Balance Summary", style="red")
        )
        return

    balance = total_income - total_expense

    table = Table(
        title="💰 Balance Summary", show_header=True, header_style="bold cyan"
    )
    table.add_column("Type", style="bold")
    table.add_column("Amount (₹)", justify="right")

    table.add_row("Total Income", f"{total_income:.2f}")
    table.add_row("Total Expense", f"{total_expense:.2f}")

    if balance > 0:
        table.add_row("Balance", f"[green]{balance:.2f} (Saving)[/green]")
    elif balance < 0:
        table.add_row("Balance", f"[red]{balance:.2f} (Loss)[/red]")
    else:
        table.add_row("Balance", f"[yellow]0.00 (Break-even)[/yellow]")

    console.print(table)
    input("\nPress Enter to return to menu...")


def show_menu():
    console.clear()

    header = Text("📋 MAIN MENU", justify="center", style="bold cyan")

    menu_table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
    )

    menu_table.add_column("Option", style="bold yellow", width=6)
    menu_table.add_column("Action", style="bold white")

    menu_table.add_row("1️⃣", "Add Income")
    menu_table.add_row("2️⃣", "Add Expense")
    menu_table.add_row("3️⃣", "View Transactions")
    menu_table.add_row("4️⃣", "Monthly Summary")
    menu_table.add_row("5️⃣", "Check Balance")
    menu_table.add_row("0️⃣", "Exit")

    panel = Panel(
        Align.center(menu_table),
        title="💸 Finance Tracker",
        border_style="cyan",
        padding=(1, 4),
    )

    console.print(header)
    console.print(panel)


def main():
    print(">>> MAIN STARTED <<<")
    animate_welcome()

    while True:
        show_menu()
        choice = console.input("\n[bold cyan]👉 Choose an option:[/bold cyan] ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            check_balance()
        elif choice == "0":
            console.print("\n[bold green]👋 Goodbye! Thank you [/bold green]")
            break


if __name__ == "__main__":
    main()


# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os

# print(">>> FILE STARTED <<<")

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("DB_NAME")

# print("MONGO_URI:", "FOUND" if MONGO_URI else "NOT FOUND")
# print("DB_NAME:", DB_NAME)

# if not MONGO_URI:
#     raise ValueError("❌ MONGO_URI missing in .env")

# if not DB_NAME:
#     raise ValueError("❌ DB_NAME missing in .env")

# try:
#     client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
#     print(">>> MongoClient created <<<")

#     client.admin.command("ping")
#     print(">>> MongoDB CONNECTED SUCCESSFULLY <<<")

#     db = client[DB_NAME]
#     collection = db["transactions"]

#     print(">>> Database & Collection READY <<<")

# except Exception as e:
#     print("❌ MongoDB connection failed")
#     print(e)
