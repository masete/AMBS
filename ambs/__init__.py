from flask import Flask
from .config import BaseConfig
from flask_cors import CORS
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     get_jwt_identity
# )



def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    # app.config['JWT_SECRET_KEY'] = 'mugisha-sylivin'  # Change this!
    # jwt = JWTManager(app)

    CORS(app)

    from ambs.errors.handlers import errors
    from ambs.dashboard.routes import main
    from ambs.importers.routes import importer
    from ambs.auth.login import auth
    from ambs.dashboard_ura.routes import ura_dashboard
    from ambs.nda.routes import nda

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(importer)
    app.register_blueprint(auth)
    app.register_blueprint(nda)
    app.register_blueprint(ura_dashboard)

    return app
