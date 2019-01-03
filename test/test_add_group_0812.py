# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group0812(app):
    old_group = app.group.get_group_list()
    group = Group(group_name="name1", group_header="header1", group_footer="footer1")
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


#def test_add_group0812_empty(app):
 #   old_group = app.group.get_group_list()
  #  group = Group(group_name="", group_header="", group_footer="")
   # app.group.create(group)
    #new_group = app.group.get_group_list()
    #assert len(old_group) + 1 == len(new_group)
    #old_group.append(group)
    #assert sorted(old_group, key = Group.id_or_max) == sorted(new_group, key = Group.id_or_max)

