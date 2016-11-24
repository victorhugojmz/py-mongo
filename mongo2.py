from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')
print ("Hello World!")
print("I love Python and MongoDB")
amigos = list()
try: 
    nombre  = str(raw_input('Permitame su nombre caballero:'))
    apellidos = str(raw_input('Permitame su apellidos'))
    profesion =  str(raw_input('Permitame su profesion caballero'))
    for x in range(0,5):
        amigo = str(raw_input('como se llama su nombre de su amigo'))
        amigos.append(str(amigo))
except ValueError: 
    print "No es un string"
persona = {
    "nombre": nombre, 
    "apellidos": apellidos,
    "profesion" :profesion,
    "amigos": amigos
}
db = client.starwars 
db.Jedis.insert(persona)