import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import logging 
logger = logging.getLogger(os.path.basename(__file__))

db = SQLAlchemy()
logger.warning("In models.py")
def get_db():
    from app import db
    logger.info("In get_db") 
    return db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    major = db.Column(db.Boolean, nullable=False)
    img = db.Column(db.String(255), nullable=True)

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)
    position = db.Column(db.Integer, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    card = db.relationship('Card', backref=db.backref('readings', lazy=True))

