from requests import get

# Example 1: Get a random joke from Official Joke API
res = get("https://official-joke-api.appspot.com/jokes/random")

if res.status_code == 200:
    joke = res.json()
    print(f"😂 {joke['setup']}")
    print(f"👉 {joke['punchline']}")
else:
    print("Failed to fetch joke, try again later.")

# Example 2: Get Bitcoin price from Coindesk
res = get("https://api.coindesk.com/v1/bpi/currentprice.json")
if res.status_code == 200:
    btc_data = res.json()
    usd_price = btc_data['bpi']['USD']['rate']
    print(f"₿ Current Bitcoin Price: {usd_price} USD")
