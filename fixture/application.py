from selenium import webdriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_session_valid(self):
        try:

            webdriver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='home'])[1]/preceding::a[3]")
            return True
        except:
                return False



    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()



