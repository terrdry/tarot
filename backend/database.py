
from models import Card, get_db


def add_card():
    db= get_db()
    card=  Card(name="The Magician", 
                major=True, 
                img="magician.jpg")
    db.session.add(card)
    db.session.commit()
    return card.id