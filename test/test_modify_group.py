from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="name1", group_header="header1", group_footer="footer1"))
    app.group.modify_group(Group(group_name="modifname3"))
