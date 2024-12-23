import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from fixture.locators import MainPageLocators
from fixture.locators import ProdactPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class Helper:

    def __init__(self, app):
        self.app = app

    def open_page(self, link):
        wd = self.app.wd
        wd.get(link)

    def open_home_page(self):
        self.open_page('http://selenium1py.pythonanywhere.com/')

    def go_to_login_page(self):
        wd = self.app.wd
        wd.find_element(*MainPageLocators.LOGIN_LINK).click()

    def is_element_present(self, how, what):
        wd = self.app.wd
        try:
            wd.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        wd = self.app.wd
        alert = wd.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(1)
        try:
            alert = wd.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_to_basket(self, link):
        wd = self.app.wd
        self.open_page(link)
        wd.find_element(*ProdactPageLocators.BUTTON_ADD_TO_BASKET).click()

    def remove_product_from_basket(self):
        wd = self.app.wd
        wd.implicitly_wait(1)
        wd.find_element(By.CSS_SELECTOR, 'a[class="btn btn-default"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[id="id_form-0-quantity"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[id="id_form-0-quantity"]').clear()
        wd.find_element(By.CSS_SELECTOR, 'input[id="id_form-0-quantity"]').send_keys('0')
        wd.find_element(By.CSS_SELECTOR, 'button[data-loading-text="Обновление..."]').click()

    def is_not_element_present(self, how, what, timeout=4):
        wd = self.app.wd
        try:
            WebDriverWait(wd, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        wd = self.app.wd
        try:
            WebDriverWait(wd, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True