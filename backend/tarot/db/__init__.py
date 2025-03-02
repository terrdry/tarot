# from flask import Flask
# from core.config import Config
# # from db import db
# from api.users import user_routes
# from api.readings import reading_routes

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)

#     # Register blueprints
#     app.register_blueprint(user_routes)
#     app.register_blueprint(reading_routes)

#     with app.app_context():
#         db.create_all()

#     return app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
