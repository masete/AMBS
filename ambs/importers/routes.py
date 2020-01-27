from flask import render_template, Blueprint
from ambs.models.models import AmbsModel

importer = Blueprint('importers', __name__)


@importer.route("/imported_drugs")
def imported_drugs():
    return render_template('importers/index.html', title='importers')
