import time
from selenium.webdriver.common.by import By
from fixture.locators import ProdactPageLocators
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