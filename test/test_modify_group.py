from model.group import Group

def test_modify_group(app):
    app.group.modify_group(Group(group_name="modifname3"))
