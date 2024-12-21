from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Helper:

    def __init__(self, app):
        self.app = app

    def open_page(self, link):
        wd = self.app.wd
        wd.get(link)

    def go_to_login_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "#login_link").click()

    def is_element_present(self, how, what):
        wd = self.app.wd
        try:
            wd.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True