from selenium import webdriver
from fixture.helper import Helper
from fixture.session import SessionHelper
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class Application:

    def __init__(self, browser, language):
        if browser == 'firefox':
            options = Options()
            options.set_preference("intl.accept_languages", language)
            self.wd = webdriver.Firefox(options=options)
        elif browser == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            self.wd = webdriver.Chrome(options=options)
        else:
            raise ValueError('Unrecognized browser: ' f'{browser}')
        self.helper = Helper(self)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()