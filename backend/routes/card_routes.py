# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint
from flask import jsonify
from flask import request

# Local applicaion imports
from models import Card
from database import add_card
from database import delete_card
from database import read_card
from database import update_card


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


@card_routes.route('/cards/add', methods=["POST"])
def adding_card():
    """adding_card Add card

    Add the tarot card

    Args:
        card_name (string): name of card
        isMajor (bool): Major Arcana card flag

    Returns:
        string: result of operation encoded in JSON
    """
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error", str(e)}), 500

    # add the record
    record_id = add_card(data)
    return jsonify({"id": record_id})


@card_routes.route("/cards/delete/<int:id>", methods=["POST"])
def deleting_card(id):
    """deleting_card Delete card

    Delete the Tarot card

    Args:
        name (string): name of card

    Returns:
        string: result of operation encoded in JSON
    """
    card_deleted = delete_card(id)
    logger.warning("In deleting_card")
    return jsonify(f'Deleted  {card_deleted}')


@card_routes.route("/cards/read/<int:id>",  methods=["GET"])
def reading_card(id):
    """reading_card Read card

#     Read the Tarot card

#     Args:
#         id (int): id of card

#     Returns:
#         string: record of id returned encoded in JSON
#     """
    card_read = read_card(id)
    logger.warning("In card_read")
    return jsonify(card_read.json)


@card_routes.route("/cards/update/<int:id>",  methods=["POST"])
def updating_card(id):
    """updating_card Update card

    Update the Tarot card

    Args:
        id (int): id of card

    Returns:
        string: result of operation encoded in JSON
    """
    pass
    try:
        data = request.get_json()
        update_card(id, data)
    except Exception as e:
        return jsonify({"post  error", str(e)}), 500

    return jsonify(data)


@card_routes.route("/",  methods=["GET"])
def index_cards():
    pass
    return jsonify("hello")
