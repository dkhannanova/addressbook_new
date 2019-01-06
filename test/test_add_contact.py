# -*- coding: utf-8 -*-
from selenium import webdriver
import string
import pytest
import random
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix+"".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo=None, title="",
                                            company="", address="", home="", mobile="", work="", fax="", email="",
                                            homepage="", bday=None, bmonth=None, byear=None, address2="", phone="", notes="")] + [
    Contact(firstname=random_string("first",10), middlename=random_string("middle",20), lastname=random_string("last", 13),
          nickname=random_string("nick",12), photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title=random_string("title",12),
          company=random_string("company",12), address=random_string("address",12), home=random_string("home",12), mobile=random_string("mobile",12),
          work=random_string("work",12), fax=random_string("fax",12), email=random_string("email",12),
          homepage=random_string("home",12), bday="1", bmonth="August", byear="1985", address2=random_string("address2",12), phone=random_string("phone",12), notes=random_string("notes",12))

    for i in range (5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)






