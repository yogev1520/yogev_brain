def normalize_result(tool_result):
    """
    הופך כל output לפורמט אחיד
    """

    if isinstance(tool_result, dict):
        return tool_result

    return {
        "type": "text",
        "content": str(tool_result)
    }
