from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/square/{number}")
def square_number(number: int):
    return {"square": number ** 2}
