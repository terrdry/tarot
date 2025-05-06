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
ALLOWED_ORIGINS = [
    'http://127.0.0.1:5000',
    'http://localhost:4000',
]

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
CORS(app, resources={
    r"/*": {
        "origins": ALLOWED_ORIGINS
        # "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        # "allow_headers": ["Content-Type", "Authorization"]
    }
})
# TODO this should be tested to see what effect methods and allow_headers
# CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)  # least restrictive

with app.app_context():
    db.create_all()
    logger.warning("created databases")

app.register_blueprint(card_routes)
app.register_blueprint(reading_routes)
