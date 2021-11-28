import sqlite3

DB_NAME = 'ong.sqlite'


# crea un cursor para consultar la db
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


# inicializa la db creando sus tablas
def init_db():
    cursor = get_cursor()

    # crear la tabla ongs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ongs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(500) NOT NULL,
            contact_number VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            address VARCHAR(50) NOT NULL,
            manager_name VARCHAR (50) NOT NULL,
            manager_contact VARCHAR(50) NOT NULL
           
        )
    """)

    # crear la tabla users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(50) NOT NULL,
            name VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            role VARCHAR(35)
        )
    """)

    # crear la tabla tickets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value VARCHAR(50) NOT NULL,
            user_id INTEGER NOT NULL
        )
    """)


    # crear la tabla de categorías
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(50) NOT NULL
        )
    """)


    #crear la tabla de departamentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name VARCHAR(50) NOT NULL
        )
    """)


    cursor.connection.commit()
    print("Ong table created")
    print("Users table created")
    print("Tickets table created")
    print("Categories table created")
    print("Departments table created")
    cursor.connection.close()


# inserta en la db los valores inicialies de las tablas users y ongs
def seed_db():
    cur = get_cursor()

    # inicializa las ongs
    ongs = [
        {
            'id': '1',
            'name': 'Idas y Vueltas',
            'description': 'Trabajamos para que las personas puedan migrar sin perder sus derechos y sean respetadas en su dignidad independientemente del país en el que nacieron o en el que residen.',
            'contact_number': '099 376 605',
            'email':'idasyvueltasong@gmail.com',
            'address': 'Juan Carlos Gómez 1540, Ciudad Vieja',
            'manager_name': 'Rinche Roodenburg',
            'manager_contact': '099 376 605',
        },
    ]
    for ong in ongs:
        cur.execute(f"""REPLACE INTO ongs 
            (
                id, 
                name, 
                description, 
                contact_number, 
                email,
                address, 
                manager_name, 
                manager_contact
            ) 
            VALUES (
                '{ong['id']}',
                '{ong['name']}', 
                '{ong['description']}',
                '{ong['contact_number']}', 
                '{ong['email']}',
                '{ong['address']}', 
                '{ong['manager_name']}', 
                '{ong['manager_contact']}'
            )
        """)

    # inicializa los usuarios
    users= [
        {
            'id': '1',
            'email':'elizabetrgz91@gmail.com',
            'name': 'Eizabet',
            'password':'123',
            'role': 'admin',
        },
         {
            'id': '2',
            'email':'aleyva@gmail.com',
            'name': 'Alexander',
            'password':'123',
            'role': 'admin',
        }
    ]
    for user in users:
        cur.execute(f"""REPLACE INTO users 
            (
                id,
                email, 
                name,
                password,
                role 
            ) 
            VALUES (
                '{user['id']}',
                '{user['email']}', 
                '{user['name']}',
                '{user['password']}', 
                '{user['role']}' 
            )
        """)  


    #inicializa la tabla categories
    categories= [
        {
            'id': '1',
            'category_name':'Violencia de Género',
            
        }
    ]
    for category in categories:
        cur.execute(f"""REPLACE INTO categories 
            (
                id,
                category_name
            ) 
            VALUES (
                '{category['id']}',
                '{category['category_name']}' 
                )
        """)   

    cur.connection.commit()
    cur.connection.close()


# devuelve una lista con todas las ongs
def get_ongs():
    cur = get_cursor()
    cur.execute('SELECT * FROM ongs')
    list_ong = cur.fetchall()
    cur.connection.close()
    return list_ong


def find_ong(id):
    cur =get_cursor()
    cur.execute(f'SELECT * FROM ongs WHERE id= "{id}"')
    list_ong = cur.fetchall()
    cur.connection.close()
    if len(list_ong) == 0:
        return None
    return list_ong[0]



# crea una ong en la db con los parametros indicados
def create_ongs(name, description, contact_number, email, address, manager_name, manager_contact):
    # if name is None:
    #     return "The name is required", 400
    # if len(name) < 3 or len(name) > 50:
    #     return "Invalid name length", 400
    # if description is None:
    #     return "The description is required", 400
    # if len(description) < 3 or len(description) > 100:
    #     return "Invalid description length", 400

    cur = get_cursor()
    cur.execute(f"""INSERT INTO ongs (
        name, description, contact_number,email, address,manager_name, manager_contact)
        VALUES (
        \'{name}\', \'{description}\', \'{contact_number}\', \'{email}\', \'{address}\', \'{manager_name}\', \'{manager_contact}\'
        )""")
    cur.connection.commit()
    cur.connection.close()
    return True


def update_ongs(id, name, description, contact_number, email, address, manager_name, manager_contact):
    # if name is None:
    #     return "The name is required", 400
    # if len(name) < 3 or len(name) > 50:
    #     return "Invalid name length", 400
    # if description is None:
    #     return "The description is required", 400
    # if len(description) < 3 or len(description) > 100:
    #     return "Invalid description length", 400

    cur = get_cursor()
    cur.execute(f"""
            UPDATE ongs SET
                name = \'{name}\',
                description = \'{description}\',
                contact_number = \'{contact_number}\', 
                email = \'{email}\', 
                address = \'{address}\', 
                manager_name = \'{manager_name}\',
                manager_contact = \'{manager_contact}\' 
            WHERE id= \'{id}\'
        """)
    cur.connection.commit()
    cur.connection.close()
    return True



# busca la ong por el id, y si exista la elimina de la db
def delete_ong(id_ongs):
    cur = get_cursor()

    # buscar la ong por id
    cur.execute('SELECT * FROM ongs WHERE id =' + id_ongs)
    n = cur.fetchall()

    # si la longitud de la lista es 0, significa q no se encontraron ongs con ese id
    if len(n) == 0:
        cur.connection.close()
        return None

    # elimina la ong de la db por el id dado
    cur.execute('DELETE FROM ongs WHERE id = '+ id_ongs)
    cur.connection.commit()
    cur.connection.close()
    return True


# devuelve un usuario de la db q tenga el email y password indicado, o null
def search_user(email, password):
    cur =get_cursor()
    cur.execute(f'SELECT * FROM users WHERE email= "{email}" and password= "{password}"')
    list_users = cur.fetchall()
    cur.connection.close()
    if len(list_users) == 0:
        return None
    return list_users[0]


# devuelve el usuario (dictionario) con el id indicado, o null
def find_user(user_id):
    cur =get_cursor()
    cur.execute(f'SELECT * FROM users WHERE id= "{user_id}"')
    list_users = cur.fetchall()
    cur.connection.close()
    if len(list_users) == 0:
        return None
    return list_users[0]


def create_tikets(value, user_id):
    cur=get_cursor()
    cur.execute(f'INSERT INTO tickets(value, user_id) VAlUES (\'{value}\', \'{user_id}\')')
    cur.connection.commit()
    cur.connection.close()


def find_ticket (ticket_value):
    cur =get_cursor()
    cur.execute (f'SELECT * FROM tickets WHERE value = "{ticket_value}"' )
    list_tickets = cur.fetchall()
    cur.connection.close()
    if len(list_tickets) == 0:
        return None
    return list_tickets[0]


def delete_ticket(ticket_value):
    cur = get_cursor()
    cur.execute('DELETE FROM tickets WHERE value = '+ ticket_value)
    cur.connection.commit()
    cur.connection.close()
    return True

# funciones  para listar categorias, agregar nuevas categorias y borrar categorias


# devuelve una lista con todas las categorias
def get_categories():
    cur = get_cursor()
    cur.execute('SELECT * FROM categories')
    list_categories = cur.fetchall()
    cur.connection.close()
    return list_categories


# crea una categoria en la db con los parametros indicados
def create_categories(category_name):
    # if name is None:
    #     return "The name is required", 400
    # if len(name) < 3 or len(name) > 50:
    #     return "Invalid name length", 400
    # if description is None:
    #     return "The description is required", 400
    # if len(description) < 3 or len(description) > 100:
    #     return "Invalid description length", 400

    cur = get_cursor()
    cur.execute(f'INSERT INTO categories (category_name) VALUES (\'{category_name}\')')
    cur.connection.commit()
    cur.connection.close()
    return True


# busca la categoria por el id, y si exista la elimina de la db
def delete_categories(id_category):
    cur = get_cursor()

    # buscar la categoria por id
    cur.execute('SELECT * FROM categories WHERE id =' + id_category)
    n = cur.fetchall()

    # si la longitud de la lista es 0, significa q no se encontraron ongs con ese id
    if len(n) == 0:
        cur.connection.close()
        return None

    # elimina la ong de la db por el id dado
    cur.execute('DELETE FROM categories WHERE id = '+ id_category)
    cur.connection.commit()
    cur.connection.close()
    return True

