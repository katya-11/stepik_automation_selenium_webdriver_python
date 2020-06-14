from selenium import webdriver
import time

from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.NAME, "first_name").send_keys("Katya")
    last_name = driver.find_element(By.NAME, "last_name").send_keys("Makey")
    city = driver.find_element(By.NAME, "firstname").send_keys("Minsk")
    country = driver.find_element(By.ID,"country").send_keys("Belarus")
    submit_btn = driver.find_element(By.ID,"submit_button").click()

finally:
    time.sleep(5)
    driver.quit()




