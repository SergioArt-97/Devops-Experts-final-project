import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

print("=== E2E TEST STARTED ===")


def wait_for_selenium_server(full_url, timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(full_url)
            print(f"Connecting to Selenium at {full_url}, status: {response.status_code}")  # Log the response
            if response.status_code == 200:
                print("Selenium server is ready.")
                break
        except requests.exceptions.ConnectionError as e:
            print(f"Connection failed: {e}")  # Log connection failures
        if time.time() - start_time > timeout:
            raise Exception("Timeout waiting for Selenium server.")
        time.sleep(5)

def test_scores_service(app_url):
    print("Running test against URL:", app_url)  # Log the test URL

    options = Options()
    options.add_argument("--headless=new")  # Run in headless mode for testing
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    selenium_base_url = 'http://selenium:4444'
    selenium_status_url = f"{selenium_base_url}/wd/hub/status"
    selenium_url = f"{selenium_base_url}/wd/hub"

    print(f"Connecting to Selenium at {selenium_status_url}")  # Log the Selenium URL
    wait_for_selenium_server("http://selenium:4444/wd/hub/status")

    print(f"[DEBUG] Final Selenium URL used: {selenium_url}")

    try:
        driver = webdriver.Remote(command_executor=selenium_url, options=options)
        print("WebDriver connected successfully.")  # Log WebDriver connection success
    except Exception as e:
        print(f"Error connecting to WebDriver: {e}")  # Log WebDriver connection error
        raise e

    driver.get(app_url)
    try:
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        if score_text.isdigit():
            score = int(score_text)
            if 0 <= score <= 1000:
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
    app_url = "http://flask-app:5000"
    print("Starting the test...")  # Log start of test

    if test_scores_service(app_url):
        print("Test passed, Score is valid.")  # Log success
        sys.exit(0)
    else:
        print("Test failed, Score is invalid.")  # Log failure
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
