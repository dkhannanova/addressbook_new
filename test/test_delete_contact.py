from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname=1))
    app.contact.delete_contact()
