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


@importer.route('/filtered_imported_drugs/')
def filtered_fields(AGENT,CO_NAME,RCPT_DATE,SUPP_QTY):
    filtered_list = model_inst.get_most_needed_med(AGENT, CO_NAME, RCPT_DATE, SUPP_QTY)

    return render_template('importers/index.html', title='importers', len=len(filtered_list), filtered_list=filtered_list)
    # return jsonify({"filtered fields from medicine table": filtered_list})


@importer.route('/imported_drugs/<int:med_id>')
def imported_drug_by_id(med_id):
    meds_per_year = model_inst.single_med(med_id)

    return jsonify({"medicines per year": meds_per_year})


@importer.route('/imported_drugs/<int:ASS_DATE>')
def imported_drugs_annually(ASS_DATE):
    meds_per_year = model_inst.drugs_per_year(ASS_DATE)

    return jsonify({"medicines per year": meds_per_year})



# def imported_drugs_annually():
