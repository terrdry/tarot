# Standard Library imports
import os
import logging

# Third-party imports
from flask import Flask
from flask import jsonify
from flask_cors import CORS

# Local applicaion imports
from models import Card
from models import Reading
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from config.config import devConfig
from config.config import prodConfig
from models import db
from logging_config import setup_logging

logger = logging.getLogger(os.path.basename(__file__))


def create_app(name, config):
    """create_app Create the Flask Application

    This will create the application instance and return
    the app handle for subsequent use by other modules using
    a simple import

    Args:
        name (String): Flask application name
        config (object): Name of `Class` in config/config

    Returns:
        object: Flask app
    """

    app = Flask(name)
    setup_logging(logging.WARNING)
    app.config.from_object(config)
    db.init_app(app)
    return app


app = create_app("tarot", devConfig)
# CORS(app, resources={r"/*": {"origins": "http://localhost:4000"}})
CORS(app, resources={r"/*": {"origins": "*"}})
with app.app_context():
    db.create_all()
    logger.warning("created databases")

app.register_blueprint(card_routes)
app.register_blueprint(reading_routes)
