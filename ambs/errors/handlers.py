from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    breadcrumb_content=[
        '404 Error Page',
        'Home',
        '404 error'
    ]
    return render_template('errors/404.html',breadcrumb=breadcrumb_content), 404

@errors.app_errorhandler(403)
def error_403(error):
    breadcrumb_content=[
        '403 Error Page',
        'Home',
        '403 error'
    ]
    return render_template('errors/403.html',breadcrumb=breadcrumb_content), 403


@errors.app_errorhandler(500)
def error_500(error):
    breadcrumb_content=[
        '500 Error Page',
        'Home',
        '500 error'
    ]
    return render_template('errors/500.html',breadcrumb=breadcrumb_content), 500
