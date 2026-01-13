import json
import time
import yfinance as yf
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

PORTFOLIO_FILE = "portfolio.json"
REFRESH_TIME = 120  # 2 minutes

console = Console()


# ------------------ UTILITIES ------------------

def load_portfolio():
    try:
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=4)


def fetch_price(symbol):
    data = yf.download(symbol, period="1d", interval="1m", progress=False)
    if data.empty:
        return None
    return round(float(data["Close"].iloc[-1]), 2)


# ------------------ CORE FEATURES ------------------

def add_stock():
    symbol = Prompt.ask("Enter NSE stock symbol (e.g. TCS.NS)")
    qty = float(Prompt.ask("Quantity"))
    buy_price = float(Prompt.ask("Buy price"))

    portfolio = load_portfolio()
    portfolio[symbol] = {
        "quantity": qty,
        "buy_price": buy_price
    }

    save_portfolio(portfolio)
    console.print("[green]✔ Stock added successfully[/green]")


def remove_stock():
    portfolio = load_portfolio()
    symbol = Prompt.ask("Enter stock symbol to remove")

    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        console.print("[red]✖ Stock removed[/red]")
    else:
        console.print("[yellow]Stock not found[/yellow]")


def show_portfolio():
    portfolio = load_portfolio()

    table = Table(title="📈 Indian Stock Portfolio", show_lines=False)
    table.add_column("Stock", style="cyan")
    table.add_column("Qty")
    table.add_column("Buy Price")
    table.add_column("Current Price")
    table.add_column("P/L", justify="right")

    total_pl = 0

    for symbol, data in portfolio.items():
        current_price = fetch_price(symbol)

        if current_price is None:
            continue

        qty = data["quantity"]
        buy = data["buy_price"]

        pl = (current_price - buy) * qty
        total_pl += pl

        color = "green" if pl >= 0 else "red"

        table.add_row(
            symbol,
            str(qty),
            f"₹{buy}",
            f"₹{current_price}",
            f"[{color}]₹{pl:.2f}[/{color}]"
        )

    console.clear()
    console.print(table)
    console.print(f"\n💰 Total P/L: {'[green]' if total_pl >= 0 else '[red]'}₹{total_pl:.2f}")


# ------------------ MAIN LOOP ------------------

def main():
    while True:
        console.print("\n[bold cyan]📊 Portfolio Tracker[/bold cyan]")
        console.print("1. Add Stock")
        console.print("2. Remove Stock")
        console.print("3. View Portfolio (Live)")
        console.print("4. Exit")

        choice = Prompt.ask("Choose option", choices=["1", "2", "3", "4"])

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            console.print("[yellow]Auto-refresh every 2 minutes (Ctrl+C to stop)[/yellow]")
            try:
                while True:
                    show_portfolio()
                    time.sleep(REFRESH_TIME)
            except KeyboardInterrupt:
                console.print("\n[bold]Stopped live view[/bold]")
        elif choice == "4":
            break


# if __name__ == "__main__":


main()
