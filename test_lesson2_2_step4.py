from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    #driver.execute_script("alert('Robots at work');")
    #driver.execute_script("document.title='Script executing';")
    driver.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(5)
    driver.quit()