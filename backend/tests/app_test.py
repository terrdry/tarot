# Standard Library imports
import os
import logging

# Third-party imports
import pytest
from flask import jsonify
from pathlib import Path
from sqlalchemy import inspect

# Local applicaion imports
from models import get_db
from database import add_card
from config import config
from routes.card_routes import card_routes
from routes.reading_routes import reading_routes
from logging_config import setup_logging


logger = logging.getLogger(os.path.basename(__file__))
FILE_NAME = "db/tarot-test.db"


@pytest.fixture
def client():
    """client  
    Pytest fixture for testing the client code 
    Responsible for setting up database and adding information 
    to the pytest Global/share area

    Yields:
        none : 
    """
    from app import create_app

    setup_logging(filename="tarot-test.log")
    app = create_app("test-tarot", config.testConfig)
    app.register_blueprint(card_routes)
    app.register_blueprint(reading_routes)
    db = get_db()

    app.config.from_object(config.testConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            pytest.names = get_table_names(app)
            logger.warning("From tester--")
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()


def get_table_names(app):
    """get_table_names 
    Helper function for getting the names of the tables 
    that the database contains. Used for subsequent tests

    Args:
        app (object): 
        Flask application module

    Returns:
        list : list of tables defined in the database
    """
    with app.app_context():
        inspector = inspect(get_db().engine)
        table_names = inspector.get_table_names()
    return table_names


def test_database(client):
    """test_database 
    Ensure that the database exists
    Args:
        client (object): pyTest fixture
    """
    tester = Path(os.path.join(os.getcwd(), FILE_NAME)).is_file()
    assert tester


def test_index(client):
    """test_index 
    check and see if the index is accessible
    Args:
        client (object): pyTest fixture
    """
    """Ensure database is blank"""
    # client.get
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_for_reading(client):
    """test_for_reading _summary_
    Ensure that the reading table exists

    Args:
        client (object): pyTest fixture
    """
    table_names = pytest.names
    assert 'reading' in table_names


# def test_get_readings(client):
#     """test_get_readings 
#     Make sure that route is defined

#     Args:
#         client (object): pyTest fixture
#     """
#     response = client.get('/readings')
#     assert response.status_code == 200
#     assert response.json == []

