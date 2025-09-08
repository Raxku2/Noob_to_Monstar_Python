import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()
API_KEY = getenv('API_KEY')

location = input("Enter Location: ")
role = input("Enter Role: ")
params = {
    "engine": "google_jobs",
    "q": role,
    "location": location,   
    "api_key": API_KEY
}

response = requests.get("https://serpapi.com/search", params=params)


data = response.json()

all_jobs_data = data.get("jobs_results")

for job in all_jobs_data:
    print(f"One job posting found at {job['company_name']}, in {job['location']}, for {job['title']}| Apply: {job['apply_options']}",'\n')