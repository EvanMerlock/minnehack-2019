from flask import Flask
from flask import render_template
from database import db_access
import psycopg2

app = Flask(__name__)
db = db_access.Database(psycopg2.connect())


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/farmadd')
def farm_add_page():
    return render_template('farmadd.html')


@app.route('/fieldadd')
def field_add_page():
    return render_template('fieldadd.html')


@app.route('/blockadd')
def block_add_page():
    return render_template('blockadd.html')


@app.route('/cropadd')
def crop_add_page():
    return render_template('cropadd.html')


@app.route('/cropswap')
def crop_swap_page():
    return render_template('cropswap.html')


if __name__ == '__main__':
    app.run()
