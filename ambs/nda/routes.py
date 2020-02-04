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

    return render_template('nda/index.html', title='nda', len=len(data), data=data)


@nda.route('/nda_district')
def nda_get_district_drugshop():
    # med_id = 1
    nda_chart_data = nda_inst.get_district()
    count = []
    district = []

    for item in nda_chart_data:
        count.append(item['count'])
        district.append(item['district'])

    # dist = nda_chart_data.drugshop
    # print (dist)
    # return jsonify(district)

    return render_template('dashboard/index.html', district=district, count=count, nda_chart_data=nda_chart_data)


# @nda.route('/nda_rugshop')
# def nda_get_drugshop():
#     # med_id = 1
#     drugshop = nda_inst.get_drugshop()
#
#     return jsonify({"drug shop": drugshop})

    # return render_template('dashboard/index.html', title='nda', len = len(drugshop), drugshop=drugshop)
