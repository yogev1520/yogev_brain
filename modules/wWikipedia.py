# modules/wWikipedia.py

import wikipedia

# הגדרת שפת החיפוש לויקיפדיה לעברית
wikipedia.set_lang("he")

def get_wikipedia_info(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"יש כמה פירושים למונח '{query}': {', '.join(e.options[:5])}..."
    except wikipedia.exceptions.PageError:
        return "לא נמצא מידע מתאים."
    except Exception as e:
        return f"שגיאה בחיפוש: {str(e)}"
