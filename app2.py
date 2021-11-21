import re
import random
from sqlite3.dbapi2 import Error
from flask import Flask, Response,redirect, make_response
from flask import request
from flask import render_template
from web.services import db


# inicializa la app de flask
app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

# inicializa la db y sus valores iniciales
db.init_db()
db.seed_db()

# inicialiaza los tickets y usernames de los usuarios logeados
tickets = []
user_names = []


@app.route('/')
def home():
    # renderizar la pagina principal
    return render_template('index.html', title= 'hola mundo')
   

@app.route('/categories2')
def categories():
    # renderizar todas las categorias
    return render_template('categories2.html', ongs = db.get_ongs()) 


@app.route('/admin/ongs')
def get_ongs():
    # obtiene el ticket q envio el usuario en la cookie (si no se envio es None)
    user_ticket = request.cookies.get('ticket')

    # itera por todos los tickets q estan guardados para saber si el ticket del usuario esta en la lista
    encontrado = False
    i = 0
    for current_ticket in tickets:
        if current_ticket == user_ticket:
            encontrado = True
            break
        else:
            i += 1

    # si se encontro el ticket del usuario en la lista de tickets entonces renderiza todas las ongs
    if encontrado == True:
        return render_template('admin/list_ong.html', ongs = db.get_ongs(), name = user_names[i])
    else:
        # si no lo redirecciona al login
        return redirect('/auth/login')
    

@app.route('/admin/ongs/new')
def new_ong():
    # renderizar el formulario crear una nueva ong
    return render_template('/admin/new_ongs.html')

@app.route('/admin/ongs/save', methods=['POST'])
def create_ong():
    # obtiene el nombre y descricion del formulario q envio el navegador
    name = request.form['name']
    description = request.form['description']

    # creao la ong en la db
    db.create_ongs(name, description)

    # redirecciona a la url '/admin/ongs' (donde se listan todas las ong)
    return redirect('/admin/ongs')


@app.route('/admin/ongs/delete/<id>', methods=['DELETE'])
def delete_ong(id):
    # elimina la ong de la db
    db.delete_ong(id)
    return 'delete'


@app.route('/auth/login')
def login_get():
    # renderizar el formulario para el login
    return render_template('auth/login.html')


@app.route('/auth/login', methods=['POST'])
def login_post():
    # obtine el email y el password del formulario q envio el navegador
    email = request.form.get('email')
    password = request.form.get('password')

    # obtiene todos los usuarios de la db q tengan el email y el password q envio el navegador
    r = db.search_user(email, password)
    # r es una lista q contine los usuarios

    # si no se encontro ningun usuario con el email y el password q envio el navegador
    if len(r) == 0:
        # returno el login nuevamente con un mensaje de error
        return render_template('auth/login.html', error = True)

    # create un tikcket para el usuario y lo anado a la lista de tickets
    global tickets
    ticket = str(random.randint(1000000, 10000000))
    tickets.append(ticket)

    # guarda el name del usuario en la lista de nombres
    global user_names
    user = r[0]
    user_name= user['name']
    user_names.append(user_name)
    
    # crea un response que haga un redirect a la url '/admin/ongs'
    resp = make_response(redirect('/admin/ongs'))

    # guardo el ticket en una cookie
    resp.set_cookie('ticket', ticket)

    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)

