from fixture.locators import MainPageLocators
from fixture.locators import LoginPageLocators
# Запуск в консоли: pytest -v --tb=line --language=en tests\test_main_page.py

# проверка, что есть ссылка перехода на форму регистрации / аунтификации
def test_guest_can_go_to_login_page(app):
    app.helper.open_home_page()
    assert app.helper.is_element_present(*MainPageLocators.LOGIN_LINK), 'Ссылка не отображается'

# проверка, что url адрес корректный
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

# проверка, что есть форма регистрации на странице
def test_be_register_form(app):
    app.helper.open_home_page()
    app.helper.go_to_login_page()
    assert app.helper.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Формы регистрации нет на странице'