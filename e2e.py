import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(app_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(app_url)
    try:
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        if score_text.isdigit():
            score = int(score_text)
            if 1 <= score <= 1000:
                return True
    except Exception as e:
        print(f"Error while testing: {e}")

    return False

def main_function():
    app_url = "http://127.0.0.1:5000/"

    if test_scores_service(app_url):
        print("Test passed, Score is valid.")
        sys.exit(0)
    else:
        print("Test failed, Score is invalid.")
        sys.exit(-1)