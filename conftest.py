import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    if target is None:
        with open(path) as config:
            target = json.load(config)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['base_url'])
        fixture.session.login(username=target['username'], password=target['password'])
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
    parser.addoption("--target", action="store", default="target.json")

