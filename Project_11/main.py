from dotenv import load_dotenv
load_dotenv()

from os import getenv
WEATHER_API_KEY = getenv("API_KEY")


from requests import get

usr_location = input("Enter Location: ")
URI = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={usr_location}&aqi=yes"

if usr_location.lower() == 'q':
    exit()

res = get(URI)
# print(res)
apiResData: dict = (res.json())
if res.status_code <= 200 and res.status_code < 400:
    location = (apiResData.get('location'))
    weather = (apiResData.get('current'))

    print(f'Weather of {location['name']}, {location['region']}')

    print(f'''--------------------------------------------
    Temp: {weather.get('temp_c'):<5}°C  | Feels: {weather["feelslike_c"]:<5}°C |
    Wind: {weather["wind_kph"]:<5}km/h|
    Humidity: {weather['humidity']:<2}%  |description : {weather["condition"]['text']:<10}''')
elif res.status_code <= 400:
    print(f"{res.json()}")
else:
    print("hoyni, pore aso")