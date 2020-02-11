from flask import render_template, Blueprint
from ambs.models.nda_models import NdaDataModel

main = Blueprint('main', __name__)

nda_inst = NdaDataModel()
@main.route("/") 
# @main.route("/dashboard")
def dashboard():
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


# return render_template('dashboard/index.html', title='Dashboard')
