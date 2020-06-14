from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_btn = driver.find_element(By.ID, "book").click()

    submit_btn = driver.find_element(By.CSS_SELECTOR, "#solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit_btn.click()

finally:
    time.sleep(5)
    driver.quit()

