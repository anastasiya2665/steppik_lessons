import math
import re
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
# from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait

#исправить методы в классах в алфавитном порядке

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #открыть текщуюю страницу
    def open(self):
         self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    #кликаем по логин ссылке
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    #проверяем что ссылка логин сушествует
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def is_text_present_at(self, where, what, explicit_timeout=12):
        try:
            WebDriverWait(self.browser, explicit_timeout).until(
                wait_for_text_to_match(where, what))
        except TimeoutException:
            return False
        return True

    def check_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link are not presented'

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    #исчезновение элемента
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    #формула
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


     #ожидание подсчета
class wait_for_text_to_match:
        def __init__(self, locator, pattern):
                self.locator = locator
                self.pattern = re.compile(pattern)

        def __call__(self, driver):
            try:
                element_text = EC._find_element(driver, self.locator).text
                return self.pattern.search(element_text)
            except StaleElementReferenceException:
                return False
