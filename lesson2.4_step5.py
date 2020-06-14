from selenium import webdriver

driver = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/wait1.html")

button = driver.find_element_by_id("verify")
button.click()
message = driver.find_element_by_id("verify_message")

assert "successful" in message.text