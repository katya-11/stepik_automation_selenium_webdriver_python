from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("Value of people radio:", people_checked)
    #if people_radio button is not selected by default, the assert message below will be printed
    assert people_checked is not None, "People radio button is not selected by default"

    robot_radio = driver.find_element(By.ID, "robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("Value of robot radio:", robot_checked)
    assert robot_checked is None

    submit_before_timeout = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_enabled = submit_before_timeout.get_attribute("disabled")
    print("Value of submit button before timeout", submit_enabled)
    assert submit_enabled is None

    time.sleep(10)
    submit_after_timeout = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_disabled = submit_after_timeout.get_attribute("disabled")
    print("Value of submit button after timeout", submit_disabled)
    assert submit_disabled is not None, "Submit button is not disabled after timeout"


finally:
    time.sleep(2)
    driver.quit()
