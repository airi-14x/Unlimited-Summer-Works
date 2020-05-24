import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database"] # Create DB
my_col = my_db["customers"]

my_dict = { "name": "John", "address": "Highway 37"}

my_col.insert_one(my_dict)

my_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

my_col.insert_many(my_list)

#print(my_client.list_database_names())
db_list = my_client.list_database_names()
if "my_database" in db_list:
    print("my_database exists.")

col_list = my_db.list_collection_names()
if "customers" in col_list:
    print(my_col.find_one())

for data in my_col.find():
  print(data)
