
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class TestProductPage(BasePage):
    def test_guest_can_add_product_to_basket(link, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        product = page.get_product_name_and_price()
        page.add_to_basket()
        page.should_be_added_to_basket(product.get('product_name'))
        page.should_be_product_price(product.get('product_price'))
        page.solve_quiz_and_get_code