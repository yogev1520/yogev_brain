# -*- coding: utf-8 -*-
# ייבוא מודולים נדרשים
# ai_interface.py
from modules.jokes_module import tell_joke
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import os
import datetime
import time
from gtts import gTTS
import tempfile
import speech_recognition as sr
import threading

from brain.brain import process_command
from modules.help import get_help_text  # כאן תיקנתי את הייבוא

# יצירת תיקיית לוגים אם לא קיימת
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

def save_log(message):
    today = datetime.date.today().isoformat()
    with open(f"{log_dir}/log_{today}.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def open_log():
    today = datetime.date.today().isoformat()
    log_path = os.path.join(log_dir, f"log_{today}.txt")
    if os.path.exists(log_path):
        os.system(f"notepad {log_path}")
    else:
        messagebox.showinfo("אין לוג", "אין שיחות שנשמרו להיום.")

def clear_logs():
    for filename in os.listdir(log_dir):
        if filename.endswith(".txt"):
            os.remove(os.path.join(log_dir, filename))
    messagebox.showinfo("נמחק", "כל קבצי הלוג נמחקו.")

def clear_chat():
    chat_area.configure(state='normal')
    chat_area.delete("1.0", tk.END)
    chat_area.configure(state='disabled')

# פונקציה נוחה להוספת טקסט ל-chat_area
def append_chat(text):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, text)
    chat_area.configure(state='disabled')
    chat_area.see(tk.END)

# פונקציית דיבור עם gTTS
def speak(text, lang='iw'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name
        tts.save(filename)
        os.system(f'start {filename}')  # Windows
    except Exception as e:
        print(f"שגיאה בהקראה: {e}")

# פונקציית האזנה למיקרופון
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("אני מקשיב...")
        time.sleep(1)
        print("התחלת האזנה...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="he-IL")
    except sr.UnknownValueError:
        return "שגיאת זיהוי: לא הצלחתי להבין אותך"
    except sr.RequestError:
        return "שגיאת חיבור: בעיה בגישה לאינטרנט"

# פונקציה שמטפלת בשיחה קולית (רצה ברקע)
def listen_and_respond():
    def thread_func():
        user_input = listen()
        append_chat(f"🗣️ אתה אמרת: {user_input}\n")
        save_log(f"🗣️ אתה אמרת: {user_input}")

        if "שגיאת" in user_input:
            append_chat(f"❌ {user_input}\n\n")
            speak(user_input)
            return

        response = process_command(user_input)
        append_chat(f"🤖 יוגב: {response}\n\n")
        save_log(f"🤖 יוגב: {response}\n")

        speak(response)

    threading.Thread(target=thread_func).start()

def show_joke():
    joke = tell_joke()
    append_chat(f"😂 בדיחה: {joke}\n\n")
    save_log(f"😂 בדיחה: {joke}")
    speak(joke)


# פונקציה לשליחת פקודה מקלט הטקסט (שליחה רגילה)
def send_command():
    user_input = input_field.get()
    if not user_input.strip():
        return

    append_chat(f"👤 אתה: {user_input}\n")
    save_log(f"👤 אתה: {user_input}")
    input_field.delete(0, tk.END)

    response = process_command(user_input)
    append_chat(f"🤖 יוגב: {response}\n\n")
    save_log(f"🤖 יוגב: {response}\n")

# הגדרת חלון ראשי
root = tk.Tk()
root.title("המוח של יוגב - עוזר קולי חכם")
root.geometry("700x600")
root.configure(bg="#f5f5f5")

# כותרת ראשית
title_label = tk.Label(root, text="🤖 המוח של יוגב", font=("Rubik", 24, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# אזור שיחה עם גלילה
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Rubik", 14), width=70, height=20, bg="white")
chat_area.pack(padx=10, pady=10)
chat_area.configure(state='disabled')  # נעילה לעריכה ישירה

# שורת קלט
input_frame = tk.Frame(root, bg="#f5f5f5")
input_field = tk.Entry(input_frame, font=("Rubik", 14), width=50, justify='right')
input_field.pack(side=tk.RIGHT, padx=10, pady=5)

send_button = tk.Button(input_frame, text="➤ שלח", font=("Rubik", 12), bg="#4CAF50", fg="white", command=send_command)
send_button.pack(side=tk.RIGHT, padx=5)

input_frame.pack()

# אפשר לשלוח את הטקסט גם בלחיצת Enter
input_field.bind("<Return>", lambda event: send_command())

# כפתורי פעולה נוספים
buttons_frame = tk.Frame(root, bg="#f5f5f5")

clear_button = tk.Button(buttons_frame, text="🧹 נקה שיחה", font=("Rubik", 10), command=clear_chat)
clear_button.grid(row=0, column=0, padx=5, pady=5)

log_button = tk.Button(buttons_frame, text="📁 פתח לוג", font=("Rubik", 10), command=open_log)
log_button.grid(row=0, column=1, padx=5, pady=5)

clear_logs_button = tk.Button(buttons_frame, text="🗑️ נקה לוגים", font=("Rubik", 10), command=clear_logs)
clear_logs_button.grid(row=0, column=2, padx=5, pady=5)

help_button = tk.Button(buttons_frame, text="❓ עזרה", font=("Rubik", 10), command=lambda: append_chat(get_help_text() + "\n\n"))
help_button.grid(row=0, column=3, padx=5, pady=5)

exit_button = tk.Button(buttons_frame, text="🚪 צא", font=("Rubik", 10), command=root.quit)
exit_button.grid(row=0, column=4, padx=5, pady=5)

# כפתור הפעלה קולית חדש
listen_button = tk.Button(buttons_frame, text="🎙️ דבר עכשיו", font=("Rubik", 10), bg="#2196F3", fg="white", command=listen_and_respond)
listen_button.grid(row=0, column=5, padx=5, pady=5)

buttons_frame.pack(pady=10)

# התחלת לולאת GUI
root.mainloop()
