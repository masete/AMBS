from flask import render_template, jsonify, Blueprint
from ambs.models.models import AmbsModel
from ambs.models.nda_models import NdaDataModel

model_inst = AmbsModel()
nda_inst = NdaDataModel()

nda = Blueprint('nda', __name__)


@nda.route('/nda_data')
def nda_get_data():
    # med_id = 1
    data = nda_inst.get_nda_data()

    # return jsonify({"all nda": data})

    return render_template('nda/index.html', title='nda', len = len(data), data=data)


@nda.route('/nda_data')
def nda_get_district():
    # med_id = 1
    districts = nda_inst.get_district()

    # return jsonify({"all nda": data})

    return render_template('nda/index.html', title='nda', len = len(districts), districts=districts)


@nda.route('/nda_data')
def nda_get_drugshop():
    # med_id = 1
    drugshop = nda_inst.get_drugshop()

    # return jsonify({"all nda": data})

    return render_template('nda/index.html', title='nda', len = len(drugshop), drugshop=drugshop)
