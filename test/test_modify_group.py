from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(group_name="modifname1", group_header="modifheader1", group_footer="modiffooter1"))
    app.session.logout()