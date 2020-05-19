import mysql.connector

mydb = mysql.connector.connect(option_files="mysql_config.conf")

print(mydb)

mydb.close()
