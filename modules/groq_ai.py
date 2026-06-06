# modules/groq_ai.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# בדיקת מפתח (רק לדיבוג – תוכל למחוק אחרי שזה עובד)
print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_with_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"שגיאה ב-Groq: {str(e)}"