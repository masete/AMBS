from flask import Flask
from ambs.config import BaseConfig
from flask_cors import CORS


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    CORS(app)

    from ambs.errors.handlers import errors
    from ambs.dashboard.routes import main
    from ambs.importers.routes import importer
    from ambs.dashboard_ura.routes import ura_dashboard
    from ambs.nda.routes import nda

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(importer)
    app.register_blueprint(nda)
    app.register_blueprint(ura_dashboard)

    return app
