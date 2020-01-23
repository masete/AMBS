from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route("/") 
@main.route("/dashboard") 
def dashboard():
    return render_template('dashboard/index.html', title='Dashboard')
