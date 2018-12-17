# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group0812(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="name1", group_header="header1", group_footer="footer1"))
    app.logout()

def test_add_group0812_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()

