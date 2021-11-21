from flask import Flask, Response,redirect, make_response
from flask import request
from flask import render_template
from web.services import db


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

db.init_db()
db.seed_db()

@app.route('/')
def home():
    return render_template('index.html', title= 'hola mundo')
   

@app.route('/categories2')
def categories():
    print(request.cookies.get('ticket'))
    return render_template('categories2.html', ongs = db.get_ongs()) 

@app.route('/admin/ongs')
def tables():
    return render_template('admin/list_ong.html', ongs = db.get_ongs())

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

@app.route('/admin/user')
def create_ticket():
    resp = make_response()
    resp.set_cookie('ticket', '4254352345243635464')
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)