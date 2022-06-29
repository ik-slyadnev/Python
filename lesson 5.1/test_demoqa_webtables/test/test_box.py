import time
from selene.support.shared import browser

def test_new_string():
    browser.open('webtables').driver.maximize_window()

# добавить новую четвертую строку
    browser.element('#addNewRecordButton').click()

    browser.element('#firstName').type('UserNameTest')
    browser.element('#lastName').type('UserSurnameTest')
    browser.element('#userEmail').type('user_emailTest@ya.ru')

    browser.element('#age').type('28')

    browser.element('#salary').type('100000')
    browser.element('#department').type('QA')

    browser.element('#submit').click()
    time.sleep(3)

# отредактировать все поля во второй строке
def test_change_second_line():
    browser.element('#edit-record-2').click()

    browser.element('#firstName').clear().type('UserTwoNameTest')
    browser.element('#lastName').clear().type('UserTwoSurnameTest')
    browser.element('#userEmail').clear().type('user_two_emailTest@ya.ru')

    browser.element('#age').clear().type('18')
    browser.element('#salary').clear().type('200000')

    browser.element('#department').clear().type('DEV')

    browser.element('#submit').click()
    time.sleep(3)

# удалить третью строку
def test_remove_third_line():
    browser.element('#delete-record-3').click()
    time.sleep(3)










