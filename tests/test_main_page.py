from fixture.locators import MainPageLocators
from fixture.locators import LoginPageLocators
from fixture.locators import BasePageLocators
# Запуск в консоли: pytest -v --tb=line --language=en tests\test_main_page.py

# Проверка, что есть ссылка перехода на форму регистрации / аунтификации.
def test_guest_can_go_to_login_page(app):
    app.helper.open_home_page()
    assert app.helper.is_element_present(*MainPageLocators.LOGIN_LINK), 'Ссылка не отображается'

# Проверка, что url адрес корректный.
def test_be_login_url(app):
    app.helper.open_home_page()
    app.helper.go_to_login_page()
    current_url = app.wd.current_url
    assert 'login' in current_url, 'Подстроки "login" нет в текущем url браузера'

# проверка, что есть форма логина
def test_be_login_form(app):
    app.helper.open_home_page()
    app.helper.go_to_login_page()
    assert app.helper.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Формы логина нет на странице'

# Проверка, что есть форма регистрации на странице.
def test_be_register_form(app):
    app.helper.open_home_page()
    app.helper.go_to_login_page()
    assert app.helper.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Формы регистрации нет на странице'

# Проверка, что для гостя корзина пуста.
def test_guest_cant_see_product_in_basket_opened_from_main_page(app):
    app.helper.open_home_page()
    app.helper.open_basket()
    # Ожидаем, что в корзине нет товаров.
    assert app.helper.is_not_element_present(*BasePageLocators.BASKET_IS_NOT_EMPTY), 'В корзине есть товары!'
    # Ожидаем, что есть текст о том что корзина пуста.
    assert app.helper.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), 'Корзина не пуста!'