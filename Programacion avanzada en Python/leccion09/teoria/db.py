import sqlite3

def get_connect():
    try:
        conn = sqlite3.connect('mydb.db')
        return conn
    except Exception as e:
        print(e)

def create_db():
    sql = """
            CREATE TABLE IF NOT EXISTS personas(
                id integer primary key autoincrement,
                nombre text not null,
                edad integer not null,
                salario real not null
            );
    """
    db = get_connect()
    cursor = db.cursor()
    cursor.execute(sql)