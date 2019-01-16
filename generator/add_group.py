from model.group import Group
import string
import random
import os.path
import json




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix+"".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("name",10),group_header=random_string("header",20), group_footer=random_string("footer", 13))
    for i in range (5)]


#склейка родительской директории текущего файла и названия файла, в который будут записаны тестовые данные, вложенная функция определяет абсолютный путь к текущему файлу
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

#открываем файл для записи по пути path для записи в него сгенерированных данных
with open(path, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__))
