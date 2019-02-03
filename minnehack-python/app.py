from flask import Flask, request, render_template, redirect

from Models.Farm import FarmTemplate
from database import db_access
import psycopg2

app = Flask(__name__)
db = db_access.Database(psycopg2.connect("postgresql://farmers_project:yoloswag@104.154.96.65:5432/farmers_project"))


@app.route('/', methods=['POST', 'GET'])
def index_page():
    if request.method == "GET":
        farms = db.get_all_farms()
        print(farms)
        return render_template('index.html', farms=farms, fields=[], blocks=[])
    else:
        if "farmupdate" in request.form:
            farms = db.get_all_farms()
            for item in farms:
                if item.get_name() == request.form['farmselect'].replace("farm_", ""):
                    fields = db.get_fields_from_farm(item.get_id())
                    return render_template('index.html', farms=farms, fields=fields, blocks=[])
            return render_template('index.html', farms=farms, fields=[], blocks=[])
        elif "farmedit" in request.form:
            pass
        elif "fieldremove" in request.form:
            print(request.form)
            selected_farm = int(request.form['farmselect'].replace("farm_", ""))
            selected_field = int(request.form['fieldselect'].replace("field_", ""))
            db.remove_field(selected_field)
            farms = db.get_all_farms()
            fields = db.get_fields_from_farm(selected_farm)
            return render_template('index.html', farms=farms, fields=fields, blocks=[])
        elif "fieldupdate" in request.form:
            farms = db.get_all_farms()
            for item in farms:
                if item.get_name() == request.form['farmselect'].replace("farm_", ""):
                    fields = db.get_fields_from_farm(item.get_id())
                    for item_2 in fields:
                        if item_2.get_name() == request.form['fieldselect'].replace("field_", ""):
                            blocks = db.get_blocks_from_field(item_2.get_id())
                            return render_template('index.html', farms=farms, fields=fields, blocks=blocks)
                    return render_template('index.html', farms=farms, fields=fields, blocks=[])
            return render_template('index.html', farms=farms, fields=[], blocks=[])
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
            for item in farms:
                if item.get_name() == request.form['farmselect'].replace("farm_", ""):
                    fields = db.get_fields_from_farm(item.get_id())
                    for item_2 in fields:
                        if item_2.get_name() == request.form['fieldselect'].replace("field_", ""):
                            blocks = db.get_blocks_from_field(item_2.get_id())
                            return render_template('index.html', farms=farms, fields=fields, blocks=blocks)
                    return render_template('index.html', farms=farms, fields=fields, blocks=[])
            return render_template('index.html', farms=farms, fields=[], blocks=[])
        else:
            # assume farmdelete
            selected_farm = int(request.form['farmselect'].replace("farm_", ""))
            db.remove_farm(selected_farm)
            farms = db.get_all_farms()
            return render_template('index.html', farms=farms, fields=[], blocks=[])




@app.route('/farmadd')
def farm_add_page():
    return render_template('farmadd.html')

@app.route('/addfarmaction', methods=['POST'])
def farm_add_action():
    if request.method == 'POST':
        temp_farm = FarmTemplate(request.form['farmname'], (request.form['farmlongitude'], request.form['farmlatitude']))
        db.add_farm(temp_farm)
        return redirect('/')


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

@app.route('/farmedit', methods=['POST'])
def farm_edit_page():
    return render_template()


if __name__ == '__main__':
    app.run()
