from modules.weather_functions import get_weather
from modules.wikipedia import get_wikipedia_info
from modules.chat_gpt import chat_with_gpt
from modules.news import get_newsflashes
from modules.jokes_module import tell_joke
from modules.voice_calculator import calculate_from_text

def run(plan):
    results = []

    for step in plan.get("plan", []):
        tool = step.get("tool")
        input_text = step.get("input", "")

        if tool == "weather":
            results.append(get_weather())

        elif tool == "wiki":
            results.append(get_wikipedia_info(input_text))

        elif tool == "news":
            results.append(get_newsflashes())

        elif tool == "joke":
            results.append(tell_joke())

        elif tool == "calculator":
            results.append(calculate_from_text(input_text))

        elif tool == "gpt":
            results.append(chat_with_gpt(input_text))

    # מסכם הכול לתשובה אחת חכמה
    return chat_with_gpt(
        "Summarize this into one clear answer:\n" + "\n".join(results)
    )