import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    first_name = driver.find_element(By.NAME, "firstname").send_keys("Katya")
    last_name = driver.find_element(By.NAME, "lastname").send_keys("Makey")
    email = driver.find_element(By.NAME, "email").send_keys("katya@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_upload = driver.find_element(By.CSS_SELECTOR, "[type = 'file']").send_keys(file_path)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    driver.quit()

