#Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
#Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
#Браузер должен объявляться в фикстуре browser и передаваться в тесты как параметр.
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

options = None


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Chose language')


@pytest.fixture(scope='module')
def browser(request):
    lang_user = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_user})
    print('\nstart Chrome browser...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit Chrome browser...')
    browser.quit()




