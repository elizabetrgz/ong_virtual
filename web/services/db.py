import sqlite3
from flask import app

DB_NAME = 'ong.sqlite'


def get_cursor():
    def dict_factory(c, r):
        d = {}
        for idx, col in enumerate(c.description):
            d[col[0]] = r[idx]
        return d

    c = sqlite3.connect(DB_NAME)
    c.row_factory = dict_factory
    cur = c.cursor()
    return cur


def init_db():
    cursor = get_cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ongs (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) NOT NULL, description VARCHAR(500) NOT NULL, número_de_contacto VARCHAR(10) NOT NULL, dirección VARCHAR(20) NOT NULL,nombre_encargado VARCHAR (50) NOT NULL, número_de_encargado VARCHAR(12) NOT NULL)")
    cursor.connection.commit()
    print("Ong table created")
    cursor.connection.close()


def seed_db():
    cur = get_cursor()
    values = [
        {
            'id': '1',
            'name': 'Idas y Vueltas',
            'description': 'Trabajamos para que las personas puedan migrar sin perder sus derechos y sean respetadas en su dignidad independientemente del país en el que nacieron o en el que residen.',
            'número_de_contacto': '9937 6605',
            'dirección': 'Juan Carlos Gómez 1540, Ciudad Vieja',
            'número_de_encargado': 'Rinche Roodenburg',
            'número_de_encargado': '099 376 605',

        },
        {
            'id': '2',
            'name': 'Idas y Vueltas 2',
            'description': 'ONG dedicada a ayudar a emigrantes a su llegada al pais 2'
        }
    ]
    for ong in values:
        id = ong['id']
        name = ong['name']
        description = ong['description']
        número_de_contacto = ong['número_de_contacto']
        dirección = ong['dirección']
        nombre_encargado = ong['nombre_encargado']
        número_de_encargado = ong['número_de_encargado']

        cur.execute(f'REPLACE INTO ongs (id, name, description) VALUES (\'{id}\', \'{name}\', \'{description}\'), \'{número_de_contacto}\', \'{dirección}\', \'{nombre_encargado}\', \'{número_de_encargado}\'')
    
    cur.connection.commit()
    cur.connection.close()


def get_ongs():
    cur = get_cursor()
    cur.execute('SELECT * FROM ongs')
    list_ong = cur.fetchall()
    cur.connection.close()
    return list_ong
    

def create_ongs(id,name, description, número_de_contacto,dirección,nombre_encargado, número_de_encargado):
    # if name is None:
    #     return "The name is required", 400
    # if len(name) < 3 or len(name) > 50:
    #     return "Invalid name length", 400
    # if description is None:
    #     return "The description is required", 400
    # if len(description) < 3 or len(description) > 100:
    #     return "Invalid description length", 400

    cur = get_cursor()
    cur.execute(f'INSERT INTO ongs (id ,name, description, número_de_contacto, dirección,nombre_encargado, número_de_encargado) VALUES (\'{id}\',\'{name}\', \'{description}\', \'{número_de_contacto}\',  \'{dirección}\',  \'{nombre_encargado}\',  \'{número_de_encargado}\'),')
    cur.connection.commit()
    cur.connection.close()
    return True

def delete_ong(id_ongs):
    cur = get_cursor()
    cur.execute('SELECT * FROM ongs WHERE id =' + id_ongs)
    n = cur.fetchall()
    if len(n) == 0:
        cur.connection.close()
        return None

    cur.execute('DELETE FROM ongs WHERE id = '+id_ongs)
    cur.connection.commit()
    cur.connection.close()
    return True
