from qa_guru_hw_15_pytest.model.pages.general_page import general_page


def test_desktop_signin(desktop_resolution):
    general_page.open()
    general_page.click_signin()
    general_page.should_url_login('https://github.com/login')


def test_mobile_signin(mobile_resolution):
    general_page.open()
    general_page.click_burger_menu()
    general_page.click_signin()
    general_page.should_url_login('https://github.com/login')
