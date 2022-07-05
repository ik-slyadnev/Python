from selene import have
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

# Проверка
def test_checking_result():
    browser.element(".rt-tr-group").element(1).ss('.rt-td').element(0).should(have.exact_text('UserNameTest'))
    browser.element(".rt-tr-group").element(2).ss('.rt-td').element(0).should(have.exact_text('UserSurnameTest'))
    browser.element(".rt-tr-group").element(3).ss('.rt-td').element(0).should(have.exact_text('28'))
    browser.element(".rt-tr-group").element(4).ss('.rt-td').element(0).should(have.exact_text('user_emailTest@ya.ru'))
    browser.element(".rt-tr-group").element(5).ss('.rt-td').element(0).should(have.exact_text('UserNameTest'))
    browser.element(".rt-tr-group").element(6).ss('.rt-td').element(0).should(have.exact_text('UserNameTest'))


# удалить третью строку
def test_remove_third_line():
    browser.element('#delete-record-3').click()











