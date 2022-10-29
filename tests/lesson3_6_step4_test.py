import pytest
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_LINKS = ["https://stepik.org/lesson/236895/step/1",
              "https://stepik.org/lesson/236896/step/1",
              "https://stepik.org/lesson/236897/step/1",
              "https://stepik.org/lesson/236898/step/1",
              "https://stepik.org/lesson/236899/step/1",
              "https://stepik.org/lesson/236903/step/1",
              "https://stepik.org/lesson/236904/step/1",
              "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('page_id', PAGE_LINKS)
def test_stepik_time_synchronize(browser_chrome, page_id):
    browser_chrome.get(page_id)
    print("Loading a web page")
    answer = math.log(int(time.time() + 0.3))
    browser_chrome.implicitly_wait(10)
    print("Setting implicit wait interval for a browser")
    text_area = browser_chrome.find_element(By.CLASS_NAME, "ember-text-area")
    text_area.send_keys(str(answer))
    print("Sending answer to the text area")
    submit_button = browser_chrome.find_element(By.CLASS_NAME, "submit-submission")
    submit_button.click()
    print("Clicking the button")
    optional_feedback = WebDriverWait(browser_chrome, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    ).text
    assert optional_feedback == "Correct!", f"Optional feedback is incorrect: {optional_feedback}"
