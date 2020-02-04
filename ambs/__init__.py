from flask import Flask
from ambs.config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    from ambs.errors.handlers import errors
    from ambs.dashboard.routes import main
    from ambs.importers.routes import importer
    from ambs.nda.routes import nda

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(importer)
    app.register_blueprint(nda)

    return app
