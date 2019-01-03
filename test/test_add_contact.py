# -*- coding: utf-8 -*-
from selenium import webdriver

from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="1check", middlename="middlename", lastname="lastnamecheck", nickname="nickname", photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title="title",
                                            company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                                            homepage="homepage", bday="1", bmonth="August", byear="1985", address2="address2", phone="phone2", notes="notes")
    app.contact.create_new_contact(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)






