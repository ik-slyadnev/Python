from conftest import *


def test_serch_selene(browser_open):
    browser.element('[name="q"]').type('selene user').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))



def test_serch_fail_selene(browser_open):
    browser.element('[name="q"]').type('selene user').press_enter()
    browser.element('[id="search"]').should(have.text('GURU Python'))

