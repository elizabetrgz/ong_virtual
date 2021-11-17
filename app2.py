from flask import Flask, Response
from flask import request
from flask import render_template
from web.services import db


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

db.init_db()
db.seed_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/categories2')
def categories():
    return render_template('categories2.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)