from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MONGO_URI = getenv("MONGO_URI")
Client = MongoClient(MONGO_URI)

db = Client["db_1"]

user_collection = db["users"]
skills_collection = db["skils"]
projects_collection = db["projects"]


def is_db_a_connected():
    """check db is connected or not"""
    try:
        Client.admin.command("ping")
        print("DB Connected")
        return True
    except:
        print("DB Not Connected")
        return False
