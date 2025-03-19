# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint, jsonify

# Local applicaion imports
from models import Card
import database 



logger = logging.getLogger(os.path.basename(__file__))


card_routes = Blueprint('card_routes', __name__)

# @card_routes.route('/cards', methods=['GET'])
# def get_cards():
#     logger.info("Calling")
#     print("Call X")
#     cards = Card.query.all()
#     return jsonify("hello")
#     # return jsonify([{ 'id': c.id, 'name': c.name, 'major': c.major, 'img': c.img } for c in cards])


@card_routes.route("/cards/add/<string:card_name>/<string:isMajor>")
def adding_card(card_name, isMajor):
    record_id = database.add_card( card_name, isMajor)
    return jsonify({ "name": card_name, "isMajor": isMajor, "image": "TOOD"})

@card_routes.route("/cards/delete")
def delete_card(indexNumber):
    # logger.warning("In Add_card")
    # return jsonify('pong!')   
    # add_card()
    # assert response.status_code == 200
    # card = Card(name="The Magician", major=True, img="magician.jpg")
    # with app.app_context():
    #     db.session.add(card)
    #     db.session.commit()
    # response = client.post('/readings', json={"position": 1, "card_id": card.id})
    # assert response.status_code == 201
    return jsonify('still under construction')

@card_routes.route('/')
def index():
    return jsonify('Welcome')