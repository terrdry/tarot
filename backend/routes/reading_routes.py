from flask import Blueprint, jsonify
from models import Reading

reading_routes = Blueprint('reading_routes', __name__)

@reading_routes.route('/readings', methods=['GET'])
def get_readings():
    readings = Reading.query.all()
    return jsonify([{ 'id': r.id, 'date_created': r.date_created, 'date_modified': r.date_modified, 'position': r.position, 'card_id': r.card_id } for r in readings])
