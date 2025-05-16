#Motivation.py

import requests

def get_motivational_quote():
    url = "https://api.quotable.io/random?tags=inspire"  # API חיצוני עם משפטי השראה
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['content']  # החזרת הציטוט
        else:
            return "לא הצלחנו להוריד את הציטוט, נסה שוב מאוחר יותר."
    except Exception as e:
        return f"שגיאה: {str(e)}"
