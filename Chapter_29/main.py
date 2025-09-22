from rich.traceback import install

install()


"""
debo -> post-> create - C
nebo -> get -> read   - R *
likhbo -> update      - U
muchbo -> delete      - D
CRUD 
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world", "name": "Rakesh"}


@app.get("/about")
def about():
    return "This is a codeShiksha lession"


@app.get("/members")
def about():
    return 65


@app.get("/sum/{data=0}/{data=0}")
def sum(data: int = 0, data2: int = 0):
    
    if data and data2:
        return {"sum": data + data2}
    else:
        return "no input value found"
