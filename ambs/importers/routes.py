from flask import render_template, jsonify, Blueprint
from ambs.models.models import AmbsModel

model_inst = AmbsModel()

importer = Blueprint('importers', __name__)


@importer.route("/imported_drugs")
def imported_drugs():

    meds = model_inst.get_all_med()
    # return jsonify({"all medicines": meds})

    return render_template('importers/index.html', title='importers', len = len(meds), meds=meds)
