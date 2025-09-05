from requests import get
from time import sleep

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

while True:
    res = get(URL)
    if res.status_code == 200:
        data = res.json()
        bpi = data['bpi']
        print(f"USD: {bpi['USD']['rate']}, GBP: {bpi['GBP']['rate']}, EUR: {bpi['EUR']['rate']}")
    else:
        print("Failed to fetch price.")
    sleep(30)


## ✅ Solution 2: NASA APOD

from requests import get

API_KEY = "DEMO_KEY"  # Replace with your free API key from https://api.nasa.gov
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

res = get(URL)
if res.status_code == 200:
    data = res.json()
    print(f"Title: {data['title']}")
    print(f"Explanation: {data['explanation']}")
    print(f"Image URL: {data['url']}")
else:
    print("Failed to fetch APOD data.")

## ✅ Solution 3: Weather Dashboard


from requests import get

API_KEY = "YOUR_API_KEY"
CITY = input("Enter city: ")
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

res = get(URL)
if res.status_code == 200:
    data = res.json()
    weather = data['current']
    print(f"Temp: {weather['temp_c']}°C | Condition: {weather['condition']['text']} | Humidity: {weather['humidity']}%")
else:
    print("Failed to fetch weather data.")
