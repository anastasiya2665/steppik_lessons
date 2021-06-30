from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# class LoginPageLocators(): копии
#     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#     REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')

class BasketPageLocators():
    BASKET_ALERT = (By.CSS_SELECTOR, '.alertinner')
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content > #content_inner')
    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(2)')
    BASKET_ORDER_TOTAL = (By.CSS_SELECTOR, '.total > .price_color')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')
