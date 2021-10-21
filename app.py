from flask import Flask
from flask import request
import sqlite3


# app = Flask(__name__)
#
#
# @app.route('/api/ongs/')
# def ongs_get():
#     cur = get_cursor()
#     cur.execute('SELECT * FROM ongs')
#     list_ong = cur.fetchall()
#     cur.connection.close()
#     return {'ongs': list_ong}
#
#
# @app.route('/api/ongs/<id_ongs>')
# def ongs_id_get(id_ongs):
#     cur = get_cursor()
#     cur.execute("SELECT * FROM ongs  WHERE id = " + id_ongs)
#     a = cur.fetchall()
#     cur.connection.close()
#     if len(a) == 0:
#         return "Not found", 400
#     return a[0]
#
#
# @app.route('/api/ongs/', methods=['POST'])
# def create_ongs():
#     name = request.json.get('name')
#     description = request.json.get('description')
#
#     if name is None:
#         return "The name is required", 400
#     if len(name) < 3 or len(name) > 50:
#         return "Invalid name length", 400
#     if description is None:
#         return "The description is required", 400
#     if len(description) < 3 or len(description) > 100:
#         return "Invalid description length", 400
#
#     cur = get_cursor()
#     cur.execute(f'INSERT INTO ongs (name, description) VALUES (\'{name}\', \'{description}\')')
#     cur.connection.commit()
#
#     cur.execute("SELECT * FROM ongs  WHERE id = " + str(cur.lastrowid))
#     a = cur.fetchall()
#     cur.connection.close()
#     return a[0], 200
#
#
# @app.route('/api/ongs/<id_ongs>', methods=['PUT'])
# def ongs_update(id_ongs):
#     name = request.json.get('name')
#     description = request.json.get('description')
#
#     if name is not None and (len(name) < 3 or len(name) > 50):
#         return "Invalid name length", 400
#     if description is not None and (len(description) < 3 or len(description) > 100):
#         return "Invalid description length", 400
#
#     cur = get_cursor()
#     cur.execute("SELECT * FROM ongs  WHERE id = " + id_ongs)
#     rows = cur.fetchall()
#     if len(rows) == 0:
#         cur.connection.close()
#         return "Not found", 400
#     ong = rows[0]
#
#     if name is None:
#         name = ong['name']
#     if description is None:
#         description = ong['description']
#
#     cur.execute(f'UPDATE ongs SET name = \'{name}\', description = \'{description}\'  WHERE id= ' + id_ongs)
#     cur.connection.commit()
#     cur.execute("SELECT * FROM ongs  WHERE id = " + id_ongs)
#     a = cur.fetchall()
#     cur.connection.close()
#     return a[0], 200
#
#
# @app.route('/api/ongs/<id_ongs>', methods=['DELETE'])
# def delete_ong(id_ongs):
#     cur = get_cursor()
#     cur.execute('SELECT * FROM ongs WHERE id =' + id_ongs)
#     n = cur.fetchall()
#     if len(n) == 0:
#         cur.connection.close()
#         return "Not found", 400
#
#     cur.execute('DELETE FROM ongs WHERE id = '+id_ongs)
#     cur.connection.commit()
#     cur.connection.close()
#     return "Not found", 400
#
#
# def dict_factory(c, r):
#     d = {}
#     for idx, col in enumerate(c.description):
#         d[col[0]] = r[idx]
#     return d
#
#
# def get_cursor():
#     c = sqlite3.connect('ong.db')
#     c.row_factory = dict_factory
#     cur = c.cursor()
#     return cur
#
#
# def init_db():
#     cursor = get_cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS ongs (id  INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), description VARCHAR(100))")
#     cursor.connection.commit()
#     print("Ong table created")
#     cursor.connection.close()
#
#
# init_db()
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#






