# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
from database import add_card, get_count, delete_card, get_all
from models import Card, get_db, Reading

logger = logging.getLogger(os.path.basename(__file__))


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
    rec_no = add_card("TheMagician", True)
    assert rec_no


def test_add_duplicate_card(client):
    """test_add_duplicate_card
    Add a duplicate card and make sure that if forces an exception
    Args:
        client (_type_): _description_
    """

    response = client.get('/cards/add/{0}/{1}')
    add_card("The Magician", True)
    with pytest.raises(IntegrityError):
        add_card("The Magician", True)


def test_add_multiple_cards(client):
    test_list_cards = ["The Magician",
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
    response = client.get('/cards/add/{0}/{1}')    
    for elem in test_list_cards:
        add_card(elem, True )
    assert get_count(Card) == len(test_list_cards)

def test_delete_card(client):
    test_list_cards = ["The Magician",
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
    response = client.get('/cards/add/{0}/{1}')    
    for elem in test_list_cards:
        add_card(elem, True )

    # database setup for deletion of the 
    delete_card("The Magician")
    assert get_count(Card) == len(test_list_cards) -1 
    delete_card("Death")
    assert get_count(Card) == len(test_list_cards) -2
    cards = get_all(Card)
    card_names = [ card.name for card in get_all(Card)]
    assert "The Magician" not in card_names
    assert "Bonzo" not in card_names
    assert "King of Cups" in card_names
    assert "Death" not in card_names
    
    # for elem in card_names:
    #     logger.warning("The card's name is %s" % (elem))



    