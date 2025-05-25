# === File: jokes_module.py ===
# מיקום מוצע: yogev_brain/modules/jokes_module.py

import random

# רשימת בדיחות בעברית
jokes_list = [
    "איך קוראים לפיל שלמד קראטה? פיל-פינית!",
    "מה עובר לדג בראש? מים!",
    "מה עושה עכבר כשכואב לו הגב? הולך לעכברופראקטור.",
    "איך קוראים לקנגורו עצוב? קנגורונן.",
    "איך קוראים לחתול שעובד במוסך? מוסכנף.",
]

def tell_joke():
    return random.choice(jokes_list)
