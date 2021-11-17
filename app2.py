from flask import Flask, Response
from flask import request
from flask import render_template
from web.services import db


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

db.init_db()
db.seed_db()

ongs = db.get_ongs()
print(ongs)
print('<ul>')
for d in ongs:
    print('<li>')
    print('<p>nombre: <b>'+ d['name'] +'</b></p>')
    print('<p>descipcion: <b>'+ d['description'] +'</b></p>')
    print ('</li>')
print ('</ul>')

@app.route('/')
def home():
    return render_template('index.html', title= 'hola mundo')

@app.route('/categories2')
def categories():
    return render_template('categories2.html')

@app.route('/table')
def tables():
    return render_template('table.html', ongs = db.get_ongs())


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)