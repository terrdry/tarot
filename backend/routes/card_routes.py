from flask import Blueprint, jsonify
from models import Card

card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([{ 'id': c.id, 'name': c.name, 'major': c.major, 'img': c.img } for c in cards])
