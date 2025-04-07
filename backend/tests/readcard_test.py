# Standard Library imports
import os
import logging
import pytest

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from .app_test import client
# from database import add_card

logger = logging.getLogger(os.path.basename(__file__))


def test_for_readcard(client):
    """test_for_readcard
    Ensure that the readcard table exists
    Args:
        client (object): pyTest fixture
    """
    table_names = pytest.names
    assert 'readcard' in table_names
