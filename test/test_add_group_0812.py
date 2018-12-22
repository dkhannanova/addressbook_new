# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group0812(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(group_name="name1", group_header="header1", group_footer="footer1"))
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)


def test_add_group0812_empty(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))


