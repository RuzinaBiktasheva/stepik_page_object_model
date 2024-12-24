import time
from selenium.webdriver.common.by import By
from fixture.locators import ProdactPageLocators
from fixture.locators import BasePageLocators
from fixture.locators import LoginPageLocators
import pytest


# Проверка добавления товара в корзину.
def test_guest_can_add_product_to_basket(app):
    app.helper.add_product_to_basket('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019')
    app.helper.solve_quiz_and_get_code()
    name_product = app.wd.find_element(By.CSS_SELECTOR, 'h1').text
    price_product = app.wd.find_element(By.CSS_SELECTOR, 'p[class="price_color"]').text
    time.sleep(2)
    message_name = app.wd.find_element(By.XPATH, '//div[@id="messages"]/div/div[1]').text
    message_price = app.wd.find_element(By.XPATH, '//div[@id="messages"]/div[3]/div[1]/p[1]').text
    assert f'{name_product} был добавлен в вашу корзину.' == message_name, 'Наименование не соответствует'
    assert f'Стоимость корзины теперь составляет {price_product}' == message_price, 'Цена не соответствует'


# Тест с параметризацией, offer=7 падает.
@pytest.mark.parametrize('url', ['0', '1', '2', '3', '4', '5', '6', '8', '9', pytest.param('7', marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket_with_offer(app, url):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer' + url
    app.helper.add_product_to_basket(link)
    app.helper.solve_quiz_and_get_code()
    name_product = app.wd.find_element(By.CSS_SELECTOR, 'h1').text
    price_product = app.wd.find_element(By.CSS_SELECTOR, 'p[class="price_color"]').text
    time.sleep(1)
    message_name = app.wd.find_element(By.XPATH, '//div[@id="messages"]/div/div[1]').text
    message_price = app.wd.find_element(By.XPATH, '//div[@id="messages"]/div[3]/div[1]/p[1]').text
    try:
        assert f'{name_product} был добавлен в вашу корзину.' == message_name, 'Наименование не соответствует'
        assert f'Стоимость корзины теперь составляет {price_product}' == message_price, 'Цена не соответствует'
    finally:
        app.helper.remove_product_from_basket()

# Проверка, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message_after_adding_product_to_basket(app):
    app.helper.add_product_to_basket('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    assert app.helper.is_not_element_present(*ProdactPageLocators.SUCCESS_MESSAGE), 'Сообщение о успешном добавлении товара появляется!'

# Проверка, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(app):
    app.helper.open_page('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    assert app.helper.is_not_element_present(*ProdactPageLocators.SUCCESS_MESSAGE), 'Сообщение о успешном добавлении товара появляется!'

# Проверка, что нет сообщения об успехе с помощью is_disappeared
def test_message_disappeared_after_adding_product_to_basket(app):
    app.helper.add_product_to_basket('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    assert app.helper.is_disappeared(*ProdactPageLocators.SUCCESS_MESSAGE), 'Сообщение о успешном добавлении товара появляется!'

# Проверка, что гость видит ссылку на страницу логина со страницы Х
def test_guest_should_see_login_link_on_product_page(app):
    app.helper.open_page('http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    assert app.helper.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на страницу логина не отображается!"

# Проверка, что гость может перейти на страницу логина со страницы Х
def test_guest_can_go_to_login_page_from_product_page(app):
    app.helper.open_page('http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    app.helper.go_to_login_page()
    assert app.helper.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет возможности перейти на страницу логина!'

# Проверка, что для гостя корзина пуста.
def test_guest_cant_see_product_in_basket_opened_from_product_page(app):
    app.helper.open_page('http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    app.helper.open_basket()
    # Ожидаем, что в корзине нет товаров.
    assert app.helper.is_not_element_present(*BasePageLocators.BASKET_IS_NOT_EMPTY), 'В корзине есть товары!'
    # Ожидаем, что есть текст о том что корзина пуста.
    assert app.helper.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), 'Корзина не пуста!'