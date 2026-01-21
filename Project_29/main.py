from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
from fastapi import FastAPI, status, Response
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId

load_dotenv()
Mongo_uri = getenv("MONGO_URI")
client = MongoClient(Mongo_uri)
db = client["markdown"]
coll = db["docs"]
app = FastAPI(title="Markdown editor backend", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all header
)


@app.get("/")
def root():
    return RedirectResponse("/docs")


@app.get("/health")
def health():
    try:
        client.admin.command("ping")
        return JSONResponse({"db_status": "ok", "api_status": "ok"})
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class new_doc(BaseModel):
    title: str
    data: str


# new doc
@app.post("/doc")
def create_doc(peyload: new_doc):
    res = str(
        coll.insert_one({"title": peyload.title, "doc": peyload.data}).inserted_id
    )
    if res:
        return JSONResponse({"_id": res}, status_code=status.HTTP_201_CREATED)
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    # return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# doc show
@app.get("/doc")
def show_doc(doc_id: str):
    res = dict(coll.find_one({"_id": ObjectId(doc_id)}, {"_id": 0}))
    if res:
        return JSONResponse(res, status_code=status.HTTP_302_FOUND)
    else:
        return Response(status_code=404)


# doc list
@app.get("/documents")
def docs_ids():
    res = list(coll.find({}, {"_id": 1, "title": 1}))
    for doc in res:
        doc["_id"] = str(doc["_id"])
    if res:
        return JSONResponse(res, status_code=status.HTTP_302_FOUND)
    else:
        return Response(status_code=404)
