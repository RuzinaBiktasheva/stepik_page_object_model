from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, 'input[id="id_registration-email"]')
    PASSWORD_1 = (By.CSS_SELECTOR, 'input[id="id_registration-password1"]')
    PASSWORD_2 = (By.CSS_SELECTOR, 'input[id="id_registration-password2"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProdactPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[class="alert alert-safe alert-noicon alert-info  fade in"]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'div[id="content_inner"] p')
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, 'div[class="basket-title hidden-xs"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")