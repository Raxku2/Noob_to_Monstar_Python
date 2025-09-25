from fastapi import FastAPI
from rich.traceback import install
from rich.console import Console
from pydantic import BaseModel

console = Console()
install()
app = FastAPI()


fake_db = ["apple", "banana"]


@app.get("/items")
def items():
    return {"data": fake_db}


@app.post("/additem/{fruit}")
def additem(fruit: str):

    fake_db.append(fruit)

    if fruit in fake_db:
        return {"status": "Item added sucessfully"}
    else:
        return {"status": "err"}


class folobj(BaseModel):
    foler_nam: str 


@app.post("/addfrt") 
def addfrt(fol: folobj):
    fake_db.append(fol.foler_nam)

    if fol.foler_nam in fake_db:
        return {"status": "Item added sucessfully"}
    else:
        return {"status": "err"}
