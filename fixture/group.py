class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.group_name)
        self.change_field("group_header", group.group_header)
        self.change_field("group_footer", group.group_footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group fields
        self.fill_group(group)
        # submit group data
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # modify group
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        # submit group data
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        wd.find_element_by_id("logo").click()

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))