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


def add_reading(position, card_id):
    """add_reading 
    Add a reading record into the database

    Args:
        position (_type_): _description_
        card_id (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        db = get_db()
        reading = Reading(position=position,
                          card_id=card_id)
        db.session.add(reading)
        db.session.commit()
    except IntegrityError as e:
        logger.warning('Duplicate reading Record')
        raise e
    return reading.id


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
