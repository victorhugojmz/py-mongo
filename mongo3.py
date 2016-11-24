from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')
print("---------- Python and MongoDB Part 3")
db = client.starwars 
for documento in db.Jedis.find({}):
    print documento 


