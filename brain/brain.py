#yogev_brain\brain\brain.py




from modules.weather_functions import get_weather, get_forecast
from modules.wWikipedia import get_wikipedia_info
from modules.NEWS14 import get_newsflashes
from modules.Motivation import get_motivational_quote
from modules.voice_calculator import convert_hebrew_expression_to_math
from modules.chat_gpt import chat_with_gpt
from modules.HELP_COMMAND import get_help_text

def process_command(command: str) -> str:
    command = command.strip().lower()

    if any(greet in command for greet in ["שלום", "היי", "מה נשמע"]):
        return "שלום! איך אני יכול לעזור לך היום?"

    if "מבזקים" in command or "עדכונים" in command:
        return get_newsflashes()

    if "חדשות" in command or "מה קרה היום" in command:
        # כאן תוכל לקרוא לפונקציה לקבלת חדשות - אם יש לך מודול news.py
        return "סליחה, כרגע פונקציית החדשות עדיין בפיתוח."

    if "מזג אוויר" in command:
        return get_weather()

    if "תחזית" in command:
        return get_forecast()

    if "מה השעה" in command or "מה התאריך" in command:
        from datetime import datetime
        now = datetime.now()
        return f"השעה עכשיו היא {now.strftime('%H:%M:%S')} והתאריך היום הוא {now.strftime('%d/%m/%Y')}."

    if "משפט השראה" in command or "תן לי השראה" in command:
        return get_motivational_quote()

    if command.startswith("מה זה") or command.startswith("מי זה"):
        query = command.replace("מה זה", "").replace("מי זה", "").strip()
        if query:
            return get_wikipedia_info(query)
        else:
            return "אנא פרט מה ברצונך לחפש."

    if "שיר של" in command or "נגן ביוטיוב" in command:
        return "סליחה, ניגון ביוטיוב טרם מומש."

    if "כמה זה" in command or "תחשב" in command:
        try:
            expr = convert_hebrew_expression_to_math(command)
            result = eval(expr)
            return f"התוצאה היא: {result}"
        except Exception:
            return "לא הצלחתי לחשב את הביטוי שניתן."

    if "שוחח עם gpt" in command or "דבר איתי" in command or "צ'אט" in command:
        prompt = command.replace("שוחח עם gpt", "").replace("דבר איתי", "").replace("צ'אט", "").strip()
        if not prompt:
            return "מה תרצה לשאול את GPT?"
        return chat_with_gpt(prompt)

    if "נקה שיחה" in command:
        return "__CLEAR_CHAT__"

    if "פתח לוג" in command:
        return "__OPEN_LOG__"

    if "נקה לוגים" in command:
        return "__CLEAR_LOGS__"

    if "סגור" in command or "להתראות" in command or "צא" in command:
        return "__EXIT__"

    if "עזרה" in command or "מה אתה יודע לעשות" in command:
        return get_help_text()

    return "אני לא מבין את הפקודה, אנא נסה שנית."
