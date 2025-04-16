import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

def wait_for_selenium_server(url, timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Selenium server is ready.")
                break
        except requests.exceptions.ConnectionError:
            pass
        if time.time() - start_time > timeout:
            raise Exception("Timeout waiting for Selenium server.")
        time.sleep(1)

def test_scores_service(app_url):
    print("Running test against URL:", app_url)  # Log the test URL

    options = Options()
    options.add_argument("--headless")  # Run in headless mode for testing
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    selenium_url = 'http://selenium:4444/wd/hub'
    wait_for_selenium_server(selenium_url)
    driver = webdriver.Remote(command_executor=selenium_url, options=options)

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
