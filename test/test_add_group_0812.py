# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group0812(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="name1", group_header="header1", group_footer="footer1"))
    app.session.logout()

def test_add_group0812_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()

