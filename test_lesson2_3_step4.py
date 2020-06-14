from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    btn_journey = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    confirm = driver.switch_to.alert
    confirm.accept()

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    driver.quit()




