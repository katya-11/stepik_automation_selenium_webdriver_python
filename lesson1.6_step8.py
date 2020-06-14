from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    first_name = driver.find_element(By.NAME, "first_name").send_keys("Katya")
    last_name = driver.find_element(By.NAME, "last_name").send_keys("Katya")
    city = driver.find_element(By.NAME, "firstname").send_keys("Minsk")
    country = driver.find_element(By.ID, "country").send_keys("Belarus")
    submit_btn = driver.find_element(By.XPATH, "//*[@class='btn' and @type = 'submit']").click()

finally:
    time.sleep(10)
    driver.quit()