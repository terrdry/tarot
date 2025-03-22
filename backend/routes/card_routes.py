# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint, jsonify

# Local applicaion imports
from models import Card
from database import add_card, delete_card



logger = logging.getLogger(os.path.basename(__file__))


card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([{ 'id': c.id, 'name': c.name, 'major': c.major, 'img': c.img } for c in cards])


@card_routes.route("/cards/add/<string:card_name>/<string:isMajor>")
def adding_card(card_name, isMajor):
    record_id = add_card( card_name, True)
    return jsonify({"id": record_id,  "name": card_name, "isMajor": isMajor, "image": "TOOD"})

@card_routes.route("/cards/delete/<string:name>")
def deleting_card(name):
    card_deleted = delete_card(name)
    logger.warning("In deleting_card")
    return jsonify(f'Deleted  {card_deleted}')

@card_routes.route('/')
def index():
    return jsonify('Welcome')