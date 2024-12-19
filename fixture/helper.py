import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Helper:

    def __init__(self, app):
        self.app = app

    # открытие страницы
    def open_page(self, link):
        wd = self.app.wd
        wd.get(link)

    # расчет математической функции
    def calc(self):
        wd = self.app.wd
        x = int(wd.find_element(By.ID, 'input_value').text)
        return str(math.log(abs(12 * math.sin(int(x)))))

    # получение кода
    def get_code(self):
        wd = self.app.wd
        alert = wd.switch_to.alert
        alert_text = alert.text[79:]
        print(alert_text)
        alert.accept()

    # вычисление значения, ввод значения в поле и нажатие кнопки ввода
    def calculation(self):
        wd = self.app.wd
        answer = math.log(int(time.time()))
        wd.find_element(By.CSS_SELECTOR, 'textarea').send_keys(answer)
        # явное ожидание кликабельности кнопки
        button = WebDriverWait(wd, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="submit-submission"]'))
        )
        button.click()