import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language: en, ru, es, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    # Устанавливаем язык интерфейса браузера
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    print(f"\nstart chrome browser for test with language: {user_language}..")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
