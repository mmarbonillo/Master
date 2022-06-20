
from sqlite3 import Error
from dao.dao import DAO

class MascotaDAO():
    
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
    
    def insertMascotas(datos):
        conexion = DAO.createConnection(DAO.database)
        try:
            insert = "INSERT INTO mascotas(name, fecha_nacimiento, tipo, persona_id) VALUES(?, ?, ?, ?)"
            c = conexion.cursor()
            c.execute(insert, datos)
            conexion.commit()
            conexion.close()
            return c.lastrowid
        except Error as e:
            print(e)
    
    def update(datos, id):
        conexion = DAO.createConnection(DAO.database)
        update = DAO.montarUpdate("mascotas", datos)
        update += f"id = {id}"
        try:
            c = conexion.cursor()
            c.execute(update)
            # c.execute("select * from mascotas")
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
            delete = f'DELETE FROM mascotas WHERE id = {id}'
            c = conexion.cursor()
            c.execute(delete)
            conexion.commit()
            conexion.close()
            return True
        except Error as e:
            print(e)

    def drop():
        conexion = DAO.createConnection(DAO.database)
        try:
            drop = "DROP TABLE mascotas"
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
            truncate = f"DELETE FROM mascotas"
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
            cursor.execute('select * from mascotas')
            filas = cursor.fetchall()
            for fila in filas:
                print(fila)
            conexion.close()
        except Error as e:
            print(e)