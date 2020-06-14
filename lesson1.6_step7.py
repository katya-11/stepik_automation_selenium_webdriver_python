from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    input_field = driver.find_elements_by_css_selector("[type = 'text']")
    for element in input_field:
        element.send_keys("Test")

    button = driver.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(10)
    driver.quit()
