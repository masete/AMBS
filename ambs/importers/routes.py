from flask import render_template, jsonify, Blueprint
from ambs.models.models import AmbsModel

model_inst = AmbsModel()

importer = Blueprint('importers', __name__)


@importer.route('/imported_drugs')
def imported_drugs():
    # med_id = 1
    meds = model_inst.get_all_med()

    # meds=model_inst.single_med(med_id)
    # return jsonify({"all medicines": meds})

    return render_template('importers/index.html', title='importers', len = len(meds), meds=meds)

@importer.route('/data')
def data():
    # med_id = 1
    data1 = model_inst.get_chart_data()

      # return jsonify({"all medicines": data})

    return render_template('importers/index.html', title='importers', len = len(data1), data1=data1)


@importer.route('/imported_drugs/<int:med_id>')
def imported_drug_by_id(med_id):
    single_med = model_inst.single_med(med_id)
    return render_template('importers/single_data_field.html', title='importers', single_med=single_med)
    # return jsonify({"medicines per year": single_med})


@importer.route('/imported_by_year')
def imported_drug_by_year():

    meds_per_year = model_inst.query_by_year()
    return jsonify({"medicines per year": meds_per_year})
    # return render_template('importers/single_data_field.html', title='importers', meds_per_year=meds_per_year)


@importer.route('/imported_by_year')
def imported_by_year():
    meds_year = model_inst.query_year()
    return jsonify({"medicines per year": meds_year})
    # return render_template('importers/single_data_field.html', title='importers', meds_year=meds_year)


