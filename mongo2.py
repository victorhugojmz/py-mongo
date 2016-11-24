from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')
print ("Hello World!")
print("I love Python and MongoDB")
try: 
    nombre  = str(raw_input('Permitame su nombre caballero:'))
    apellidos = str(raw_input('Permitame su apellidos'))
    profesion =  str(raw_input('Permitame su profesion caballero'))
except ValueError: 
    print "No es un string"
persona = {
    "nombre": nombre, 
    "apellidos": apellidos,
    "profesion" :profesion 
}
db = client.starwars 
db.Jedis.insert(persona)