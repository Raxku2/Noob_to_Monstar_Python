r = requests.get("https://httpbin.org/ip")
print(r.json())

params = {"course": "python", "level": "beginner"}
r = requests.get("https://httpbin.org/get", params=params)
print(r.json())


data = {"id": 1, "task": "Learn requests"}
r = requests.post("https://httpbin.org/post", json=data)
print(r.json())


headers = {"X-Student": "Alice"}
r = requests.get("https://httpbin.org/get", headers=headers)
print(r.json())


try:
    r = requests.get("https://httpbin.org/status/500")
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Handled error:", e)

r = requests.get("https://jsonplaceholder.typicode.com/users")
print(r.json()[:5])


data = {"username": "bob", "password": "123"}
r = requests.post("https://httpbin.org/post", data=data)
print(r.json())


def fetch_data(url):
    try:
        r = requests.get(url)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


r = requests.get("https://httpbin.org/basic-auth/user/pass", auth=("user", "pass"))
print(r.json())


r = requests.get("https://api.github.com/users/octocat")
print(r.json())
