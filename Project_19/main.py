from pymongo import MongoClient
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import box
import os, sys

# ---------- Setup ----------
console = Console()
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["student_db"]
students = db["students"]

# ---------- Core Functions ----------

def add_student():
    console.print(Panel("Add New Student", style="bold green"))
    name = Prompt.ask("Enter name").strip()
    roll = Prompt.ask("Enter roll number").strip()
    course = Prompt.ask("Enter course").strip()
    year = Prompt.ask("Enter year").strip()
    email = Prompt.ask("Enter email (optional)", default="")
    
    student = {
        "name": name,
        "roll": roll,
        "course": course,
        "year": year,
        "email": email,
    }

    try:
        students.insert_one(student)
        console.print("✅ Student added successfully!", style="green")
    except Exception as e:
        console.print(f"❌ Error adding student: {e}", style="bold red")


def list_students():
    console.print(Panel("Student List", style="bold cyan"))
    all_students = list(students.find())

    if not all_students:
        console.print("No students found.", style="yellow")
        return

    table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE_HEAVY)
    table.add_column("ID", style="dim", width=10)
    table.add_column("Name")
    table.add_column("Roll")
    table.add_column("Course")
    table.add_column("Year")
    table.add_column("Email")

    for s in all_students:
        table.add_row(str(s["_id"])[:8], s.get("name", ""), s.get("roll", ""),
                      s.get("course", ""), s.get("year", ""), s.get("email", ""))

    console.print(table)


def view_student():
    roll = Prompt.ask("Enter roll number").strip()
    student = students.find_one({"roll": roll})
    if not student:
        console.print("❌ Student not found.", style="bold red")
        return

    info = "\n".join([f"[b]{k.capitalize()}[/b]: {v}" for k, v in student.items() if k != "_id"])
    console.print(Panel(info, title="Student Details", style="cyan"))


def update_student():
    roll = Prompt.ask("Enter roll number to update").strip()
    student = students.find_one({"roll": roll})
    if not student:
        console.print("❌ Student not found.", style="bold red")
        return

    console.print("Leave blank to keep current value.", style="yellow")
    name = Prompt.ask("Name", default=student.get("name", ""))
    course = Prompt.ask("Course", default=student.get("course", ""))
    year = Prompt.ask("Year", default=student.get("year", ""))
    email = Prompt.ask("Email", default=student.get("email", ""))

    students.update_one(
        {"roll": roll},
        {"$set": {"name": name, "course": course, "year": year, "email": email}}
    )
    console.print("✅ Student updated successfully!", style="green")


def delete_student():
    roll = Prompt.ask("Enter roll number to delete").strip()
    student = students.find_one({"roll": roll})
    if not student:
        console.print("❌ Student not found.", style="bold red")
        return

    confirm = Confirm.ask(f"Are you sure you want to delete {student['name']}?")
    if confirm:
        students.delete_one({"roll": roll})
        console.print("🗑️ Student deleted successfully!", style="green")
    else:
        console.print("Cancelled.", style="yellow")


# ---------- Main Menu ----------

def main_menu():
    while True:
        console.print("\n[bold white on blue] STUDENT DATABASE MENU [/bold white on blue]")
        console.print("[1] Add Student")
        console.print("[2] List Students")
        console.print("[3] View Student")
        console.print("[4] Update Student")
        console.print("[5] Delete Student")
        console.print("[0] Exit\n")

        choice = Prompt.ask("Choose an option", choices=["0", "1", "2", "3", "4", "5"])

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            view_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            console.print("Goodbye!", style="bold green")
            sys.exit(0)

        Prompt.ask("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\nExiting...", style="yellow")
        sys.exit(0)
