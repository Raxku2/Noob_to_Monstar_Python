from rich import print
from rich.traceback import install
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime
from pymongo import MongoClient

# from json import dump, load
# from os import path, makedirs
# from gc import collect

install()
input = Prompt.ask

MONGO_URI = "m"
client = MongoClient(MONGO_URI)
db = client["db"]
coll = db["collection"]


# def init_doc():
#     db_dir = path.expanduser("~/Documents/Expenses")

#     makedirs(db_dir, exist_ok=True)

#     if not path.exists(path.join(db_dir, "Data.json")):

#         with open(path.join(db_dir, "Data.json"), "w") as file:
#             dump({"income": [], "expenses": []}, file)

#     del db_dir
#     collect()


# def load_doc() -> dict:
#     db_dir = path.expanduser("~/Documents/Expenses")

#     with open(path.join(db_dir, "Data.json"), "r") as file:
#         return load(file)


# def save_doc(data):
#     db_dir = path.expanduser("~/Documents/Expenses")

#     with open(path.join(db_dir, "Data.json"), "w") as file:
#         dump(data, file, indent=4)


def add_income():
    amount = float(input("[white bold on blue] Enter income amount [/]"))
    source = input("[white bold on blue] Enter income Source [/]")

    # data = load_doc()
    # data["income"].append(
    #     {"amount": amount, "source": source, "date": str(datetime.now().date())}
    # )
    # save_doc(data)

    status = coll.insert_one(
        {
            "type": "i",
            "amount": amount,
            "source": source,
            "date": str(datetime.now().date()),
        }
    )

    if status.acknowledged:
        print("[white bold on green] Income added sucessfully [/]")
    else:
        print("[red] Fail to add Income  [/]")


def add_expense():
    amount = float(input("[white bold on blue] Enter expense amount [/]"))
    category = input("[white bold on blue] Enter category (Food/Travel/etc) [/]")
    note = input("[white bold on green] Enter note [/]") or "No note added"

    # data = load_doc()
    # data["expenses"].append(
    #     {"amount": amount, "category": category,"note":note, "date": str(datetime.now().date())}
    # )
    # save_doc(data)
    status = coll.insert_one(
        {
            "type": "e",
            "amount": amount,
            "source": category,
            "note": note,
            "date": str(datetime.now().date()),
        }
    )
    if status.acknowledged:
        print("[white bold on green] expense added sucessfully [/]")
    else:
        print("[red] Fail to add expense  [/]")


def view_balance():

    get_income_doc = coll.find({"type": "i"}, {"amount": 1, "_id": 0})
    get_expense_doc = coll.find({"type": "e"}, {"amount": 1, "_id": 0})

    total_income = 0
    total_expenses = 0

    for amount in get_expense_doc:
        total_expenses += float(amount.get("amount"))

    for amount in get_income_doc:
        total_income += float(amount.get("amount"))

    balance = total_income - total_expenses
    print(f"[bold green ] Total Income: ₹{total_income} [/]")
    print(f"[red bold] Total Expense: ₹{total_expenses} [/]")
    print(f"[yellow bold] Balance: {balance} [/]")


def view_expenses():
    #     data = load_doc()
    summary = {}
    data = list(coll.find({"type": "e"}, {"_id": 0}))
    for e in data:
        summary[e["source"]] = summary.get(e["source"], 0) + e["amount"]

    summery_table = Table(title="Expense Summary")

    summery_table.add_column("Catagory")
    summery_table.add_column("Amount")

    for cat, amt in summary.items():
        summery_table.add_row(str(cat), str(amt))

    print(summery_table)


def main():
    # init_doc()

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

        choice = input("Choose an option", default="5", choices=["1", "2", "3", "4"])

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
