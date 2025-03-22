# Standard Library imports
import os
import logging

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from models import Card, get_db, Reading


logger = logging.getLogger(os.path.basename(__file__))


def add_card(name, major, img="TODO"):
    """add_card Add Card
    Add the card record to the database name 

    name is a unique key and Integretiy error will be triggered 
    when there is a duplicate.

    Args:
        name (string): name of the tarot card
        major (bool): Major arcana card
        img (str, optional): Tarot card image. Defaults to "TODO".

    Raises:
        e: Integrity Error for cards and card record

    Returns:
        string: the name of the tarot card
    """
    try:
        db = get_db()

        card = Card(name=name,
                    major=major,
                    img=img)
        db.session.add(card)
        db.session.commit()
        return card.name
    except IntegrityError as e:
        logger.warning('Duplicate card Record')
        raise e


def delete_card(name):
    """delete_card Delete Card
    Delete the card by name of card; since this is a unique
    value we can trust it to work with an existant card. 

    Args:
        name (string): name of the tarot card

    Raises:
        e: Integrity Error for cards and card record

    Returns:
        string: the name of the tarot card
    """
    try:
        db = get_db()
        card = db.session.query(Card).filter_by(name=name).first()
        if card:
            db.session.delete(card)
            db.session.commit()
            return card.name
        else:
            logger.warning("Record not found")
    except IntegrityError as e:
        logger.warning('Duplicate card Record')
        raise e


def add_reading(name):
    """add_reading 
    Add a reading record into the database

    Args:
        name (string): Reading name

    Raises:
        e: Integrity Error for reads and read record

    Returns:
        string: the name of the tarot reading
    """
    try:
        db = get_db()
        reading = Reading(name=name)
        db.session.add(reading)
        db.session.commit()
    except IntegrityError as e:
        logger.warning('Duplicate reading Record')
        raise e
    return reading.id


def delete_reading(name):
    """delete_card Delete reading
    Delete the reading by name of the reading; since this is a unique
    value we can trust it to work with an existant card. 

    Args:
        name (string): name of the reading event

    Raises:
        e: Integrity Error for reading and reading record

    Returns:
        string: the id of the reading 
    """
    try:
        db = get_db()
        reading = db.session.query(Reading).filter_by(name=name).first()
        if Reading:
            db.session.delete(reading)
            db.session.commit()
            return reading.name
        else:
            logger.warning("Record not found")
    except IntegrityError as e:
        logger.warning('Duplicate reading Record')
        raise e
# Should be in a seperate file like /db/helpers


def get_count(table_object):
    """get_count 
    This is a database helper function to get the count of records
    for the table object 

    Args:
        table_object (object): Table reference 

    Raises:
        e: Error for any integrity errors.

    Returns:
        int: Number of records in table_object
    """
    try:
        db = get_db()
        count = db.session.query(table_object).count()
    except IntegrityError as e:
        logger.warning("get_count returned error")
        raise e
    return count


def get_all(table_object):
    """get_all Get all records in table

    Args:
        table_object (object): Table reference

    Raises:
        e: Error for any integrity errors.

    Returns:
        list: dictionary for all cards in card table 
    """

    try:
        db = get_db()
        card_list = db.session.query(table_object).all()
    except IntegrityError as e:
        logger.warning('not able to do all query')
        raise e
    return card_list
