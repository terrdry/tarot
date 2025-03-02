# from flask import Flask
# from core.config import Config
# from db import db  # Import db FIRST
# from api.users import user_routes
# from api.readings import reading_routes

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)

#     # Import models here to avoid circular imports
#     with app.app_context():
#         from db.models import User, Reading
#         db.create_all()

#     # Register blueprints
#     app.register_blueprint(user_routes)
#     app.register_blueprint(reading_routes)

#     return app
from flask import Flask
from core.config import Config
from db import db  # Import db FIRST
from api.users import user_routes
from api.readings import reading_routes
from app import app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import models here to avoid circular imports
    with app.app_context():
        from db.models import User, Reading
        db.create_all()

    # Register blueprints
    app.register_blueprint(user_routes)
    app.register_blueprint(reading_routes)

    return app
# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello"
# # jsonify({"message": "Welcome to the Tarot API"}), 200