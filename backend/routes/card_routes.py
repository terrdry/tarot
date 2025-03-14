from flask import Blueprint, jsonify
from models import Card

card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([{ 'id': c.id, 'name': c.name, 'major': c.major, 'img': c.img } for c in cards])

@card_routes.route("/ping", methods=['GET'])
def ping_pong():
    return jsonify('pong!')   

@card_routes.route("/cards")
def add_card():
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
    return jsonify('Hello World')