import pytest

from selene import browser


@pytest.fixture(params=[(1920, 1080), (1366, 720)])
def desktop_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=[(800, 600), (960, 540)])
def mobile_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=['desktop_resolution', 'mobile_resolution'])
def resolution(request):
    if request.param == 'desktop_resolution':
        browser.config.window_width = 1300
        browser.config.window_height = 1080
    elif request.param == 'mobile_resolution':
        browser.config.window_width = 800
        browser.config.window_height = 600

    yield
    browser.quit()


@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.base_url = 'https://github.com'
