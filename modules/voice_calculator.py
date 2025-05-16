# modules/voice_calculator.py

import speech_recognition as sr

# מילון להמרת מילים למספרים בעברית
hebrew_numbers = {
    "אחד": "1", "שתיים": "2", "שניים": "2", "שלוש": "3", "ארבע": "4", "חמש": "5",
    "שש": "6", "שבע": "7", "שמונה": "8", "תשע": "9", "עשר": "10",
    "אפס": "0"
}

# מילון פעולות חשבוניות
operations = {
    "פלוס": "+", "ועוד": "+", "מינוס": "-", "פחות": "-",
    "כפול": "*", "פעמים": "*", "חלקי": "/", "לחלק": "/"
}

def convert_hebrew_expression_to_math(text):
    for word, number in hebrew_numbers.items():
        text = text.replace(word, number)
    for word, symbol in operations.items():
        text = text.replace(word, symbol)
    return text

def listen_and_calculate():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🔊 דבר את הביטוי החשבוני בעברית (למשל: חמש כפול שתיים):")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="he-IL")
        print(f"שמעת: {text}")
        expr = convert_hebrew_expression_to_math(text)
        print(f"מתורגם ל: {expr}")
        result = eval(expr)
        print(f"✅ תוצאה: {result}")
    except Exception as e:
        print("⚠️ שגיאה:", e)

# דוגמה להרצה
# listen_and_calculate()
