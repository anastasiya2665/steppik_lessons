import pytest
from .pages.product_page import ProductPage
import time
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver.support import expected_conditions

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

class TestProductPage():
    @pytest.mark.parametrize('promo_number',
                             ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_number):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        promo_link = '?promo=offer'
        item_page = ProductPage(browser, link + promo_link + promo_number)
        item_page.open()
        item_page.add_to_basket()
        item_page.solve_quiz_and_get_code()
        # item_page.check_item_name()
        # item_page.check_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_dissapeared_after_adding_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_dissapear_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

    @pytest.mark.xfail
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()

    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail30.org"
        login_page.register_new_user(email, "pop86fghynnv")
        login_page.should_be_authorized_user()

    @pytest.fixture(scope="function", autouse=True)
    def setupF(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail30.org"
        login_page.register_new_fooluser(email, "pop86fghynnv", "pop86fg1")
        login_page.should_be_not_authorized_user()
#метод неудачного сообщения реги


