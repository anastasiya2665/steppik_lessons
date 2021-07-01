from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    login_page_url = "/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
       assert self.login_page_url in self.browser.current_url, \
           self.login_page_url + " are not correct login url"
        # реализуйте проверку на корректный url адрес


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        submit_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email = str(time.time()) + "@fakemail30.org"
        email_input.send_keys(email)
        pass_input.send_keys(password)
        confirm_input.send_keys(password)
        submit_btn.click()
        #метод который принимает две строки и регистрирует пользователя

    def register_new_fooluser(self, email, password, password_part):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        submit_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        pass_input.send_keys(password)
        confirm_input.send_keys(password_part)
        submit_btn.click()
        #метод который принимает две строки и регистрирует пользователя с ошибкой
