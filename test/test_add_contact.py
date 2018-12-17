# -*- coding: utf-8 -*-
from selenium import webdriver

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create_new_contact(Contact(firstname="1", middlename="middlename", lastname="lastname", nickname="nickname", photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title="title",
                                            company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                                            homepage="homepage", bday="1", bmonth="August", byear="1985", address2="address2", phone="phone2", notes="notes"))

        app.session.logout()


