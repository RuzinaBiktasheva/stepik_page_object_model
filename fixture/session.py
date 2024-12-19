from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    # авторизация на Stepik
    def login(self, email, password):
        wd = self.app.wd
        self.app.helper.open_page('https://stepik.org/catalog?auth=login')
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        wd.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys(email)
        wd.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(10)

    # logout на Stepik
    def logout(self):
        wd = self.app.wd
        dropdown = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[class="navbar__profile-img"]'))
        )
        dropdown.click()
        button = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-qa="menu-item-logout"] > button')))
        button.click()
        ok_button = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]'))
        )
        ok_button.click()