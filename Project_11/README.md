# 🌦️ Project 11: Weather App (API)  

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
[![Requests](https://img.shields.io/badge/Library-requests-yellow)](https://docs.python-requests.org/)  
[![dotenv](https://img.shields.io/badge/Library-python--dotenv-green)](https://pypi.org/project/python-dotenv/)  
[![API](https://img.shields.io/badge/API-weatherapi.com-blueviolet)](https://www.weatherapi.com/)  

---

## 📖 Overview
This project is a **Weather App CLI** that fetches **real-time weather data** from [WeatherAPI](https://www.weatherapi.com/).  
It demonstrates:
- 🌐 **API integration** in Python.  
- 🔑 Using **environment variables** (`.env`) for security.  
- 📊 Displaying weather details like **temperature, wind, humidity, and conditions**.  

---

## ✨ Features
- 🔍 Search weather by **city or location**.  
- 🌡️ Shows **current temperature & feels-like** values.  
- 🌬️ Displays **wind speed** and **humidity**.  
- ☁️ Provides **weather description** (e.g., "Cloudy", "Rainy").  
- 🔑 Secure API key management with **dotenv**.  

---

## ⚙️ Tech Stack
- **Python 3.x**  
- [Requests](https://docs.python-requests.org/) – For HTTP requests  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – For secure API keys  
- [WeatherAPI](https://www.weatherapi.com/) – Data provider  

---

## 🚀 Setup & Installation

1. Clone the project folder:
   ```bash
   git clone https://github.com/your-repo/Project_11_Weather_App.git
   cd Project_11_Weather_App
   ````

2. Install dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Get a free API key from [WeatherAPI](https://www.weatherapi.com/).

4. Create a `.env` file in the project root:

   ```env
   API_KEY=your_weatherapi_key_here
   ```

---

## ▶️ Usage

Run the app:

```bash
python weather_app.py
```

Example:

```
Enter Location: Kolkata
Weather of Kolkata, West Bengal
--------------------------------------------
Temp: 30   °C  | Feels: 33   °C |
Wind: 12   km/h|
Humidity: 78%  | description: Partly cloudy
```

To quit, enter:

```
Enter Location: q
```

---

## 📂 Project Structure

```
Project_11_Weather_App/
│── README.md
│── weather_app.py
│── .env.example
```

---

## 🧠 Learning Takeaway

* ✅ Use **APIs** to get real-world data.
* ✅ Always keep **API keys secret** with `.env`.
* ✅ Handle **status codes** and possible API errors gracefully.

---
