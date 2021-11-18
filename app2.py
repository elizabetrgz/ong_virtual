from flask import Flask, Response,redirect
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
    return render_template('categories2.html')

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


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)