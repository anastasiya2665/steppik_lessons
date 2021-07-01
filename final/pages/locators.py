from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    # LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    # USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():


    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class MainPageLocators(BasePageLocators):
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    def __init__(self, *args, **kwargs):
        super(BasePageLocators, self).__init__(*args, **kwargs)


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page div.product_main p.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    # BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    # EMPTY_BASKET = (By.ID, "content_inner")
    # BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')
    URGENT_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages .alert-success div.alertinner strong")
    URGENT_INFO_MESSAGES = (By.CSS_SELECTOR, "#messages .alert-info div.alertinner strong")
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini")
    #LOADER = (By.CSS_SELECTOR, "#loader"

class BasketPageLocators():
    # BASKET_ALERT = (By.CSS_SELECTOR, '.alertinner')
    # BASKET_CONTENT = (By.CSS_SELECTOR, '.content > #content_inner')
    CONTENT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    # BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(2)')
    # BASKET_ORDER_TOTAL = (By.CSS_SELECTOR, '.total > .price_color')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')
