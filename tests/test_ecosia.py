from selene import have
from selene.support.shared import browser


def test_search():
    # Given
    browser.open('https://www.ecosia.org/')

    # When
    browser.element('[name=q]').type('yashaka selene').press_enter()
    browser.all('.result').first.click()

    # Then
    browser.all('[href="/yashaka/selene"]').should(have.size(3))
