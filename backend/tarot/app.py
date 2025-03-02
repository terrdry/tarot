from flask import Flask, jsonify
from core.config import Config
from db.models import User, Reading
from db import db
from api.users import user_routes
from api.readings import reading_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register blueprints
app.register_blueprint(user_routes)
app.register_blueprint(reading_routes)

@app.route('/')
@app.route('/index')
def index():
    return "hello"
# jsonify({"message": "Welcome to the Tarot API"}), 200

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(user_routes)
    app.register_blueprint(reading_routes)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)

# from app import appdd