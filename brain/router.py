def extract_location(text):
    text = text.lower()

    if "תל אביב" in text:
        return "Tel Aviv"

    if "ירושלים" in text:
        return "Jerusalem"

    if "חיפה" in text:
        return "Haifa"

    return "Israel"