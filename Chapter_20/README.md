# 🌐 Chapter 20: HTTP Requests with `requests`  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![Requests](https://img.shields.io/badge/Library-requests-yellow)](https://pypi.org/project/requests/)  
[![API](https://img.shields.io/badge/Focus-HTTP%20API-orange)]()  

---

## 📖 Overview
This chapter introduces the **`requests` library** in Python, which allows you to interact with web servers using HTTP methods such as GET, POST, PUT, and DELETE.  

It is one of the most widely used libraries for **REST APIs, web scraping, and automation scripts**.  

---

## ✨ Topics Covered
- 🌍 Sending **GET requests**  
- 📩 Sending **POST requests**  
- 🛠️ Using headers and parameters  
- 📦 Sending JSON payloads  
- 🔐 Handling authentication  
- ⚠️ Error handling with `status_code` and exceptions  

---

## 🛠️ Installation
Install the `requests` library:
```bash
pip install requests
```
🚀 Learning Code Examples
1️⃣ Basic GET Request
```python
import requests
response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Response Body:", response.json())
```

2️⃣ GET Request with Parameters
```python
import requests
url = "https://httpbin.org/get"
params = {"name": "Alice", "age": 22}

response = requests.get(url, params=params)
print(response.json())
```

3️⃣ POST Request with JSON Data
```python
import requests

url = "https://httpbin.org/post"
data = {"username": "admin", "password": "1234"}

response = requests.post(url, json=data)
print(response.json())
```

4️⃣ Adding Headers
```python
import requests

url = "https://httpbin.org/headers"
headers = {"User-Agent": "MyApp/1.0"}

response = requests.get(url, headers=headers)
print(response.json())
```

5️⃣ Handling Errors
```python
import requests

try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)
```

📂 Chapter Structure
```bash
Chapter_20_HTTP_Requests/
│── README.md        # Documentation
│── learning_code.py # Example code snippets
│── practice_set.md  # Exercises
│── solutions.md     # Answers/Explanations
```
