import time

from selene.support.shared import browser
from selene.core import command
from selene import be, have

def test_submit_form():
    browser.open('automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type('Ivan')
    browser.element('[id="lastName"]').should(be.blank).type('Petrov')
    browser.element('[id="userEmail"]').should(be.blank).type('ivan_petrov@ya.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('9208887755')
    browser.element('[id="dateOfBirth-wrapper"]').click()
    browser.element(".react-datepicker__month-select").type("September")
    browser.element(".react-datepicker__year-select").type("1993")
    browser.element("[aria-label= 'Choose Saturday, September 18th, 1993']").click()
    browser.element("#subjectsInput").type("Economics").press_enter().type("English").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').type('D:\\l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg')
    time.sleep(1)
    browser.element('[id="currentAddress"]').type('Bolshaya Nikitskaya st., 22k2, Moscow, 121099')
    browser.element("#state").perform(command.js.scroll_into_view).click()
    browser.element('[id="state"]').click()
    browser.element("#state input").type("Rajasthan").press_enter()
    browser.element('[id="city"]').click()
    browser.element("#city input").type("Jaipur").press_enter()
    browser.element('footer')._execute_script('element.style.display = "None"')
    browser.element('[id="submit"]').press_enter()
    time.sleep(3)





