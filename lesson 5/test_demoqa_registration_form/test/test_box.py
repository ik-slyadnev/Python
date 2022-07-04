import os
from selene.support.shared import browser
from selene import have, command

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

    # Assertions
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element("//td[text()='Student Name']").element("..").should(have.text('TestName TestSurname'))
    browser.element("//td[text()='Student Email']").element("..").should(have.text('test_email@ya.ru'))

    browser.element("//td[text()='Gender']").element("..").should(have.text('Male'))
    browser.element("//td[text()='Mobile']").element("..").should(have.text('9208887755'))

    browser.element("//td[text()='Date of Birth']").element("..").should(have.text('18 September,1993'))
    browser.element("//td[text()='Subjects']").element("..").should(have.text('Economics, English'))

    browser.element("//td[text()='Hobbies']").element("..").should(have.text('Sports, Music'))
    browser.element("//td[text()='Picture']").element("..").should(have.text('l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg'))

    browser.element("//td[text()='Address']").element("..").should(have.text('Bolshaya Nikitskaya st., 22k2, Moscow, 121099'))
    browser.element("//td[text()='State and City']").element("..").should(have.text('Rajasthan Jaipur'))



