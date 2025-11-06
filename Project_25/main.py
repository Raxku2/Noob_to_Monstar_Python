import secrets
import string
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse


class shortData(BaseModel):
    url: str

app = FastAPI()

load_dotenv()

mongo_URI = getenv("MONGO_URI")

Client = MongoClient(mongo_URI)
db = Client["urlDB"]
coll = db["urls"]


def generate_token(length=10):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    token = "".join(secrets.choice(characters) for _ in range(length))
    return token


@app.get("/")
def home():
    return RedirectResponse(url="/docs")


@app.post("/short")
def short(data: shortData):
    try:
        url = data.url
        try:
            while True:
                token = generate_token()
                exists = coll.find_one({"token": token}, {"_id": 0})
                if exists:
                    continue
                else:
                    state = coll.insert_one({"url": url, "token": token})
                    if state.inserted_id:
                        return {
                            "status": 200,
                            "message": "recorded",
                            "url": f"http://localhost:8000/{token}",
                        }
                    break
        except:
            return {"status": 404, "message": "Mongo DB error"}
    except:
        return {"status": 404, "message": "API Endpoint error"}
    return 0



@app.get("/{token}")
def redirect(token: str):
    try:
        if token.isalnum():
            try:
                state = coll.find_one({"token": token}, {"url": 1,"_id":0})
                if state:
                    url = state["url"]
                    return RedirectResponse(url=url)
                else:
                    return {"message": "DB Error"}
            except:
                return {"message": "DB Error"}
        else:
            return {"message": "invalid url"}
    except:
        return {"message": "invalid url"}
