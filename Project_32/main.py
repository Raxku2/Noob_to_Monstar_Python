from requests import get
from html import unescape
from gc import collect
from rich import print
from rich.prompt import Prompt

input = Prompt.ask
from rich.traceback import install

install()
from random import shuffle


def get_questions():
    url = f"https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"

    res = get(url)
    data = res.json()
    for questions in data.get("results"):
        yield questions
    del res, data, url
    collect()


score = 0

for question in get_questions():
    # print(question)
    print(f"[bold white on red]{unescape(question.get("question"))}[/]")
    options = [opt for opt in question.get("incorrect_answers")]
    correctAns = question.get("correct_answer")
    options.append(correctAns)
    shuffle(options)

    for index, option in enumerate(options):
        print(f"[yellow] {index+1}. [/][blue] {unescape(option)} [/]")

    choise = input(
        "[violet]Choose Correct Option[/]", choices=["1", "2", "3", "4", "Q"]
    )

    if choise.isnumeric():
        choise = int(choise)

        if options[choise - 1] == correctAns:
            print("ok")
            score += 1
        else:
            print("no")
            print(correctAns)

    else:
        if choise == "Q":
            print(score)
            exit()


print(score)
