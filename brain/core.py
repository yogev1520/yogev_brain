import json
from modules.groq_ai import chat_with_groq


SYSTEM_PROMPT = """
You are an AI agent planner.

You MUST break the user request into steps.

Return ONLY valid JSON (no markdown, no explanation):

{
  "plan": [
    {
      "tool": "weather | wiki | news | joke | calculator | gpt",
      "input": "what to pass to tool"
    }
  ],
  "final_answer_required": true
}

Rules:
- Always break complex tasks into steps
- You can use multiple tools
- Keep steps minimal but logical
- If unsure, use tool: gpt
- Output MUST be valid JSON only
"""


def safe_json_parse(text: str):
    """
    מחלץ JSON בצורה בטוחה גם אם המודל מוסיף טקסט מסביב
    """
    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            try:
                return json.loads(text[start:end + 1])
            except:
                pass

    return None


def think(user_input: str):
    response = chat_with_groq(
        f"{SYSTEM_PROMPT}\nUser: {user_input}"
    )

    plan = safe_json_parse(response)

    if plan:
        return plan

    # fallback בטוח
    return {
        "plan": [
            {
                "tool": "gpt",
                "input": user_input
            }
        ],
        "final_answer_required": True
    }