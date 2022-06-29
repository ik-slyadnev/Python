import time, os
from selene.support.shared import browser
from selene import be, have, command

def test_student_registration_form():
    browser.open('automation-practice-form')

    # First name, last name, mail
    browser.element('#firstName').type('TestName')
    browser.element('#lastName').type('TestSurname')
    browser.element('#userEmail').type('test_email@ya.ru')

    # Gender
    browser.element('[for="gender-radio-1"]').click()
    # Phone number
    browser.element('#userNumber').type('9208887755')

    # Form with date
    browser.element('#dateOfBirth-wrapper').click()
    browser.element('.react-datepicker__month-select').type("September")
    browser.element('.react-datepicker__year-select').type("1993")
    browser.element('[aria-label= "Choose Saturday, September 18th, 1993"]').click()

    # Subjects
    browser.element('#subjectsInput').type('Economics').press_enter().type('English').press_enter()

    # Hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Loading a picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg'))

    # Address
    browser.element('#currentAddress').type('Bolshaya Nikitskaya st., 22k2, Moscow, 121099')

    # Scroll
    browser.element('#state').perform(command.js.scroll_into_view).click()

    # State selection
    browser.element('#state').click()
    browser.element('#state input').type('Rajasthan').press_enter()

    # City selection
    browser.element('#city').click()
    browser.element('#city input').type('Jaipur').press_enter()

    # Submit form button
    browser.element('#submit').press_enter()

    # Let's see the result of magic
    time.sleep(2)





