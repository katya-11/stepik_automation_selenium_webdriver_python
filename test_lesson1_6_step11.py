from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Katya")
    last_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Makey")
    email = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("katya@mail.ru")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(2)

    welcome_txt_el = driver.find_element(By.TAG_NAME, "h1")
    welcome_txt = welcome_txt_el.text
    assert "Congratulations! You have successfully registered!" == welcome_txt

finally:
    time.sleep(5)
    driver.quit()
