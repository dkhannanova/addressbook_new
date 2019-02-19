from model.group import Group
import random

def test_delete_first_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test_name"))
    old_group = db.get_group_list()
    group = random.choice(old_group)
    app.group.delete_group_by_id(group.id)
    assert len(old_group) - 1 == app.group.count()
    new_group = db.get_group_list()
    old_group.remove(group)
    assert old_group == new_group
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
