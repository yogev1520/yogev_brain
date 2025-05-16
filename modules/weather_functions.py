# modules/weather_functions.py

import requests
import os

# מפתחות API מהסביבה (או מקובץ .env)
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "515aaaa2d3cc24490f7170cf4bdc6894")
FORECAST_API_KEY = os.getenv("WEATHERSTACK_API_KEY", "7c905d464147917cae31d681ccb6d226")

def get_weather(location="ישראל"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&lang=he&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "main" in data:
            temperature = data["main"].get("temp", "?")
            description = data["weather"][0].get("description", "?")
            humidity = data["main"].get("humidity", "?")
            wind_speed = data["wind"].get("speed", "?")

            return f"הטמפרטורה כעת ב{location} היא {temperature}°C, {description}. לחות: {humidity}%, רוח: {wind_speed} קמ\"ש."
        else:
            return "⚠️ לא הצלחתי לקבל את נתוני מזג האוויר."
    except Exception as e:
        return f"שגיאה: {str(e)}"

def get_forecast(location="ישראל"):
    url = f"http://api.weatherstack.com/forecast?access_key={FORECAST_API_KEY}&query={location}&language=he"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "forecast" in data:
            forecast_data = data["forecast"]
            forecast = ""
            for date, weather in forecast_data.items():
                temp = weather.get('temperature', '?')
                desc = weather.get('weather_descriptions', [''])[0]
                forecast += f"📅 בתאריך {date} צפויה טמפרטורה של {temp}°C, {desc}. "
            return forecast
        else:
            return "⚠️ לא הצלחתי לקבל את תחזית מזג האוויר."
    except Exception as e:
        return f"שגיאה: {str(e)}"
