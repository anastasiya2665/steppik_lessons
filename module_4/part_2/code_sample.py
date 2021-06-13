import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_input_locator = "#id_registration-email"
password_input_locator = "#id_registration-password1"
password_repeat_input_locator = "#id_registration-password2"
registration_button_locator = "registration_submit"
result_title_succsess_registration_locator = "#messages"



    test_email = "whgufd@mailto.plus"
    test_password = "test789t№Test"


  @pytest.fixture(scope='module')
  def browser():
      print("\nstart browser for test..")
      browser = webdriver.Chrome()
      yield browser
      print("\nquit browser..")
      browser.quit()


        search_input_email = browser.find_element_by_css_selector(email_input_locator)
        search_input_email.send_keys(test_email)

        search_input_password = browser.find_element_by_css_selector(password_input_locator)
        search_input_password.send_keys(test_password)

        search_input_password_repeat = browser.find_element_by_css_selector(password_repeat_input_locator)
        search_input_password_repeat.send_keys(test_password)


        browser.find_element_by_name(registration_button_locator).click()
        browser.implicitly_wait(5)


        result_succsess_title = browser.find_element_by_css_selector(result_title_succsess_registration_locator)
        assert "Спасибо за регистрацию!" in result_succsess_title.text, \
            "Not succsess user registration"
