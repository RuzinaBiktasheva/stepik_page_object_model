import pytest
from fixture.application import Application


# инициализация фикстуры
@pytest.fixture(scope="session")
def app(request):
    browser = request.config.getoption('--browser')
    language = request.config.getoption('--language')
    fixture = Application(browser=browser, language=language)
    request.addfinalizer(fixture.destroy)
    return fixture

# инициализация параметров
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--language', action='store', default='ru')