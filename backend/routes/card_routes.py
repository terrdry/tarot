# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint
from flask import jsonify

# Local applicaion imports
from models import Card
from database import add_card
from database import delete_card
from database import edit_card


logger = logging.getLogger(os.path.basename(__file__))
card_routes = Blueprint('card_routes', __name__)


@card_routes.route('/cards', methods=['GET'])
def get_cards():
    """get_cards Get all cards in a table

    Returns:
        string: result of operation encoded in JSON 
    """
    cards = Card.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'major': c.major, 'img': c.img} for c in cards])


@card_routes.route("/cards/add/<string:card_name>/<string:isMajor>")
def adding_card(card_name, isMajor):
    """adding_card Add card 

    Add the tarot card

    Args:
        card_name (string): name of card
        isMajor (bool): Major Arcana card flag

    Returns:
        string: result of operation encoded in JSON 
    """
    record_id = add_card(card_name, True)
    return jsonify({"id": record_id,  "name": card_name, "isMajor": isMajor, "image": "TOOD"})


@card_routes.route("/cards/delete/<string:name>")
def deleting_card(name):
    """deleting_card Delete card

    Delete the Tarot card

    Args:
        name (string): name of card

    Returns:
        string: result of operation encoded in JSON 
    """
    card_deleted = delete_card(name)
    logger.warning("In deleting_card")
    return jsonify(f'Deleted  {card_deleted}')


@card_routes.route("/cards/edit/<string:name>/<string:other_name>")
def editing_card(name, other_name):
    """editing_card Edit card

    Edit the Tarot card

    Args:
        name (string): name of card

    Returns:
        string: result of operation encoded in JSON 
    """
    card_edit = edit_card(name, other_name)
    logger.warning("In edit_card")
    return jsonify(f'Editing  {card_edit}')


@card_routes.route('/')
def index():
    """index HTML Index

    Temporary here until we work on the main page

    Returns:
        string: JSON welcome string 
    """
    return jsonify('Welcome')
