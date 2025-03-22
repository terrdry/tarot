# Standard Library imports
import os
import logging
from datetime import datetime

# Third-party imports
from flask_sqlalchemy import SQLAlchemy

# Local applicaion imports


logger = logging.getLogger(os.path.basename(__file__))

db = SQLAlchemy()
logger.warning("In models.py")


def get_db():
    from app import db
    logger.info("In get_db")
    return db


class Card(db.Model):
    __tablename__ = "card"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    major = db.Column(db.Boolean, nullable=False)
    img = db.Column(db.String(255), nullable=True)

    # Relationship to Readcard
    readings_relation = db.relationship(
        "Readcard", back_populates='cards_relation')


class Reading(db.Model):
    __tablename__ = "reading"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)
    # position = db.Column(db.Integer, nullable=False)

    cards_relation = db.relationship(
        "Readcard", back_populates="readings_relation")


class Readcard(db.Model):
    __tablename__ = "readcard"

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    read_id = db.Column(db.Integer, db.ForeignKey(
        'reading.id'), nullable=False)

    cards_relation = db.relationship(
        "Card", back_populates='readings_relation')
    readings_relation = db.relationship(
        "Reading", back_populates='cards_relation')
