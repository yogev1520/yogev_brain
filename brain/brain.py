from brain.core import think
from brain.executor import run


def process_command(user_input: str):
    """
    Main entry point for the AI brain.
    1. Send input to planner (core)
    2. Execute planned steps (executor)
    3. Return final response
    """

    # שלב 1: GPT מתכנן מה לעשות
    plan = think(user_input)

    # שלב 2: הרצת התוכנית
    result = run(plan)

    return result