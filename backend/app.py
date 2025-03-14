from flask import Flask, jsonify
from models import Card, Reading
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from config.config import prodConfig, devConfig
from models import db 

def create_app(name, config):
    app = Flask(name)
    app.config.from_object(config)
    db.init_app(app)
    return app

app = create_app("tarot", devConfig )


with app.app_context():
    db.create_all()

app.register_blueprint(card_routes)
app.register_blueprint(reading_routes)


def get_db():
    from app import db
    return db

# Sanity check route
@app.route('/')
def index():
    return jsonify('Hello World')
