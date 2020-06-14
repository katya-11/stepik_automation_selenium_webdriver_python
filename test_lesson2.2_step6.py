from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    not_a_robot = driver.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']")
    driver.execute_script("return arguments[0].scrollIntoView(true)", not_a_robot)
    not_a_robot.click()

    robot_rule = driver.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    driver.execute_script("return arguments[0].scrollIntoView(true)", robot_rule)
    robot_rule.click()

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
    driver.execute_script("return arguments[0].scrollIntoView(true)", submit_btn)
    submit_btn.click()

finally:
    time.sleep(5)
    driver.quit()



