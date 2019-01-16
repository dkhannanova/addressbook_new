from model.group import Group
import string
import random



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix+"".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("name",10),group_header=random_string("header",20), group_footer=random_string("footer", 13))
    for i in range (5)]