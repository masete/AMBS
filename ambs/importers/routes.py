from flask import render_template, Blueprint

importer = Blueprint('importers', __name__)


@importer.route("/importers") 
def importers():
    return render_template('importers/index.html', title='importers')
