from model.contact import Contact

def test_delete_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname=1))
    app.contact.delete_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)-1 == len(new_contact)
    old_contact[0:1] = []
    assert new_contact == old_contact

