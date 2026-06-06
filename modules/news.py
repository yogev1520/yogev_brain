# modules/NEWS14.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_newsflashes():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")  # אפשר להפעיל ברקע

    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.c14.co.il/news-flash/")

        print("ממתין לטעינת הדף...")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        headlines_elements = driver.find_elements(
            By.CSS_SELECTOR,
            "p.text-\\[17px\\].leading-\\[23px\\]"
        )

        if not headlines_elements:
            return "לא נמצאו מבזקים באתר עכשיו 14."

        headlines = [el.text.strip() for el in headlines_elements if el.text.strip()]
        if not headlines:
            return "לא נמצאו מבזקים תקפים."

        return "📢 הנה המבזקים האחרונים:\n" + "\n".join(headlines[:5])

    except Exception as e:
        return f"שגיאה בעת שליפת מבזקים: {str(e)}"
    finally:
        if driver:
            driver.quit()
