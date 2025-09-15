
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import getpass
from argparse import ArgumentParser
from os import getenv
from dotenv import load_dotenv

load_dotenv()
URI = getenv("MONGO_URI")

parser = ArgumentParser()
parser.add_argument('--reg', action='store_true', help="'--reg' for register new user")
parser.add_argument('--name','-n', type=str, default='', help='name')
parser.add_argument('--usr','-u', type=str, default='', help='username')
parser.add_argument('--email','-e', type=str, default='', help='email')
parser.add_argument('--list','-ls', action='store_true', help="list all registers user")

args = parser.parse_args()

# Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi('1'))

db = client["db1"]
coll = db['items']


def register_user(collection):
    name = args.name.strip()
    email = args.email.strip()
    username = args.usr.strip()
    password = getpass.getpass("Password: ").strip()
    
    # Check if username/email already exists
    if collection.find_one({"$or": [{"username": username}, {"email": email}]}):
        print("⚠️ Username or Email already exists. Try again.")
        return
    
    user_data = {
        "name": name,
        'username': username,
        "email": email,
        "password": password 
    }
    if name and email and username and password:
        collection.insert_one(user_data)
        print("✅ Registration successful!")
    else:
        print("Invalid input!")

def list_users(collection):
    for user in collection.find({}, {"_id": 0, "password": 0}):  # Hide password
        print(user)



def main():
    if args.reg:
        register_user(coll)
    elif args.list:
        list_users(coll)
    else:
        print("Invalis input")
    # pass


main()