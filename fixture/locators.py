from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProdactPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[class="alert alert-safe alert-noicon alert-info  fade in"]')