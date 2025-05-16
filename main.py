# main.py

import sys
import os

# הוספת נתיב התיקיות כדי שהייבוא יעבוד תקין
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "gui"))
sys.path.append(os.path.join(current_dir, "brain"))
sys.path.append(os.path.join(current_dir, "features"))

from GUI.ai_interface import root


def main():
    # כאן אפשר להוסיף קוד אתחול או הגדרות אם צריך
    print("✨ הפעלת עוזר יוגב...")
    root.mainloop()

if __name__ == "__main__":
    main()
