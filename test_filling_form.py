from selene import browser, by, have


def test_form_filling():

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('lisressy@test.com')
    browser.element('#userNumber').type('1122334455')
    browser.element('#currentAddress').type('Ghandi str., 11')
    browser.element('#subjectsInput').type('Maths').press_enter()


    browser.element('label[for="gender-radio-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()


    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(17)
    browser.element('.react-datepicker__year-select').send_keys(1999)
    browser.element('.react-datepicker__day--015').click()


    browser.element('#state').click()
    browser.element('//div[text()="NCR"]').click()

    browser.element('#city').click()
    browser.element('//div[text()="Delhi"]').click()

    browser.element('#submit').click()

    browser.element('.modal-content').should(have.text('John'))
    browser.element('.modal-content').should(have.text('Doe'))
    browser.element('.modal-content').should(have.text('lisressy@test.com'))
    browser.element('.modal-content').should(have.text('1122334455'))
    browser.element('.modal-content').should(have.text('Ghandi str., 11'))
