import allure
from selene import browser, have


class GeneralPage:
    def open(self):
        with allure.step('Открытие главной страницы'):
            browser.open('/')
            return self

    def click_signin(self):
        with allure.step("Нажать кнопку Sign in"):
            browser.element(".HeaderMenu-link--sign-in").click()

    def click_burger_menu(self):
        with allure.step("Нажать на Бургер-меню"):
            browser.element(".Button--link").click()

    def should_url_login(self, url):
        browser.should(have.url(url))


general_page = GeneralPage()
