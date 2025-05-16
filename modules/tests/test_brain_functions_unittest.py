import unittest
from brain.brain import process_command

class TestBrainFunctions(unittest.TestCase):

    def test_greetings(self):
        response = process_command("שלום")
        self.assertTrue("שלום" in response or "היי" in response)

        response = process_command("היי, מה נשמע?")
        self.assertTrue("שלום" in response or "היי" in response)

    def test_weather(self):
        response = process_command("מה מצב מזג אוויר")
        self.assertTrue("מזג" in response or "תחזית" in response)

    def test_forecast(self):
        response = process_command("תן לי תחזית")
        self.assertTrue("תחזית" in response or "מזג" in response)

    def test_news(self):
        response = process_command("תן לי מבזקים")
        self.assertTrue("חדשות" in response or "מבזקים" in response)

        response = process_command("עדכונים")
        self.assertTrue("חדשות" in response or "מבזקים" in response)

    def test_time_date(self):
        response = process_command("מה השעה עכשיו?")
        self.assertTrue("שעה" in response or "זמן" in response or "עת" in response)

    def test_inspiration(self):
        response = process_command("תן לי משפט השראה")
        self.assertTrue(len(response) > 10)  # משפט השראה לא יהיה ריק

    def test_wikipedia(self):
        response = process_command("מה זה אינטליגנציה מלאכותית")
        self.assertTrue("אינטליגנציה" in response or "מלאכותית" in response)

    def test_calculation(self):
        response = process_command("כמה זה שתיים ועוד שלוש")
        self.assertTrue(any(word in response for word in ["5", "חמש", "5.0"]))

    def test_chat_gpt(self):
        try:
            response = process_command("שוחח עם gpt מה זה למידה עמוקה?")
            self.assertTrue(len(response) > 0)
        except Exception as e:
            self.fail(f"שיחה עם GPT נכשלה: {e}")

if __name__ == "__main__":
    unittest.main()



# # test_brain_functions.py
# #yogev_brain\modules\tests\test_brain_functions.py
# #הפעלה בשורת הפקודה בצורה הזאת python -m modules.tests.test_brain_functions
#