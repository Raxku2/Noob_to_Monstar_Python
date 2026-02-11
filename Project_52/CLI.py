import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.prompt import Prompt
import time

console = Console()
input = Prompt.ask

API = "http://127.0.0.1:8001"

def animate_welcome():
    console.clear()
    colors = ["red", "orange1", "yellow", "green", "cyan", "blue", "violet"]

    with Live(console=console, refresh_per_second=3) as live:
        for _ in range(1):
            for color in colors:
                live.update(
                    Panel.fit(
                        f"[bold {color}]🚀 Welcome to Notes & Task Manager CLI[/]",
                        title=f"[bold {color}]WELCOME[/]",
                        border_style=color,
                        padding=(1, 2),
                    )
                )
                time.sleep(0.1)


def add_task():
    console.clear()
    console.print("\n[bold red]➕ Add New Task[/]")
    title = input("Title: ")
    description = input("Description: ")
    type_ = input("Type (task/note): ").lower()
    priority = input("Priority (Low/Medium/High)", choices=["1","2","3"], default="1")

    if priority == "1":
        priority = "LOW"
        pass
    elif priority == "2":
        priority = "MEDIUM"
        pass
    elif priority == "3":
        priority = "HIGH"
        pass
    else:
        console.print("[bold red]:warning: Something wrong[/]")



    tags = input("Tags (comma separated): ").split(",")
    due_date = input("Due Date (YYYY-MM-DD or blank): ") or None

    payload = {
        "title": title,
        "description": description,
        "type": type_,
        "priority": priority,
        "tags": tags,
        "due_date": due_date,
    }

    r = requests.post(f"{API}/add", json=payload)

    if r.status_code == 200:
        console.print(r.json()) 
    else:
        console.print("[bold red]:warning: Something wrong[/]")



def list_tasks():
    console.clear()
    console.print("\n[bold orange]📋 All Tasks[/]")
    r = requests.get(f"{API}/all")
    data = r.json()

    if data["status"] != 200:
        console.print("❌ No data found")
        return

    table = Table(title="Tasks")
    table.add_column("ID", style="red")
    table.add_column("Title")
    table.add_column("Type")
    table.add_column("Priority")
    table.add_column("Status")
    table.add_column("Due Date")

    for item in data["data"]:
        table.add_row(
            item["_id"],
            item["title"],
            item["type"],
            item["priority"],
            item["status"],
            str(item.get("due_date", "-")),
        )

    console.print(table)


def update_task():
    console.clear()
    console.print("\n[bold yellow]✏️ Update Task[/bold yellow]")
    item_id = input("Enter Task ID: ")
    status = input("New Status (Pending/Done or blank): ") or None
    
    priority = input("Priority (Low/Medium/High)", choices=["1","2","3"], default="")

    if priority == "1":
        priority = "LOW"
        pass
    elif priority == "2":
        priority = "MEDIUM"
        pass
    elif priority == "3":
        priority = "HIGH"
        pass
    else:
        priority = None


    payload = {
        "status": status,
        "priority": priority,
    }

    r = requests.put(f"{API}/update/{item_id}", json=payload)
    console.print(r.json())


def delete_task():
    console.clear()
    console.print("\n[bold red]🗑 Delete Task[/bold red]")
    item_id = input("Enter Task ID: ")
    r = requests.delete(f"{API}/delete/{item_id}")
    console.print(r.json())


def delete_all():
    console.clear()
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        r = requests.delete(f"{API}/delete-all")
        console.print(r.json())


def menu():
    while True:
        console.print(
"""
[bold green]
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Delete All
0. Exit
[/]
"""
        )

        choice = input("Choose option", choices=["1","2","3","4","5","0"])

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            delete_all()
        elif choice == "0":
            console.clear()
            console.print("👋 Bye!")
            break
        else:
            console.print("❌ Invalid choice")


if __name__ == "__main__":

    animate_welcome()
    menu()
