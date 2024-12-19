import time
from selenium.webdriver.common.by import By
# Запуск в консоли: pytest -v --tb=line --language=en tests\test_main_page.py

def test_find_button(app):
    # открытие страницы
    app.helper.open_page('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    # проверка отображения кнопки
    assert len(app.wd.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')) == 1