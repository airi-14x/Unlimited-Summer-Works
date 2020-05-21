# Python 3.7
import mysql.connector

my_db = mysql.connector.connect(option_files="mysql_config.conf")

my_cursor = my_db.cursor()
print(my_cursor)
# Database names are UNIQUE
#my_cursor.execute("CREATE DATABASE mydatabase")

my_cursor.execute("SHOW DATABASES")

for database in my_cursor:
    print(database)

my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print(table)

# Table names are UNIQUE
#my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# my_cursor.execute(
#    "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# my_cursor.execute(
#    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
# )

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
my_cursor.commit()
print(my_cursor.rowcount, "record inserted.")
'''

'''
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

my_cursor.executemany(sql, val)

my_cursor.commit()
print(my_cursor.rowcount, "record inserted.")
print("Last ID: ", my_cursor.lastrowid)
'''

#my_cursor.execute("SELECT * FROM customers")
#my_cursor.execute("SELECT name, address FROM customers")
#one_result = my_cursor.fetchone()
# print(one_result)

#sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
#sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# my_cursor.execute(sql)

# ESCAPING CHARACTERS
'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
my_cursor.execute(sql, adr)
'''

#sql = "SELECT * FROM customers ORDER BY name"
#sql = "SELECT * FROM customers ORDER BY name DESC"
#sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
'''
results = my_cursor.fetchall()

for result in results:
    print(result)
'''

# Better DELETE
'''
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
my_cursor.execute(sql, adr)
my_db.commit()

print(my_cursor.rowcount, "record(s) deleted")
'''

# DROP
'''
sql = "DROP TABLE IF EXISTS customers"
my_cursor.execute(sql)
'''

# UPDATE
#sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
my_cursor.execute(sql, val)
my_db.commit()
print(my_cursor.rowcount, "record(s) affected")

#sql = "SELECT * FROM customers LIMIT 5"
sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
my_cursor.execute(sql)
results = my_cursor.fetchall()

for result in results:
    print(result)

my_db.close()
