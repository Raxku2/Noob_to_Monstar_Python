from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
import hashlib
import base64
import secrets

load_dotenv()

def create_Token(bytes: int = 20):
    return secrets.token_hex(bytes)

def generateHash(text):
    data = text.encode('utf-8')
    hash_bytes = hashlib.sha256(data).digest()
    base64_hash = base64.b64encode(hash_bytes).decode('ascii')
    return base64_hash

USER_DB_URI = getenv("USER_DB_URI")

userDB_CLient = MongoClient(USER_DB_URI)
userDB = userDB_CLient['usr_data']
userColl = userDB['cred']

# userColl.insert_one({'usrname':'amar@mail.com','pass':generateHash('Passw0rd')})

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)


class loginCred(BaseModel):
    email: str
    passwd: str

@app.get('/')
def home():
    return JSONResponse({"status":'true', 'message':"Hello!!"})

@app.post('/login')
def login(cred: loginCred):
    email = cred.email
    passwd = cred.passwd

    try:
        usrNameData = userColl.find_one({'usrname':email},{'_id':0})
        userPasswd = usrNameData['pass']

        if userPasswd == passwd:
            token  = create_Token()
            return {'message':'logged in','token':token,'status':200}
        else:
            return JSONResponse({'message':"Invalid Password",'status':403})
    except:
        return JSONResponse({"status":404,"message":'invalid username'})

