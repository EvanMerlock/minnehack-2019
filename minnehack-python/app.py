from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def indexpage():
    return render_template('index.html')


@app.route('/farmadd')
def farmaddpage():
    return render_template('farmadd.html')


@app.route('/fieldadd')
def fieldaddpage():
    return render_template('fieldadd.html')


@app.route('/blockadd')
def blockaddpage():
    return render_template('blockadd.html')


@app.route('/cropadd')
def cropaddpage():
    return render_template('cropadd.html')


@app.route('/cropswap')
def cropswappage():
    return render_template('cropswap.html')


if __name__ == '__main__':
    app.run()
