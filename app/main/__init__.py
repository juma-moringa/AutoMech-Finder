from flask import Blueprint
from flask.app import Flask
from .. import config_options
main = Blueprint('main',__name__)
from . import views

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from ..main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app