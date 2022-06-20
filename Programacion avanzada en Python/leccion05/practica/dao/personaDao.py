
from sqlite3 import Error
from dao.dao import DAO

class PersonaDAO():
    
    @classmethod
    def createTable(self, sentencia):
        conexion = DAO.createConnection(DAO.database)
        try:
            c = conexion.cursor()
            c.execute(sentencia)
            conexion.close()
            return True
        except Error as e:
            print(e)
    
    def insertPersona(datos):
        conexion = DAO.createConnection(DAO.database)
        try:
            insert = "INSERT INTO personas(name, email) VALUES(?, ?)"
            c = conexion.cursor()
            c.execute(insert, datos)
            conexion.commit()
            conexion.close()
            return c.lastrowid
        except Error as e:
            print(e)

    @classmethod
    def update(self, datos, id):
        conexion = DAO.createConnection(DAO.database)
        update = DAO.montarUpdate("personas", datos)
        update += f"id = {id}"
        print(f"update: {update}")
        try:
            c = conexion.cursor()
            c.execute(update)
            # CON ESTE SELECT SÍ SALE ACTUALIZADA LA TABLA, CON EL DEL MAIN NO.
            # ¿POR QUÉ NO ESPERA A QUE ACABE LA FUNCIÓN?
            # c.execute("select * from personas")
            # filas = c.fetchall()
            # for fila in filas:
            #     print(fila)
            conexion.close()
            return c.lastrowid
        except Error as e:
            print(e)
    
    def delete(id):
        conexion = DAO.createConnection(DAO.database)
        try:
            c = conexion.cursor()
            # buscar = f"SELECT id FROM personas WHERE name LIKE '%{nombre}%'"
            # c.execute(buscar)
            # id = c.fetchone() # Devuelve tupla
            delete = f'DELETE FROM personas WHERE id = {id}'
            c.execute(delete)
            conexion.commit()
            conexion.close()
            return True
        except Error as e:
            print(e)

    def drop():
        conexion = DAO.createConnection(DAO.database)
        try:
            drop = "DROP TABLE personas"
            c = conexion.cursor()
            c.execute(drop)
            conexion.commit()
            conexion.close()
            return True
        except Error as e:
            print(e)

    def truncate():
        conexion = DAO.createConnection(DAO.database)
        try:
            # SQLITE NO TIENE SENTENCIA TRUNCATE. EN VEZ DE ESO IMPLEMENTA QUE, UN DELETE SIN WHERE HACE ESA FUNCIÓN
            truncate = f"DELETE FROM personas"
            c = conexion.cursor()
            c.execute(truncate)
            conexion.commit()
            conexion.close()
            return True
        except Error as e:
            print(e)
    
    def select():
        conexion = DAO.createConnection(DAO.database)
        try:
            cursor = conexion.cursor()
            cursor.execute('select * from personas')
            filas = cursor.fetchall()
            for fila in filas:
                print(fila)
            conexion.close()
        except Error as e:
            print(e)