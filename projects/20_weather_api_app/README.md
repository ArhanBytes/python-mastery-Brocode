# 🌦️ Weather App (PyQt5 GUI)

A modern **Weather Application** built using PyQt5 that fetches real-time weather data using an API and displays it with a clean and styled interface.

---

## 🚀 Features

* 🌍 Get weather by city name
* 🌡️ Displays temperature (°C)
* ☁️ Weather condition description
* 🌈 Emoji-based weather visualization
* ⚠️ Proper error handling (invalid city, network issues, etc.)
* 🎨 Styled GUI using CSS

---

## 📌 What It Does

* Takes a city name as input
* Sends a request to the weather API
* Fetches live weather data
* Displays:

  * Temperature
  * Weather description
  * Weather emoji

---

## ▶️ How To Run

### 1. Install Requirements

```bash
pip install PyQt5 requests
```

### 2. Run the Application

```bash
python 20_weather_api_app/main.py
```

### 3. Enter City Name

* Example: `Karachi`, `London`, `New York`

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* PyQt5 (GUI Development)
* API Handling (`requests`)
* JSON Data Processing
* Exception Handling
* QLabel, QLineEdit, QPushButton
* Layout Management (QVBoxLayout)
* Signals & Slots
* Styling (CSS in PyQt)

---

## 🖥️ Preview

![Weather App UI](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/20_weather_api_app/output.png)

---

## ⚠️ Note

* You need a valid API key from **OpenWeatherMap**
* Replace this line in code:

```python
api_key = "YOUR_API_KEY"
```

---

## 💡 Future Improvements

* Add search history
* Show humidity & wind speed
* Add 5-day forecast
* Dark/Light mode toggle

---