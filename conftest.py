import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("base_url")
        fixture = Application(browser=browser, base_url=base_url)
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/")

