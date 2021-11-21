import re
import random
from sqlite3.dbapi2 import Error
from flask import Flask, Response,redirect, make_response
from flask import request
from flask import render_template
from web.services import db


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

db.init_db()
db.seed_db()

ticket = None
user_name = None


@app.route('/')
def home():
    return render_template('index.html', title= 'hola mundo')
   

@app.route('/categories2')
def categories():
    print(request.cookies.get('ticket'))
    return render_template('categories2.html', ongs = db.get_ongs()) 


@app.route('/admin/ongs')
def get_ongs():
    user_ticket = request.cookies.get('ticket')
    if user_ticket == None or user_ticket != ticket:
        return redirect('/auth/login')
    
    print('el user name es:' + user_name)
    return render_template('admin/list_ong.html', ongs = db.get_ongs(), name = user_name)


@app.route('/admin/ongs/new')
def new_ong():
    return render_template('/admin/new_ongs.html')

@app.route('/admin/ongs/save', methods=['POST'])
def create_ong():
    name = request.form['name']
    description = request.form['description']
    db.create_ongs(name, description)
    return redirect('/admin/ongs')


@app.route('/admin/ongs/delete/<id>', methods=['DELETE'])
def delete_ong(id):
    db.delete_ong(id)
    return 'delete'


@app.route('/auth/login')
def login_get():
    return render_template('auth/login.html')


@app.route('/auth/login', methods=['POST'])
def loguin_post():
    # obtine el email y el password del formulario q envio el navegador
    email = request.form.get('email')
    password = request.form.get('password')

    # obtiene todos los usuarios de la db q tengan el email y el password q envio el navegador
    r = db.search_user(email, password)
    # r es una lista q contine los usuarios

    # si no se encontro ningun usuario con el email y el password q envio el navegaro
    if len(r) == 0:
        # returno el login nuevamente con un mensaje de error
        return render_template('auth/login.html', error = True)

    # create un tikcket para el usuario
    global ticket
    ticket = str(random.randint(1000000, 10000000))

    # guarda el name del usuario q se le da el ticket
    global user_name
    user = r[0]
    user_name= user['name']

    print(ticket)
    print(user_name)
    
    # crearun response que haga un redirect a la url '/admin/ongs'
    resp = make_response(redirect('/admin/ongs'))

    # guardo el ticket en una cookie
    resp.set_cookie('ticket', ticket)

    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)