# YOGEV_BRAIN/modules/chat_gpt.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("חסר מפתח API של OpenAI. ודא שקובץ .env כולל את OPENAI_API_KEY.")

client = OpenAI(api_key=api_key)

# פונקציה מרכזית שתשמש את המוח
def chat_with_gpt(user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "אתה עוזר קולי חכם בשם יוגב."},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"שגיאה בשיחה עם GPT: {str(e)}"
