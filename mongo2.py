from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')
import datetime
print ("Hello Py World!")
print("I love Python and MongoDB")
amigos = list()
try: 
    nombre  = str(raw_input('Permitame su nombre caballero:'))
    apellidos = str(raw_input('Permitame su apellidos'))
    profesion =  str(raw_input('Permitame su profesion caballero'))
    calle =  str(raw_input('Permitame su profesion calle'))
    num_int = str(raw_input('Permitame su numero interior'))
    colonia  = str(raw_input('Permitame su colonia'))
    ciudad =  str(raw_input('Permitame su ciudad caballero'))
    for x in range(0,2):
        amigo = str(raw_input('como se llama su nombre de su amigo'))
        amigos.append(str(amigo))
except ValueError: 
    print "No es un string"
persona = {
    "nombre": nombre, 
    "apellidos": apellidos,
    "profesion" :profesion,
    "amigos": amigos,
    "registro" :  datetime.datetime.utcnow(),
    "direccion" : { 
        "ciudad" : ciudad, 
        "calle" : calle, 
        "numero_interior" : num_int, 
        "colonia": colonia, 
    },
}
db = client.starwars 
db.Jedis.insert(persona)