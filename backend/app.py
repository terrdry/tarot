from flask import Flask, jsonify
from extensions import db
from models import Card, Reading
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.devConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(card_routes)
    app.register_blueprint(reading_routes)

    return app

app = create_app()
client = app.test_client()

# Sanity check route
@app.route('/')
def index():
    return jsonify('Hello World')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')   
    

@app.route("/spoon")
def test_db():
    card = Card(name="The Magician", major=True, img="magician.jpg")
    with app.app_context():
        db.session.add(card)
        db.session.commit()
    # response = client.post('/readings', json={"position": 1, "card_id": card.id})
    # assert response.status_code == 201
    return jsonify('still under construction')