API = "https://open.er-api.com/v6/latest/USD"

from requests import get
res = get(API)


apiResponse = res.json().get('rates')
all_currency = list(apiResponse.keys())

print(f"you can choose from :\n {all_currency}")

amount = int(input("Value: "))

frCurr = input("from Currency: ")
toCurr = input("to currency: ")

current = [apiResponse[frCurr],apiResponse[toCurr]]

print((amount/current[0])*current[1])
