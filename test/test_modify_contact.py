from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname="modified", middlename="middlename", lastname="modified lastname", nickname="nickname", photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title="title",
                                            company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                                            homepage="homepage", bday="1", bmonth="August", byear="1985", address2="address2mod", phone="phone2", notes="notes"))
    app.session.logout()