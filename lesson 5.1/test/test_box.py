import time

from selene.support.shared import browser
from selene.core import command
from selene import be, have

def test_new_string():
    browser.open('webtables').driver.maximize_window()

# добавить новую четвертую строку
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('ivan_petrov@ya.ru')
    browser.element('#age').should(be.blank).type('100')
    browser.element('#salary').should(be.blank).type('100000')
    browser.element('#department').should(be.blank).type('QA')
    browser.element('#submit').click()
    time.sleep(3)

# отредактировать все поля во второй строке
def test_change_second_line():
    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type('Anna')
    browser.element('#lastName').clear().type('Ivanova')
    browser.element('#userEmail').clear().type('anna_ivanova@ya.ru')
    browser.element('#age').clear().type('25')
    browser.element('#salary').clear().type('200000')
    browser.element('#department').clear().type('DEV')
    browser.element('#submit').click()
    time.sleep(3)

# удалить третью строку
def test_remove_third_line():
    browser.element('#delete-record-3').click()
    time.sleep(3)










