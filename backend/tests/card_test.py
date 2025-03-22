# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
from database import add_card, get_count, delete_card, get_all
#from models import Card, get_db, Reading
from models import Card, get_db 

logger = logging.getLogger(os.path.basename(__file__))
CARD_LIST = ["The Magician",
             "The Fool",
             "Ace of Swords",
             "3 of Pentacles",
             "5 of Wands",
             "The Tower",
             "Death",
             "The Hanged Man",
             "Nine of Swords",
             "King of Cups"
             ]


def test_for_card(client):
    """test_for_card
    Ensure that the cards table exists
    Args:
        client (object): pyTest fixture
    """
    table_names = pytest.names
    assert 'card' in table_names


def test_add_card(client):
    """test_add_card
    Add a card to the card table

    Args:
        client (object): pyTest fixture
    """
    response = client.get('/cards/add/The Magician/True')
    assert response.status_code == 200


def test_add_duplicate_card(client):
    """test_add_duplicate_card
    Add a duplicate card and make sure that if forces an exception
    Args:
        client (object): pyTest fixture
    """
    name = 'The Magician'
    isMajor = True

    response = client.get(f'/cards/add/{name}/{isMajor}')
    with pytest.raises(IntegrityError):
        add_card(name, isMajor)


def test_add_multiple_cards(client):
    """test_add_multiple_cards _summary_

    Args:
        client (object): pyTest fixture
    """    
    isMajor = True
    for elem in CARD_LIST:
        response = client.get(f'/cards/add/{elem}/{isMajor}')
    assert get_count(Card) == len(CARD_LIST)


def test_delete_card(client):
    """test_delete_card 

    Args:
        client (object): pyTest fixture
    """ 
    isMajor = True
    for elem in CARD_LIST:
        response = client.get(f'/cards/add/{elem}/{isMajor}')

    assert get_count(Card) == len(CARD_LIST)
    # database setup for deletion of the
    delete_card("The Magician")
    assert get_count(Card) == len(CARD_LIST) - 1
    delete_card("Death")
    assert get_count(Card) == len(CARD_LIST) - 2
    cards = get_all(Card)
    card_names = [card.name for card in get_all(Card)]
    assert "The Magician" not in card_names
    assert "Bonzo" not in card_names
    assert "King of Cups" in card_names
    assert "Death" not in card_names

def test_delete_card_badname(client):
    isMajor = True
    for elem in CARD_LIST:
        response = client.get(f'/cards/add/{elem}')
    response = client.get(f'/cards/delete/{elem}')