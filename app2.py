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
    ticket_value = request.cookies.get('ticket')
    ticket = db.find_ticket (ticket_value)
    if ticket == None:
        return redirect('/auth/login')
    else:
        user_id = ticket['user_id']
        user = db.find_user(user_id)
        return render_template('admin/list_ong.html', ongs = db.get_ongs(), name = user['name'])     
    

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

    # obtiene el usuario de la db q tengan el email y el password q envio el navegador
    user = db.search_user(email, password)

    # si no se encontro ningun usuario con el email y el password q envio el navegador
    if user == None:
        # returno el login nuevamente con un mensaje de error
        return render_template('auth/login.html', error = True)

    # create un tikcket para el usuario y lo anado a la lista de tickets
    ticket_value = str(random.randint(1000000, 10000000))
    user_id= user['id']
    db.create_tikets(ticket_value, user_id)

    # crea un response que haga un redirect a la url '/admin/ongs'
    resp = make_response(redirect('/admin/ongs'))

    # guardo el ticket_value en una cookie
    resp.set_cookie('ticket', ticket_value)

    return resp

@app.route('/auth/logout', methods = ['POST'])
def logout ():
    ticket_value = request.cookies.get('ticket')
    db.delete_ticket(ticket_value)
    return redirect('/auth/login')


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)

