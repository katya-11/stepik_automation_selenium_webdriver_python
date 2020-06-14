from selenium import webdriver
import time
try:
    driver = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    driver.get(link)
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    time.sleep(5)
    driver.quit()

