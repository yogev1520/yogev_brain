# modules/voice_calculator.py

from simpleeval import simple_eval

hebrew_numbers = {
    "אחד": "1", "שתיים": "2", "שניים": "2", "שלוש": "3", "ארבע": "4", "חמש": "5",
    "שש": "6", "שבע": "7", "שמונה": "8", "תשע": "9", "עשר": "10", "אפס": "0"
}

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

def calculate_expression(expression):
    """
    מחשב את הביטוי המתמטי המומר בצורה בטוחה.
    """
    try:
        result = simple_eval(expression)
        return f"התוצאה היא: {result}"
    except Exception as e:
        return "⚠️ לא הצלחתי לחשב את הביטוי. ודא שהוא תקין."

def calculate_from_text(text):
    expr = convert_hebrew_expression_to_math(text)
    return calculate_expression(expr)
