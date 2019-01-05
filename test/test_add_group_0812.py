# -*- coding: utf-8 -*-
from model.group import Group
import string
import pytest
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix+"".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("name",10),group_header=random_string("header",20), group_footer=random_string("footer", 13))
    for i in range (5)]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

def test_add_group0812(app, group):
    old_group = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)




