# Standard Library imports
import os
import logging

# Third-party imports
from flask import Flask, jsonify

# Local applicaion imports
from models import Card, Reading
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from config.config import prodConfig, devConfig
from models import db 
from logging_config import setup_logging

logger = logging.getLogger(os.path.basename(__file__))

def create_app(name, config):
    """create_app 
    Create the Flask application
    This was modularized to be callable in imports

    Args:
        name (String): Name of APP
        config (object): Name of options in config/config

    Returns:
        NoneValue : null
    """
    app = Flask(name)
    setup_logging(logging.WARNING)
    app.config.from_object(config)
    db.init_app(app)
    return app

app = create_app("tarot", devConfig )

logger.info("what")

with app.app_context():
    db.create_all()
    logger.warning("created databases")

app.register_blueprint(card_routes)
app.register_blueprint(reading_routes)

