from modules.weather_functions import get_weather
from modules.wikipedia import get_wikipedia_info
from modules.groq_ai import chat_with_groq
from modules.news import get_newsflashes
from modules.jokes_module import tell_joke
from modules.voice_calculator import calculate_from_text

from brain.normalizer import normalize_result
import json


def run(plan):

    results = []

    # 🧠 safety: ensure dict
    if isinstance(plan, str):
        try:
            plan = json.loads(plan)
        except:
            return {
                "done": True,
                "answer": "Invalid plan format"
            }

    print("PLAN RAW:", plan)

    for step in plan.get("plan", []):

        tool = step.get("tool")
        input_text = step.get("input") or ""

        print("TOOL:", tool, "INPUT:", input_text)

        try:

            if tool == "weather":
                location = input_text or "ישראל"
                result = get_weather(location)
                results.append(normalize_result(result))

            elif tool == "wiki":
                query = input_text or "תל אביב"
                result = get_wikipedia_info(query)
                results.append(normalize_result(result))

            elif tool == "news":
                result = get_newsflashes()
                results.append(normalize_result(result))

            elif tool == "joke":
                result = tell_joke()
                results.append(normalize_result(result))

            elif tool == "calculator":
                result = calculate_from_text(input_text)
                results.append(normalize_result(result))

            elif tool == "gpt":
                result = chat_with_groq(input_text)
                results.append(normalize_result(result))

            else:
                results.append(normalize_result(f"Unknown tool: {tool}"))

        except Exception as e:
            results.append(normalize_result(f"Tool error ({tool}): {e}"))

    # 🧠 Summary layer
    summary_prompt = (
        "You are a helpful assistant.\n"
        "Summarize the following tool results into one clear answer:\n\n"
        + "\n".join(str(r) for r in results)
    )

    try:
        final_answer = chat_with_groq(summary_prompt)
    except Exception as e:
        final_answer = "\n".join(str(r) for r in results) + f"\n\n[Summary error: {e}]"

    return normalize_result({
        "done": True,
        "answer": final_answer,
        "raw_results": results
    })