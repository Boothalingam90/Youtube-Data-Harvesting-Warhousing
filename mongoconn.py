import pymongo
class mongo:
    def __init__(self, connectionstring, dbname):
        self.connectionstring = connectionstring
        self.dbname = dbname
    def insert_one(self, collectionname, data):
        # Connect to the database using known good certificates
        client = pymongo.MongoClient(self.connectionstring)

        # If we know the correct database to talk to, we connect like this:
        my_database = client[self.dbname]
        mycol = my_database[collectionname]
        x = mycol.insert_one(data)
        return x.inserted_id
    
    def insert_many(self, collectionname, data):
        # Connect to the database using known good certificates
        client = pymongo.MongoClient(self.connectionstring)

        # If we know the correct database to talk to, we connect like this:
        my_database = client[self.dbname]
        mycol = my_database[collectionname]
        x = mycol.insert_many(data)
        return x.inserted_ids
    
    def get_one(self, collectionname, query):
        # Connect to the database using known good certificates
        client = pymongo.MongoClient(self.connectionstring)

        # If we know the correct database to talk to, we connect like this:
        my_database = client[self.dbname]
        mycol = my_database[collectionname]
        return mycol.find_one(query)
    
    def get(self, collectionname, query):
        # Connect to the database using known good certificates
        client = pymongo.MongoClient(self.connectionstring)

        # If we know the correct database to talk to, we connect like this:
        my_database = client[self.dbname]
        mycol = my_database[collectionname]
        return mycol.find(query)
    
    def del_one(self, collectionname, query):
        # Connect to the database using known good certificates
        client = pymongo.MongoClient(self.connectionstring)

        # If we know the correct database to talk to, we connect like this:
        my_database = client[self.dbname]
        mycol = my_database[collectionname]
        return mycol.delete_one(query)
    
    
# # Retrieve records from a collection matching a query
# cursor = mycol["ChannelData"].find()
# print(cursor)
# # for x in mycol.find():
# #   print(x)

# Check what databases exist on this server
# all_databases = client.list_database_names()
# print(f"This MongoDB server has the databases {all_databases}")

# # Retrieve records from a collection matching a query
# cursor = my_database["records"].find({ "year": 1978 })