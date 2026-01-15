from rich.traceback import install

install()
from rich.console import Console
from rich import print
from rich.prompt import Prompt

console = Console()
input = Prompt.ask
from tkinter.filedialog import askopenfile, asksaveasfilename

from PIL import Image


def main():
    image_path = askopenfile(
        title="Open a image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.webp")],
    ).name
    img = Image.open(image_path)
    width, height = img.size
    print(f"h: {height}\nw: {width}")

    custom_height = int(input("Enter height", default=f"{height}"))
    custom_width = int(input("Enter width", default=f"{width}"))

    img = img.resize((custom_width, custom_height))

    image_save_path = asksaveasfilename(
        title="Save image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.webp")],defaultextension=".jpg",
    )
    img.save(image_save_path)

    pass


main()
