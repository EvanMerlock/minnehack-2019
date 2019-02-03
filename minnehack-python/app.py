from flask import Flask
from flask import render_template
from database import db_access
import psycopg2

app = Flask(__name__)
db = db_access.Database(psycopg2.connect())


@app.route('/', methods=['POST', 'GET'])
def index_page(request):
    if request.method == "GET":
        farms = db.get_all_farms()
        return render_template('index.html', farms=farms, fields=[], blocks=[])
    else:
        if "farmupdate" in request.form:
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(int(request.form['farmselect'].replace("farm_", "")))
            return render_template('index.html', farms=farms, fields=fields, blocks=[])
        elif "farmedit" in request.form:
            pass
        elif "fieldremove" in request.form:
            selected_farm = int(request.form['farmselect'].replace("farm_", ""))
            selected_field = int(request.form['fieldselect'].replace("field_", ""))
            db.remove_field(selected_field)
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(selected_farm)
            return render_template('index.html', farms=farms, fields=fields, blocks=[])
        elif "fieldupdate" in request.form:
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(int(request.form['farmselect'].replace("farm_", "")))
            blocks = db.get_blocks_from_field(int(request.form['fieldselect'].replace("field_", "")))
            return render_template('index.html', farms=farms, fields=fields, blocks=blocks)
        elif "fieldedit" in request.form:
            pass
        elif "blockremove" in request.form:
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(int(request.form['farmselect'].replace("farm_", "")))
            db.remove_block(int(request.form['blockselect'].replace("block_", "")))
            blocks = db.get_blocks_from_field(int(request.form['fieldselect'].replace("field_", "")))
            return render_template('index.html', farms=farms, fields=fields, blocks=blocks)
        elif "blockedit" in request.form:
            pass
        elif "blockupdate" in request.form:
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(int(request.form['farmselect'].replace("farm_", "")))
            blocks = db.get_blocks_from_field(int(request.form['fieldselect'].replace("field_", "")))
            return render_template('index.html', farms=farms, fields=fields, blocks=blocks)
        else:
            # assume farmdelete
            selected_farm = int(request.form['farmselect'].replace("farm_", ""))
            db.remove_farm(selected_farm)
            farms = db.get_all_farms()
            return render_template('index.html', farms=farms, fields=[], blocks=[])




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
