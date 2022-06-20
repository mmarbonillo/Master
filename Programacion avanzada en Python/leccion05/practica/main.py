
# Actividad relacionada con la lección 5: Crea en Python una función 
# que genere una BBDD Sqlite3
# Partiendo de la BBDD generada, crea una función que genere las siguientes tablas:
# •Una tabla con 4 campos
# •Una tabla con 2 campos

# Crea una función para cada una de las siguientes sentencias que opere 
# sobre las tablas creadas:
# •Insertar
# •Actualizar
# •Listar
# •Borrar

'''
Hay mil cosas que no se por qué funcionan así.
¿Por qué hay métodos que me obligan a pasar el SELF y otros no?
¿Por qué me obliga a pasar SELF en métodos de clase? Si no necesitan objeto, son de clase, ¿Qué es SELF ahí?
¿Por qué tengo que abrir conexión cada vez que quiero usarla aunque no la cierre previamente?
    Si comento en PersonaDAO el conexion.close() y en MascotaDAO el createConection(), crea bien la tabla de Personas pero con la de Mascotas salta error: AttributeError: 'NoneType' object has no attribute 'cursor'
    No entiendo por qué si DAO.conn es un método de clase
'''

from database import *
from models.persona import Persona
from models.mascota import Mascota
from database import *

'''
----------------- ABRIMOS CONEXIÓN ---------------------
'''
# conn = DAO.createConnection('prueba.db')

'''
------------------ CREAR TABLAS ------------------------
'''

personas = """CREATE TABLE IF NOT EXISTS personas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(150) NOT NULL
                        );"""
mascotas = """CREATE TABLE IF NOT EXISTS mascotas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(60),
                    fecha_nacimiento DATE NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    persona_id INTEGER NOT NULL,
                    FOREIGN KEY ('persona_id') REFERENCES personas(id)
                    );"""

Persona.drop()
Mascota.drop()
Persona.createTable(personas)
Mascota.createTable(mascotas)

'''
ELIMINO EL CONTENIDO DE LAS TABLAS PARA QUE CADA VEZ QUE EJECUTE EL MAIN, SE VACÍEN
PARA HACER BIEN Y LIMPIAS LAS PRUEBAS
'''
# truncate(conn, "personas")
# truncate(conn, "mascotas")

'''
------------------ INSERTAR DATOS EN TABLA PERSONAS -------------------
'''
p1 = Persona("Carmen", "carmen@gmail.com")
p2 = Persona("Juan", "juan@gmail.com")
p3 = Persona("María", "maria@gmail.com")
p4 = Persona("Jose", "jose@gmail.com")
p5 = Persona("Juana", "juana@gmail.com")
p6 = Persona("Carlos", "carlos@gmail.com")
p7 = Persona("Lucía", "lucia@gmail.com")
p8 = Persona("María del Carmen", "mdc@gmail.com")
p9 = Persona("Jose Juan", "jj@gmail.com")
p10 = Persona("Félix", "felix@gmail.com")
datosPersonas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for persona in datosPersonas:
    persona.insert()

'''
------------------ INSERTAR DATOS EN TABLA MASCOTAS -------------------
'''

m1 = Mascota("Tina", "15-06-2006", "gato", 3)
m2 = Mascota("Manchi", "20-08-2016", "gato", 3)
m3 = Mascota("Luna", "25-01-2009", "perro", 1)
m4 = Mascota("Perico", "01-06-2006", "pajaro", 10)
m5 = Mascota("Rex", "12-03-2012", "perro", 1)
m6 = Mascota("Bobby", "15-06-2006", "pajaro", 4)
datosMascotas = [m1, m2, m3, m4, m5, m6]
for mascota in datosMascotas:
    mascota.insert()

'''
ELIMINO REGISTRO PARA COMPROBAR SI SQLITE TIENE O NO INTEGRIDAD REFERENCIAL.
NO TIENE
'''
# print(p3.delete())

'''
------------------------ HAGO UN UPDATE ------------------------
'''

# datosCampos = {"name": "Alberto"}
# p1.update(datosCampos)
# Persona.select()

# m2.update({"name": "Shera"})

'''
ELIMINO PERSONAS
'''
# Persona.drop()
# Persona.select()

'''
VACÍO LA TABLA 
'''
# Persona.truncate()
# print("TRUNCATE")
# Persona.select()