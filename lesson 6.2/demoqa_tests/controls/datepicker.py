from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


class Date_picker:
    def __init__(self, element, year, month, day):
        self.element = element
        self.year = year
        self.month = str(month - 1)
        self.day = str(day) if day > 9 else f'0{day}'

    def set_date_straight(self):
        self.element.click()
        browser.element(f'.react-datepicker__year-select [value="{self.year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{self.month}"]').click()
        browser.element(f'.react-datepicker__day--0{self.day}').click()

    def set_date_by_clicks(self):
        self.element.click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select [value="{self.year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select [value="{self.month}"]').click()
        browser.element(f'.react-datepicker__day--0{self.day}').click()


