# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
from database import add_card

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
    response = client.get('/cards/add/{0}/{1}')
    rec_no = add_card("TheMagician", True)
    assert rec_no


def test_add_duplicate_card(client):
    """test_add_duplicate_card
    Add a duplicate card and make sure that if forces an exception
    Args:
        client (_type_): _description_
    """

    response = client.get('/cards/add/{0}/{1}'.format("TheMagician", "true"), )
    add_card("The Magician", True)
    with pytest.raises(IntegrityError):
        add_card("The Magician", True)
