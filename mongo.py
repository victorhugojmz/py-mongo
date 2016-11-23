from pymongo import MongoClient
import datetime 
client = MongoClient('mongodb://localhost:27017/')
Obi = {
    "name" : "Obi-wan Kenobi", 
    "age" : 12 , 
    "homeworld" : "Tatooine"
    "birth_date" : "datetime.datetime"
    }
db = client.starwars
db.Jedis.insert(Obi)