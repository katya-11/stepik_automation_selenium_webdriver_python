import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture()
def driver():
    print("\nstart browser for test..1")
    driver = webdriver.Chrome()
    return driver


class TestMainPage1():
    #вызываем фикстуру в тесте, передав ее как параметр
    def test_user_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector("#login_link")



    def test_user_should_see_basket_link_on_the_login_page(self, driver):
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")