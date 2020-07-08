import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit driver..")
    driver.quit()


@pytest.mark.parametrize("links", ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_user_should_submit_the_answer(driver, links):
    link = f"{links}"
    driver.get(link)
    answer = math.log(int(time.time()))
    text_answer = str(answer)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))).send_keys(text_answer)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.attempt__message")))
    message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__feedback")))
    assert "Correct!" in message.text

