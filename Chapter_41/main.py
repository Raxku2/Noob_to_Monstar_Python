from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse,JSONResponse, HTMLResponse
from pydantic import BaseModel
load_dotenv()

MONGO_URI = getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client["reg"]
coll = db["students"]


app = FastAPI(title="reg form", version="0.0.1")

def db_ping():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False


@app.get('/')
def root():
    # return RedirectResponse('/docs')
    return HTMLResponse("hi")

@app.get('/health')
def health():
    db_status = db_ping()
    return JSONResponse({'db_status':db_status})

class registration(BaseModel):
    name: str
    email: str
    addr: str
    phone: str
    age: str
    student: bool

@app.post('/reg')
def reg(payload: registration):
    try:
        db_status = str(coll.insert_one({
            "name":payload.name,
            "email":payload.email,
            "addr":payload.addr,
            "phone":payload.phone,
            "age":payload.age,
            "student": payload.student
        }).inserted_id)
        return JSONResponse({"user_id":db_status}, status_code=status.HTTP_201_CREATED)
    except Exception:
        print(Exception)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


