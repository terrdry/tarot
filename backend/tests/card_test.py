# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError
from flask import jsonify

# Local applicaion imports
from .app_test import client
from database import add_card
from database import get_count
from database import read_card
from database import delete_card
from database import get_all

from models import Card
from models import get_db

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
    """test_for_card check for the existance of the table

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

    payload = {"name": "The Runt", "major": True, "img": "TODO.JPG"}

    answer = map(lambda x: x.to_dict(), payload)
    response = client.post('/cards/add', json=payload)
    assert response.status_code == 200


def test_add_duplicate_card(client):
    """test_add_duplicate_card Test Duplicate cards

    Add a duplicate card and make sure that if forces an exception

    Args:
        client (object): pyTest fixture
    """

    payload = {"name": "The Runt", "major": True, "img": "TODO.JPG"}
    response = client.post('/cards/add', json=payload)
    with pytest.raises(IntegrityError):
        add_card(payload)


def test_add_multiple_cards(client):
    """test_add_multiple_cards Add multiple records

    Add 10 records and check to see if you have 10 records in
    the card table

    Args:
        client (object): pyTest fixture
    """
    for elem in CARD_LIST:
        payload = {"name": elem, "major": True, "img": "TODO.JPG"}
        response = client.post('/cards/add', json=payload)
    assert get_count(Card) == len(CARD_LIST)


def test_read_card(client):
    """test_read_card Read the Card

    Read from a list;
    - add 10 records
    - use ge



    Args:
        client (string): Name of the tarot card
    """
    for elem in CARD_LIST:
        payload = {"name": elem, "major": True, "img": "TODO.JPG"}
        response = client.post('/cards/add', json=payload)

    response = client.get('/cards/read/1')
    assert "Magician" in response.json["name"]
    response = client.get('/cards/read/3')
    assert "Swords" in response.json["name"]


def test_update_card(client):
    """test_edit_update_card Edit and update the Card

    Change the name from one name to another

    Args:
        client (string): Name of the tarot card
    """
    for elem in CARD_LIST:
        payload = {"name": elem, "major": True, "img": "TODO.JPG"}
        response = client.post('/cards/add', json=payload)

    payload = {"name": "nosferatu", "major": True, "img": "TODO.JPG"}
    response = client.post('/cards/update/1', json=payload)
    assert "nosferatu" in response.json["name"]


def test_delete_card(client):
    """test_delete_card Delete card

    Delete an existant record

    Args:
        client (object): pyTest fixture
    """
    major = True
    for elem in CARD_LIST:
        payload = {"name": elem, "major": True, "img": "TODO.JPG"}
        response = client.post('/cards/add', json=payload)

    assert get_count(Card) == len(CARD_LIST)
    response = client.post('/cards/delete/1')  # The Magician
    assert get_count(Card) == len(CARD_LIST) - 1
    response = client.post('/cards/delete/3')  # Ace of Swords
    assert get_count(Card) == len(CARD_LIST) - 2
    cards = get_all(Card)
    card_names = [card.name for card in get_all(Card)]
    assert "The Magician" not in card_names
    assert "Ace of Swords" not in card_names
    assert "Bonzo" not in card_names
    assert "King of Cups" in card_names
    assert "Death" in card_names
