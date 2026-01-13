from rich import print
from rich.console import Console
from rich.prompt import Prompt
from tkinter import Tk
from tkinter.filedialog import askopenfile, asksaveasfilename
from pypdf import PdfReader, PdfWriter
from gc import collect


Tk().withdraw()
input = Prompt.ask

cls = Console().clear


def load_document() -> str | None:
    try:
        user_enterd_file_path = askopenfile(
            title="Select a PDF File",
            filetypes=[
                ("PDF files", "*.pdf"),
                ("PDF files", "*.PDF"),
            ],
        )
        if not user_enterd_file_path:
            return None
        file_path = user_enterd_file_path.name
    except Exception as err:
        print("[red]Error on file open : [/]\n", err)
        return
    cls()
    return file_path


def save_document(writer: PdfWriter) -> None:

    output_file_path = asksaveasfilename(
        title="Save file as",
        defaultextension=".pdf",
        filetypes=[
            ("PDF files", "*.pdf"),
            ("PDF files", "*.PDF"),
        ],
    )

    with open(output_file_path, "wb") as file:
        writer.write(file)


def get_info(document_path: str, direct_call=False) -> dict | None:
    if not document_path:
        return

    data: dict = {}
    reader = PdfReader(document_path)
    total_pages = len(reader.pages)
    data["total_pages"] = total_pages

    if direct_call:
        print(data)

    del reader, total_pages
    collect()

    return data


def doc_slice(
    document_path: str, document_info: dict, direct_call: bool = False
) -> None | PdfWriter:
    reader = PdfReader(document_path)
    writer = PdfWriter()
    print(f"[red] Selected Document has {document_info.get("total_pages")} Page")

    if (
        input(
            prompt="Do you want to slice this document", choices=["y", "n"], default="n"
        )
        == "y"
    ):
        start_page_no = int(input("Enter starting page no", default="1"))
        end_page_no = int(
            input("Enter last page no", default=f"{document_info.get("total_pages")}")
        )

        for page_no in range(start_page_no - 1, end_page_no):
            writer.add_page(reader.pages[page_no])
        del start_page_no, end_page_no
    else:
        for page_no in range(0, int(document_info.get("total_pages"))):
            writer.add_page(reader.pages[page_no])

    if direct_call:
        save_document(writer)

    del reader
    collect()
    cls()

    return writer


def main():
    while True:
        cls()
        choise = input(prompt="Choose a option", choices=["1", "2", "Q", "h"])

        match choise:
            case "1":
                print("marge")
                writer = PdfWriter()
                while True:
                    cls()
                    file_path = load_document()
                    file_info = get_info(file_path)
                    document_now = doc_slice(
                        document_path=file_path, document_info=file_info
                    )

                    for page in document_now.pages:
                        writer.add_page(page)

                    if (
                        input("Add anothor document", choices=["y", "n"], default="n")
                        == "n"
                    ):
                        break

                save_document(writer)

            case "2":

                cls()
                print("Choper")
                file_path = load_document()
                file_info = get_info(file_path)
                doc_slice(
                    document_path=file_path, document_info=file_info, direct_call=True
                )

            case "Q":
                cls()
                exit()
            case "h":
                print("help")


main()
