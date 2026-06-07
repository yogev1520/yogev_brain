from brain.core import think
from brain.executor import run


# 🧠 זיהוי מהיר של שאלות פשוטות
def smart_router(user_input: str):
    text = user_input.lower()

    if "מזג" in text or "weather" in text:
        return "weather"

    if "בדיחה" in text:
        return "joke"

    if any(op in text for op in ["+", "-", "*", "/"]):
        return "calculator"

    if "מי" in text or "מה זה" in text:
        return "wiki"

    return None


def process_command(user_input: str):

    # 🔥 שלב 1: Router מהיר
    direct_tool = smart_router(user_input)

    if direct_tool:

        plan = {
            "plan": [
                {
                    "tool": direct_tool,
                    "input": user_input
                }
            ]
        }

        result = run(plan)

        return result.get("answer")

    # 🔥 שלב 2: Agent רגיל (מורכב)
    state = {
        "goal": user_input,
        "history": []
    }

    used = set()

    for _ in range(3):  # ⬅️ פחות steps = יותר מהיר

        plan = think(state)

        filtered = []

        for p in plan.get("plan", []):
            key = f"{p.get('tool')}::{p.get('input')}"

            # ❌ מניעת כפילויות
            if key in used:
                continue

            # ❌ הורדת GPT מיותר
            if p.get("tool") == "gpt":
                continue

            used.add(key)
            filtered.append(p)

        plan["plan"] = filtered

        result = run(plan)

        state["history"].append({
            "plan": plan,
            "result": result
        })

        if isinstance(result, dict) and result.get("done"):
            return result.get("answer")

    return "לא הצלחתי להשלים את המשימה."