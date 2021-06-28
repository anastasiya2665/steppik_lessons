import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
from .pages.locators import ProductPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.add_to_basket()
        item_page.solve_quiz_and_get_code()
        item_page.check_item_name()
        item_page.check_price()
