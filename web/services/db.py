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
    cursor.execute("CREATE TABLE IF NOT EXISTS ongs (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), description VARCHAR(500))")
    cursor.connection.commit()
    print("Ong table created")
    cursor.connection.close()


def seed_db():
    cur = get_cursor()
    values = [
        {
            'id': '1',
            'name': 'Idas y Vueltas',
            'description': 'ONG dedicada a ayudar a emigrantes a su llegada al pais'
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
        cur.execute(f'REPLACE INTO ongs (id, name, description) VALUES (\'{id}\', \'{name}\', \'{description}\')')
    
    cur.connection.commit()
    cur.connection.close()


def get_ongs():
    cur = get_cursor()
    cur.execute('SELECT * FROM ongs')
    list_ong = cur.fetchall()
    cur.connection.close()
    return list_ong
    



