

import sqlite3
from sqlite3 import Error

class DAO:
    
    conn = None
    database = 'prueba.db'
    
    def createConnection(dbFile):
        try:
            conn = sqlite3.connect(dbFile)
            #print("Conexión establecida con la base de datos")
            return conn
        except Error as e:
            print(e)
    
    @classmethod
    def montarUpdate(self, tabla, datos):
        print("llegué")
        # COMIENZO DE LA SENTENCIA UPDATE
        update = f"UPDATE {tabla} SET "
        i = 1
        # RECORRO EL DICCIONARIO CON LA INFORMACIÓN A ACTUALIZAR. EL SET:
        for key, value in datos.items():
            # COMPRUEBO LA LONGITUD PARA PONERLE EL WHERE DESPUÉS DEL ÚLTIMO DATO
            # Y COMPRUEBO EL TIPO PARA PONERLE O NO COMILLAS
            if i != len(datos):
                if isinstance(value, str):
                    update += f"{key} = '{value}', "
                else:
                    update += f"{key} = {value}, "
            else:
                if isinstance(value, str):
                    update += f"{key} = '{value}' WHERE "
                else:
                    update += f"{key} = {value} WHERE, "
            i += 1
        # DEVUELVO LA SENTENCIA YA MONTADA
        return update