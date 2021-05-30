from selenium import webdriver

avtorization_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_input_locator = "#id_registration-email"
password_input_locator = "#id_registration-password1"
password_repeat_input_locator = "#id_registration-password2"
registration_button_locator = "registration_submit"
result_title_succsess_registration_locator = "#messages"


def test_registration():
    # Data
    test_email = "whgufd@mailto.plus"
    test_password = "test789t№Test"


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(avtorization_link)

        # Act
        search_input_email = browser.find_element_by_css_selector(email_input_locator)
        search_input_email.send_keys(test_email)

        search_input_password = browser.find_element_by_css_selector(password_input_locator)
        search_input_password.send_keys(test_password)

        search_input_password_repeat = browser.find_element_by_css_selector(password_repeat_input_locator)
        search_input_password_repeat.send_keys(test_password)


        browser.find_element_by_name(registration_button_locator).click()
        browser.implicitly_wait(5)

        # Assert
        result_succsess_title = browser.find_element_by_css_selector(result_title_succsess_registration_locator)
        assert "Спасибо за регистрацию!" in result_succsess_title.text, \
            "Succsess user registration"

    finally:
        browser.quit()


test_registration()

