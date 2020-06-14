from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
number = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = ("http://suninjuly.github.io/find_link_text")
try:
    driver = webdriver.Chrome()
    driver.get(link)
    url = driver.find_element(By.PARTIAL_LINK_TEXT, number).click()

    first_name = driver.find_element(By.NAME, "first_name").send_keys("Katya")
    last_name = driver.find_element(By.NAME, "last_name").send_keys("Makey")
    city = driver.find_element(By.NAME, "firstname").send_keys("Minsk")
    country = driver.find_element(By.ID, "country").send_keys("Belarus")
    submit_btn = driver.find_element(By.CLASS_NAME, "btn.btn-default").click()


finally:
    time.sleep(10)
    driver.quit()




