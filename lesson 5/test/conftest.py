from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/'
