from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    btn_journey = driver.find_element(By.CSS_SELECTOR, "button.trollface").click()
    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    time.sleep(1)
    driver.switch_to.window(new_window)



    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    driver.quit()




