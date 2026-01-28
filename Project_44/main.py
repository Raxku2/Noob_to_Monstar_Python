import csv
import os
import tkinter as tk
from tkinter import filedialog

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()
def load_csv(file_path):
    """
    Load CSV file and return headers and rows
    """
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    return headers, rows


def get_csv_info(headers, rows):
    """
    Return row count, column count, and column list
    """
    data_count = len(rows)
    column_count = len(headers)

    return data_count, column_count, headers


def filter_and_sort_data(rows, column, order):
    """
    Filter and sort data based on column and order
    """
    try:
        sorted_data = sorted(
            rows,
            key=lambda x: x[column],
            reverse=True if order == "descending" else False
        )
        return sorted_data
    except KeyError:
        console.print("[red]Invalid column selected![/red]")
        return rows


def print_table(headers, rows, title="CSV Data Preview"):
    """
    Print CSV data nicely using rich
    """
    table = Table(
        title=title,
        show_lines=True,
        box=box.SIMPLE_HEAVY
    )

    for header in headers:
        table.add_column(header, style="cyan", no_wrap=True)

    for row in rows:
        table.add_row(*(str(row[h]) for h in headers))

    console.print(table)


def print_csv_summary(data_count, column_count, headers):
    """
    Print CSV metadata
    """
    console.print("\n[bold green]CSV Summary[/bold green]")
    console.print(f"📄 Rows       : {data_count}")
    console.print(f"📊 Columns    : {column_count}")

    console.print("\n[bold yellow]Available Columns[/bold yellow]")
    for idx, col in enumerate(headers, start=1):
        console.print(f"{idx}. {col}")


def save_csv(headers, rows):
    """
    Save filtered data to user selected directory
    """
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(title="Select Folder to Save CSV")
    if not folder:
        console.print("[red]Save cancelled[/red]")
        return

    file_path = os.path.join(folder, "filtered_data.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    console.print(f"[bold green]Saved successfully at:[/bold green] {file_path}")




def main():
    console.print("[bold cyan]CSV Analytics Tool[/bold cyan]\n")

    # File selection
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        console.print("[red]No file selected. Exiting...[/red]")
        return

    console.print(f"[green]Loaded file:[/green] {file_path}\n")

    # Load CSV
    headers, rows = load_csv(file_path)

    # CSV info
    data_count, column_count, headers = get_csv_info(headers, rows)
    print_csv_summary(data_count, column_count, headers)

    # User choices
    selected_column = Prompt.ask(
        "\nSelect column for comparison",
        choices=headers
    )

    order = Prompt.ask(
        "Select order",
        choices=["ascending", "descending"],
        default="ascending"
    )

    console.print(
        f"\n[bold blue]Selected Column:[/bold blue] {selected_column}"
        f"\n[bold blue]Order:[/bold blue] {order}\n"
    )

    # Filter & sort
    filtered_data = filter_and_sort_data(rows, selected_column, order)

    # Display result
    print_table(headers, filtered_data, title="Filtered & Sorted Data")

    # Save option
    save_choice = Prompt.ask(
        "\nDo you want to save the filtered data?",
        choices=["yes", "no"],
        default="no"
    )

    if save_choice == "yes":
        save_csv(headers, filtered_data)

    console.print("\n[bold green]Done ✔[/bold green]")



if __name__ == "__main__":
    main()
