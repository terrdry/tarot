from flask import Flask, jsonify
from models import Card, Reading
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from config.config import prodConfig, devConfig
from models import db 

from logging_config import setup_logging
import logging
import os

logger = logging.getLogger(os.path.basename(__file__))
def create_app(name, config):
    app = Flask(name)
    setup_logging(logging.WARNING)
    app.config.from_object(config)
    db.init_app(app)
    return app

app = create_app("tarot", devConfig )

logger.info("what")

with app.app_context():
    db.create_all()
    logger.warn("created databases")

app.register_blueprint(card_routes)
app.register_blueprint(reading_routes)


# def get_db():
#     app.logger.info("In get_db")yy
#     from app import db
#     return db

# # Sanity check route
# @app.route('/')
# def index():
#     return jsonify('Hello World')
