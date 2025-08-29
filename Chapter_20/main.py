
import requests

# Example 1: Basic GET
r = requests.get("https://api.github.com")
print("Status Code:", r.status_code)

# Example 2: GET with parameters
params = {"q": "python requests", "page": 1}
r = requests.get("https://httpbin.org/get", params=params)
print(r.json())

# Example 3: POST with JSON
payload = {"username": "test", "password": "secret"}
r = requests.post("https://httpbin.org/post", json=payload)
print(r.json())

# Example 4: Custom headers
headers = {"User-Agent": "Chapter20-App"}
r = requests.get("https://httpbin.org/headers", headers=headers)
print(r.json())

# Example 5: Error handling
try:
    r = requests.get("https://httpbin.org/status/404")
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Caught an error:", e)
