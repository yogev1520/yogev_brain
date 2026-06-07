class AgentV2:
    def __init__(self, planner, executor):
        self.planner = planner
        self.executor = executor

    def run(self, user_input):
        memory = []

        for _ in range(5):
            plan = self.planner.think(
                user_input=user_input,
                memory=memory
            )

            result = self.executor.run(plan)

            memory.append({
                "plan": plan,
                "result": result
            })

            if result.get("done"):
                return result["answer"]

        return "לא הצלחתי להשלים את המשימה."