from selenium.webdriver.common.by import By
# Запуск в консоли: pytest -v --tb=line --language=en tests\test_main_page.py

def test_guest_can_go_to_login_page(app):
    app.helper.open_page('http://selenium1py.pythonanywhere.com/')
    assert app.helper.is_element_present(By.CSS_SELECTOR, "#login_link"), 'Тест прошел!'