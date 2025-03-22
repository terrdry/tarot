# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
from database import add_reading, delete_reading, get_count, get_all
from models import Reading

logger = logging.getLogger(os.path.basename(__file__))

READING_LIST = ["The Magician",
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


def test_for_reading(client):
    """test_for_read
    Ensure that the read table exists
    Args:
        client (object): pyTest fixture
    """
    table_names = pytest.names
    assert 'reading' in table_names


def test_add_reading(client):
    """test_add_read
    Add a card to the read table

    Args:
        client (object): pyTest fixture
    """
    read_name = "Reading with you"

    response = client.get(f'/reading/add/{read_name}')
    assert response.status_code == 200


def test_add_duplicate_reading(client):
    read_name = "Reading with Client35"
    response = client.get(f'/reading/add/{read_name}')
    with pytest.raises(IntegrityError):
        add_reading(read_name)


def test_add_multiple_reading(client):
    """test_add_multiple_reading 

    Args:
        client (object): pyTest fixture
    """
    for elem in READING_LIST:
        response = client.get(f'/reading/add/{elem}')
    assert get_count(Reading) == len(READING_LIST)


def test_delete_reading(client):
    """test_delete_reading 

    Args:
        client (object): pyTest fixture
    """
    for elem in READING_LIST:
        response = client.get(f'/reading/add/{elem}')

    assert get_count(Reading) == len(READING_LIST)
    # database setup for deletion of the
    delete_reading("The Magician")
    assert get_count(Reading) == len(READING_LIST) - 1
    delete_reading("Death")
    assert get_count(Reading) == len(READING_LIST) - 2
    readings = get_all(Reading) 
    reading_names = [card.name for card in get_all(Reading)]
    assert "The Magician" not in reading_names
    assert "Bonzo" not in reading_names
    assert "King of Cups" in reading_names
    assert "Death" not in reading_names
