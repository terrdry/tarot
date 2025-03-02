from flask import Blueprint, request, jsonify
from db.models import db, Reading

reading_routes = Blueprint('reading_routes', __name__)

@reading_routes.route('/readings', methods=['POST'])
def create_reading():
    data = request.get_json()
    new_reading = Reading(position=data['position'], card_id=data['card_id'])
    db.session.add(new_reading)
    db.session.commit()
    return jsonify({'id': new_reading.id, 'position': new_reading.position, 'card_id': new_reading.card_id}), 201

@reading_routes.route('/readings', methods=['GET'])
def get_readings():
    readings = Reading.query.all()
    return jsonify([{'id': r.id, 'position': r.position, 'card_id': r.card_id} for r in readings])

