import zipfile
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import asyncio
import threading
import gc
import os
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

CACHE_DIR = "cache"
CACHE_FILE = os.path.join(CACHE_DIR, "last_paths.json")


class CacheManager:
    @staticmethod
    def ensure_cache():
        os.makedirs(CACHE_DIR, exist_ok=True)

    @staticmethod
    def save(data: dict):
        CacheManager.ensure_cache()
        with open(CACHE_FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load():
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        return {}


class ZipExtractor:
    def __init__(self, zip_path, extract_path):
        self.zip_path = zip_path
        self.extract_path = extract_path

    def extract(self, password=None):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            if password:
                zip_ref.extractall(
                    self.extract_path,
                    pwd=password.encode()
                )
            else:
                zip_ref.extractall(self.extract_path)


class ZipExtractorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # No main window
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def select_zip(self):
        return filedialog.askopenfilename(
            title="Select ZIP File",
            filetypes=[("ZIP Files", "*.zip")]
        )

    def select_destination(self):
        return filedialog.askdirectory(title="Select Extract Folder")

    def ask_password(self, attempt):
        return simpledialog.askstring(
            "Password Required",
            f"Attempt {attempt}/3\nEnter ZIP password:",
            show="*"
        )

    def show_warning(self, msg):
        messagebox.showwarning("Warning", msg)

    def show_info(self, msg):
        messagebox.showinfo("Success", msg)

    def run_extraction(self, zip_path, extract_path):
        async def task():
            extractor = ZipExtractor(zip_path, extract_path)

            for attempt in range(1, 4):
                try:
                    password = None
                    with zipfile.ZipFile(zip_path) as z:
                        if z.namelist() and z.getinfo(z.namelist()[0]).flag_bits & 0x1:
                            password = self.ask_password(attempt)
                            if not password:
                                raise RuntimeError("Password cancelled")

                    await asyncio.to_thread(
                        extractor.extract,
                        password
                    )

                    console.print(
                        Panel.fit(
                            Text("Extraction completed successfully 🎉", style="bold green"),
                            title="Done"
                        )
                    )
                    self.show_info("ZIP extracted successfully!")
                    return

                except RuntimeError:
                    break
                except Exception:
                    console.print(
                        Panel.fit(
                            Text(f"Wrong password (Attempt {attempt}/3)", style="bold red"),
                            title="Error"
                        )
                    )
                    if attempt == 3:
                        self.show_warning("Wrong password 3 times. Exiting.")
                        return

        self.loop.run_until_complete(task())
        gc.collect()  # Hard GC

    def start(self):
        console.print(
            Panel.fit(
                Text("🧩 Lighthearted ZIP Extractor\nFast • Safe • No Lag", style="bold cyan"),
                title="Welcome"
            )
        )

        cache = CacheManager.load()

        zip_path = self.select_zip()
        if not zip_path:
            return

        extract_path = self.select_destination()
        if not extract_path:
            return

        CacheManager.save({
            "last_zip": zip_path,
            "last_extract": extract_path
        })

        thread = threading.Thread(
            target=self.run_extraction,
            args=(zip_path, extract_path),
            daemon=True
        )
        thread.start()
        thread.join()


if __name__ == "__main__":
    app = ZipExtractorApp()
    app.start()
