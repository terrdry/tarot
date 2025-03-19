# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
from database import add_reading

logger = logging.getLogger(os.path.basename(__file__))


def test_for_reading(client):
    """test_for_read
    Ensure that the read table exists
    Args:
        client (object): pyTest fixture
    """
    table_names = pytest.names
    assert 'reading' in table_names


# def test_add_read(client):
#     """test_add_read
#     Add a card to the read table

#     Args:
#         client (object): pyTest fixture
#     """
#     response = client.get('/reading/add/{0}/{1}')
#     rec_no = add_reading(1, 2)
#     assert rec_no


# def test_add_duplicate_card(client):
#     response = client.get('/cards')
#     add_reading(1, 2)
#     with pytest.raises(IntegrityError):
#         add_reading(1, 2)
