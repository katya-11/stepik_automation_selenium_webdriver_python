from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"


try:
    driver = webdriver.Chrome()
    driver.get(link)

    value1 = driver.find_element(By.ID, "num1").text
    value2 = driver.find_element(By.ID, "num2").text
    num1 = int(value1)
    num2 = int(value2)
    print(num1)
    print(num2)
    sum = str(num1 + num2)
    print(sum)

    dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
    dropdown.select_by_value(sum)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    driver.quit()




