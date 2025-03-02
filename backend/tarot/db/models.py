from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.TIMESTAMP)
    date_modified = db.Column(db.TIMESTAMP)
    position = db.Column(db.Integer, nullable=False)
    card_id = db.Column(db.Integer, nullable=False)
