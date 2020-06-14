from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = driver.find_element(By.ID, "answer").send_keys(y)
    not_a_robot = driver.find_element(By.ID, "robotCheckbox").click()
    robot_rule_radio = driver.find_element(By.ID, "robotsRule").click()
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    driver.quit()