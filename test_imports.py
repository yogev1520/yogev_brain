# test_imports.py

modules_to_test = [
    "GUI.ai_interface",       # GUI עם אות גדולה אם תיקייתך כך נקראת
    "brain.brain",
    "modules.HELP_COMMAND",
    "modules.chat_gpt",
    "modules.wWikipedia",
    "modules.weather_functions",
    "modules.NEWS14",
    "modules.Motivation",
    "modules.voice_calculator",
]

print("בדיקת טעינת מודולים...")

success = True

for module_name in modules_to_test:
    try:
        __import__(module_name)
        print(f"[OK] מודול '{module_name}' נטען בהצלחה.")
    except Exception as e:
        print(f"[ERROR] בעיה בטעינת מודול '{module_name}': {e}")
        success = False

if success:
    print("\nכל המודולים נטענו ללא בעיות!")
else:
    print("\nיש בעיות בטעינת מודולים. בדוק את ההודעות למעלה.")
