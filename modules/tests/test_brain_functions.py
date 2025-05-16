# test_brain_functions.py
#yogev_brain\modules\tests\test_brain_functions.py
#הפעלה בשורת הפקודה בצורה הזאת python -m modules.tests.test_brain_functions

# הפעלה: python -m modules.tests.test_brain_functions

from brain.brain import process_command

def test_basic_commands():
    print("בדיקת ברכות:")
    print(process_command("שלום"))
    print(process_command("היי, מה נשמע?"))

    print("\nבדיקת מזג אוויר:")
    print(process_command("מה מצב מזג אוויר"))

    print("\nבדיקת תחזית:")
    print(process_command("תן לי תחזית"))

    print("\nבדיקת חדשות ומבזקים:")
    print(process_command("תן לי מבזקים"))
    print(process_command("עדכונים"))

    print("\nבדיקת שעה ותאריך:")
    print(process_command("מה השעה עכשיו?"))

    print("\nבדיקת משפט השראה:")
    print(process_command("תן לי משפט השראה"))

    print("\nבדיקת ויקיפדיה:")
    print(process_command("מה זה אינטליגנציה מלאכותית"))

    print("\nבדיקת חישוב פשוט:")
    print(process_command("כמה זה שתיים ועוד שלוש"))

    print("\nבדיקת שיחה עם GPT:")
    print(process_command("שוחח עם gpt מה זה למידה עמוקה?"))

def test_calculator():
    print("\n🔢 בדיקות חישובים מורחבות:")
    test_cases = [
        "כמה זה שתיים ועוד שלוש",
        "תחשב חמש כפול ארבע",
        "כמה זה עשר חלקי שתיים",
        "כמה זה שבע פחות אחד",
        "תחשב שמונה כפול תשע",
        "כמה זה חמש ועוד משהו"  # צריך להיכשל
    ]
    for case in test_cases:
        print(f"\nשאלה: {case}")
        print(f"תשובה: {process_command(case)}")

if __name__ == "__main__":
    test_basic_commands()
    test_calculator()
