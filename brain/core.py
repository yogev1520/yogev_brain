import json
from modules.chat_gpt import chat_with_gpt

SYSTEM_PROMPT = """
You are an AI agent planner.

You MUST break the user request into steps.

Return ONLY valid JSON:

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
- No explanations outside JSON
"""

def think(user_input: str):
    response = chat_with_gpt(f"{SYSTEM_PROMPT}\nUser: {user_input}")

    try:
        return json.loads(response)
    except:
        return {
            "plan": [
                {"tool": "gpt", "input": user_input}
            ],
            "final_answer_required": True
        }