from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer").send_keys(y)
    checkbox = driver.find_element(By.ID, "robotCheckbox").click()
    radio_btn = driver.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    driver.quit()
