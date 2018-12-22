from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, photo=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email=None, homepage=None, bday=None, bmonth=None, byear=None, address2=None, phone=None, notes=None, conid=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone = phone
        self.notes = notes
        self.id = conid


    def __repr__(self):
        return "%s:%s" % (self.id, self.group_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_name == other.group_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



