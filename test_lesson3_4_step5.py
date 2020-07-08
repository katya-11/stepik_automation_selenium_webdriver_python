import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope = "class")
def driver():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    #этот код выполнится после завершения теста
    print("\nquit browser for test ")
    driver.quit()


class TestMainPage1():
    #вызываем фикстуру в тесте, передав ее как параметр
    def test_user_should_see_login_link(self, driver):
        print("Start test 1")
        driver.get(link)
        driver.find_element_by_css_selector("#login_link")
        print("Finish test 1")



    def test_user_should_see_basket_link_on_the_login_page(self, driver):
        print("Start test 2")
        driver.get(link)
        driver.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("Finish test 2")