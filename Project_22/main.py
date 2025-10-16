from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()
URI = getenv("MONGO_URI")

client = MongoClient(URI)
db = client["blogDB"]
coll = db["myblog"]


app = FastAPI()

class BlogData(BaseModel):
    title :str 
    body : str
    author: str

@app.get('/')
def home():
    return {'status':"ok", 'message':"API UP"}

# Blog name, Blog content, Author

@app.post('/post')
def postBlog(params: BlogData):
    data_title = params.title
    data_body = f"""{params.body}"""
    data_author = params.author
    print(data_title,data_body,data_author)
    status = str(coll.insert_one({'title':data_title,'body':data_body,'author':data_author}).inserted_id)
    if status:
        return {'status':status,'message':"Data inserted"}
    else:
        return {'status':"err",'message':"something went wrong"}


@app.get('/blog')
def getAllBlog():
    data = coll.find({},{'_id':0})
    # print(list(data))
    res = list(data)
    if res:
        return {'status':"ok",'data':res}
    else:
        return {'status':"err",'message':"something went wrong"}











