from rich import print
from rich.traceback import install
from rich.prompt import Prompt
from rich.table import Table

install()
input = Prompt.ask
from json import dump, load
from os import path, makedirs
from gc import collect
from datetime import datetime


def init_doc():
    db_dir = path.expanduser("~/Documents/Expenses")

    makedirs(db_dir, exist_ok=True)

    if not path.exists(path.join(db_dir, "Data.json")):

        with open(path.join(db_dir, "Data.json"), "w") as file:
            dump({"income": [], "expenses": []}, file)

    del db_dir
    collect()


def load_doc() -> dict:
    db_dir = path.expanduser("~/Documents/Expenses")

    with open(path.join(db_dir, "Data.json"), "r") as file:
        return load(file)


def save_doc(data):
    db_dir = path.expanduser("~/Documents/Expenses")

    with open(path.join(db_dir, "Data.json"), "w") as file:
        dump(data, file, indent=4)


def add_income():
    amount = float(input("[white bold on blue] Enter income amount [/]"))
    source = input("[white bold on blue] Enter income Source [/]")

    data = load_doc()
    data["income"].append(
        {"amount": amount, "source": source, "date": str(datetime.now().date())}
    )
    save_doc(data)
    print("[white bold on green] Income added sucessfully [/]")


def add_expense():
    amount = float(input("[white bold on blue] Enter expense amount [/]"))
    category = input("[white bold on blue] Enter category (Food/Travel/etc) [/]")
    note = input("[white bold on green] Enter note [/]") or "No note added"

    data = load_doc()
    data["expenses"].append(
        {"amount": amount, "category": category,"note":note, "date": str(datetime.now().date())}
    )
    save_doc(data)
    print("[white bold on green] Income added sucessfully [/]")


def view_balance():
    data = load_doc()
    total_income = sum(i["amount"] for i in data["income"])
    total_expenses = sum(e["amount"] for e in data["expenses"])

    balance = total_income - total_expenses
    print(f"[bold green ] Total Income: ₹{total_income} [/]")
    print(f"[red bold] Total Expense: ₹{total_expenses} [/]")
    print(f"[yellow bold] Balance: {balance} [/]")


def view_expenses():
    data = load_doc()
    summary = {}
    for e in data["expenses"]:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    summery_table = Table(title="Expense Summary")

    summery_table.add_column("Catagory")
    summery_table.add_column("Amount")


    for cat, amt in summary.items():
        summery_table.add_row(str(cat),str(amt))
    
    print(summery_table)
    




def main():
    init_doc()

    # add_income()
    # add_expense()
    # view_balance()
    # view_expenses()

    while True:
        print("[green]======[blue] Budget Tracker CLI [/]======[/]")
        print("[yellow]1. Add Income[/]")
        print("[green]2. Add Expense[/]")
        print("[violet]3. View Balance[/]")
        print("[red]4. Expense Summary[/]")
        print("[blue]5. Exit[/]")

        choice = input("Choose an option",default="5",choices=["1","2","3","4"])

        match choice:
            case "1":
                add_income()
            case "2":
                add_expense()
            case "3":
                view_balance()
            case "4":
                view_expenses()
            case "5":
                exit()
        

main()
