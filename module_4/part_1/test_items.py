

#В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку
#добавления в корзину с корректным текстом. Например, можно проверять товар, доступный по
#http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

from selenium import webdriver
import pytest

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")


def test_ukraine_language(browser) -> None:
    expected = "Додати в кошик"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert actual == expected, f"{actual} != {expected} in Ukraine language"


def test_russian_language(browser) -> None:
    expected = "Добавить в корзину"
    browser.get(link)
    actual = browser.find_element(*BUTTON_ADD_TO_BASKET).text
    assert actual == expected, f"{actual} != {expected} in Russian language"