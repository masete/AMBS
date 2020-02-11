from flask import render_template, Blueprint
from ambs.models.models import AmbsModel
from flask import jsonify
ura_dashboard = Blueprint('ura_dashboard', __name__)

nda_inst = AmbsModel()


@ura_dashboard.route("/ura_data")
def dashboard():
    ura_chart_data = nda_inst.get_co_name()
    count = []
    co_name = []

    for item in ura_chart_data:
        count.append(item['count'])
        co_name.append(item['co_name'])

    # dist = nda_chart_data.drugshop
    # print (dist)
    # return jsonify(ura_chart_data)

    return render_template('dashboard/ura_index.html', co_name=co_name, count=count, ura_chart_data=ura_chart_data)


