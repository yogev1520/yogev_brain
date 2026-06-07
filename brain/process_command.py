from brain.core import think
from brain.executor import run
from brain.memory import load_memory, add_memory
from brain.router import extract_location


def process_command(user_input: str):

    text = user_input.lower()

    # 🔥 RULE-BASED FAST PATH (חייב להיות ראשון)
    if "מזג" in text or "weather" in text:

        location = extract_location(user_input)

        plan = {
            "plan": [
                {
                    "tool": "weather",
                    "input": location
                }
            ]
        }

        result = run(plan)

        add_memory({
            "input": user_input,
            "plan": plan,
            "result": result
        })

        return result.get("answer") if isinstance(result, dict) else result


    # 🧠 MEMORY LOAD
    memory = load_memory()

    state = {
        "goal": user_input,
        "history": memory[-2:]
    }

    # 🧠 ניקוי רעש לשאלות מזג אוויר
    if "מזג" in text:
        state["history"] = []

    used = set()

    for _ in range(3):

        plan = think(state)

        filtered = []

        for p in plan.get("plan", []):
            key = f"{p.get('tool')}::{p.get('input')}"

            if key in used:
                continue

            used.add(key)
            filtered.append(p)

        plan["plan"] = filtered

        result = run(plan)

        add_memory({
            "input": user_input,
            "plan": plan,
            "result": result
        })

        if isinstance(result, dict) and result.get("done"):
            return result.get("answer")

    return "לא הצלחתי להשלים את המשימה."