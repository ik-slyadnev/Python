import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def browser_open():
    browser.open('https://google.com')


@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080