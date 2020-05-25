import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database"]  # Create DB
my_col = my_db["customers"]

my_dict = {"name": "John", "address": "Highway 37"}

my_col.insert_one(my_dict)

my_list = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

my_col.insert_many(my_list)

# print(my_client.list_database_names())
db_list = my_client.list_database_names()
if "my_database" in db_list:
    print("my_database exists.")

col_list = my_db.list_collection_names()
if "customers" in col_list:
    print(my_col.find_one())

my_query = {"address": "Park Lane 38"}
my_query_advanced = {"address": {"$gt": "S"}}
my_query_regex = {"address": {"$regex": "^S"}}

for data in my_col.find(my_query_regex).sort("name", -1):
    print(data)

print("----")
#my_query_del = {"address": "Mountain 21"}

# my_col.delete_one(my_query_del)
#x = my_col.delete_many({})
#print(x.deleted_count, " documents deleted.")

my_query_update = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
for x in my_col.find():
    print(x)

my_query_update_all = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}

x = my_col.update_many(my_query_update_all, new_values)

print(x.modified_count, "documents updated.")
