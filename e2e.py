import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(app_url):
    print("Running test against URL:", app_url)  # Log the test URL
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(app_url)
    try:
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        if score_text.isdigit():
            score = int(score_text)
            if 1 <= score <= 1000:
                print("Test passed, valid score found:", score)  # Log success
                return True
            else:
                print("Test failed, score out of range:", score)  # Log failure
        else:
            print("Test failed, score is not a valid number:", score_text)  # Log failure
    except Exception as e:
        print(f"Error while testing: {e}")  # Log exception

    return False


def main_function():
    app_url = "http://127.0.0.1:5000/"
    print("Starting the test...")  # Log start of test

    if test_scores_service(app_url):
        print("Test passed, Score is valid.")  # Log success
        sys.exit(0)
    else:
        print("Test failed, Score is invalid.")  # Log failure
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
