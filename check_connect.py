import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
try:
    cursor =connection.cursor()
#для просмотра структуры бд mysql: – вебстраницу localhost/phpmyadmin
    cursor.execute("select * from group_list")
# fetchall – возвращает все, что он извлек в виде набора строк.
    for row in cursor.fetchall():
	    print(row)
finally:
	connection.close()
