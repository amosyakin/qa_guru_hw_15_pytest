import pytest

from qa_guru_hw_15_pytest.model.pages.general_page import general_page


@pytest.mark.parametrize('resolution', ['desktop_resolution'], indirect=True)
def test_desktop_signin(resolution):
    general_page.open()
    general_page.click_signin()
    general_page.should_url_login('https://github.com/login')


@pytest.mark.parametrize('resolution', ['mobile_resolution'], indirect=True)
def test_mobile_signin(resolution):
    general_page.open()
    general_page.click_burger_menu()
    general_page.click_signin()
    general_page.should_url_login('https://github.com/login')
