from pymongo import MongoClient
import pprint
client = MongoClient('mongodb://localhost:27017/')
Obi = {
    "name" : "Obi-wan Kenobi", 
    "age" : 12 , 
    "homeworld" : "Tatooine"
}
db = client.starwars
db.Jedis.insert(Obi)