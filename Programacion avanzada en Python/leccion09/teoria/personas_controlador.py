from db import get_connect

def get_people():
    db = get_connect()
    cursor=db.cursor()
    query = "select * from personas"
    cursor.execute(query)
    salida = cursor.fetchall()
    db.close()
    return salida


def insert_person(nombre,edad,salario):
    db = get_connect()
    cursor=db.cursor()
    query="insert into personas(nombre,edad,salario) values(?,?,?)"
    param = [nombre,edad,salario]
    cursor.execute(query,param)
    db.commit()
    db.close()
    return True