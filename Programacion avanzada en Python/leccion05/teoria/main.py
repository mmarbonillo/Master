
import sqlite3
from sqlite3 import Error

def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def createTable(conn, sentencia):
    try:
        c = conn.cursor()
        c.execute(sentencia)
    except Error as e:
        print(e)

def dropTable(conn, tabla):
    try:
        conn.execute(f"DROP TABLE IF EXISTS {tabla}")
        print(f"Tabla {tabla} eliminada")
    except Error as e:
        print(e)

def insertProjects(conn, datos):
    try:
        insert = "INSERT INTO projects(name, begin_date, end_date) VALUES(?, ?, ?)"
        c = conn.cursor()
        c.execute(insert, datos)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)

def updateProjects(conn, datos):
    try:
        update = "UPDATE projects SET name = ?, begin_date = ?, end_date = ? WHERE id = ?"
        c = conn.cursor()
        c.execute(update, datos)
        c.commit()
    except Error as e:
        print(e)

def delete(conn, tabla, id):
    try:
        delete = f'DELETE FROM {tabla} WHERE id = {id}'
        c = conn.cursor()
        c.execute(delete)
        conn.commit()
    except Error as e:
        print(e)

def deleteAll(conn, tabla):
    try:
        delete = f'DELETE FROM {tabla}'
        c = conn.cursor()
        c.execute(delete)
        conn.commit()
    except Error as e:
        print(e)

#rutaActual = os.path.dirname(os.path.abspath(__file__))

# if __name__ == '__main__':
#     createConnection('sqllite.db')

def main():
    tablaProjects = """CREATE TABLE IF NOT EXISTS projects (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(60),
                            begin_date DATE NOT NULL,
                            end_date DATE NOT NULL
                            );"""
    tablaTask = """CREATE TABLE IF NOT EXISTS task (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(60),
                        priority INTEGER,
                        status_id INTEGER NOT NULL,
                        project_id INTEGER NOT NULL,
                        begin_date DATE NOT NULL,
                        end_date DATE NOT NULL,
                        FOREIGN KEY (project_id) REFERENCES projects(id)
                        );"""
    
    conn = createConnection('sqllite.db')
    
    if conn is not None:
        print("Conexión establecida")
        dropTable(conn, "projects")
        dropTable(conn, "task")
        createTable(conn, tablaProjects)
        createTable(conn, tablaTask)
    else:
        print("Error al conectar a la base de datos")
    
    with conn:
        # INSERTAR
        datos = ('Introducción de datos con SQLite', '2022-05-15', '2023-05-15')
        projectId = insertProjects(conn, datos)
        print(f"ProjectId --> {projectId}")
        
        # ACTUALIZAR
        updateProjects(conn, ('Intro cambiada', '2021-10-10', '2021-12-12', 1))
    
    
    print("Prueba se SELECT")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    filas = cursor.fetchall()
    
    for fila in filas:
        print(fila)
    

main()