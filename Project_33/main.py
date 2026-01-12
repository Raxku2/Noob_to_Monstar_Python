from platform import system
from os import path, listdir, environ
from rich import print
from rich.prompt import Prompt
from rich.traceback import install as tinstall
from rich.pretty import install as pinstall
from rich.table import Table
from rich.markdown import Markdown
from gc import collect
from asyncio import run, gather, create_task, sleep, to_thread

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"  # <-- suppress message
from pygame import mixer

tinstall()
pinstall()
input = Prompt.ask

mixer.init(
    frequency=96000,
    channels=2,
    buffer=4096,
)


queue: str = ""
music_folder = "/home/pnk/Music"


if system() == "Windows":
    music_folder = path.join(environ["USERPROFILE"], "Music")

elif system() == "Darwin":
    music_folder = path.join(path.expanduser("~"), "Music")

elif system() == "Linux":
    music_folder = path.join(path.expanduser("~"), "Music")

else:
    print("\n:warning: [red]Unsupported OS[/] \n")
    exit()


async def alive_player():
    global queue
    state_of_player = 0
    while mixer.music.get_busy():
        if state_of_player == 0:
            state_of_player = 1
        await sleep(1)

    while not mixer.music.get_busy():
        if state_of_player == 0:
            break
        else:
            await to_thread(print, "\n:white_circle: [red]Finished playing[/] \n")
        state_of_player = 0
        await sleep(1)


async def show() -> str:
    play_list_table = Table(
        title="Music :musical_note:",
        title_justify="left",
    )
    play_list_table.add_column("Id", style="", justify="right")
    play_list_table.add_column("Song")
    files = [f for f in listdir(music_folder) if f.lower().endswith(".mp3")]

    if not len(files):
        print(
            "\n:warning: [red]No Song found inside your Music :musical_note: folder[/] \n"
        )
        exit()

    for i, song in enumerate(files):
        play_list_table.add_row(str(i + 1), song)

    print(play_list_table)
    while True:

        song_id = await to_thread(
            input,
            f":heavy_plus_sign::musical_note: [yellow]Add Song by ID",
            default="cancel",
        )

        if song_id == "cancel":
            if not queue:
                continue
            return queue
        if song_id.isnumeric() and 0 < int(song_id) <= len(files):
            print(
                f":heavy_check_mark: [green]{files[int(song_id) - 1]}  added to the queue![/]"
            )
            return files[int(song_id) - 1]
        elif not song_id.isnumeric() and song_id == "Q":
            exit()
        elif not song_id.isnumeric():
            continue
        else:
            continue


async def play_music(filename):
    mixer.music.load(f"{music_folder}/{filename}")
    mixer.music.play()


async def controller():
    play_list: dict = {}
    state = "ls"
    global queue

    while True:
        if not state:
            state = await to_thread(
                input,
                ":arrow_right: Actions",
                choices=["p", "u", "r", "pl", "ls", "a", "Q", "h"],
                default="cancel",
            )
        match state:
            case "u":
                mixer.music.pause()
            case "r":
                mixer.music.unpause()
            case "a":
                mixer.music.stop()
            case "p":
                create_task(play_music(queue))

                await to_thread(
                    print, f"\n:cd: [green blink ]Now Playing... [/][blue]{queue}[/] \n"
                )
            case "ls":
                queue = await show()
                if not mixer.music.get_busy():
                    create_task(play_music(queue))

                    await to_thread(
                        print,
                        f"\n:cd: [green blink ]Now Playing... [/][blue]{queue}[/] \n",
                    )
            case "pl":
                queue = await show()
                create_task(play_music(queue))
                await to_thread(
                    print,
                    f"\n:cd: [green blink ]Now Playing... [/][blue]{queue}[/] \n",
                )

            case "Q":
                mixer.music.stop()
                collect()
                exit()

            case "h":
                with open("./MANUAL.md", "r") as manual:
                    manual = Markdown(manual.read())
                    await to_thread(
                        print,
                        manual,
                    )

        state = ""


async def main():
    create_task(alive_player())
    await controller()


run(main())
