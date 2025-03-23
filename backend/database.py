# Standard Library imports
import os
import logging

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from models import Card
from models import get_db
from models import Reading

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


def edit_card(name, new_name):
    """ edit_card Edit Card

        Edit the card by name of card; since this is a unique
        value we can trust it to work with an existant card. 

        Args:
            name (string): name of the tarot card
            new_name (string): name that the tarot card will be changed to

        Raises:
            e: Integrity Error for cards and card record

        Returns:
            string: the name of the tarot card
    """
    try:
        db = get_db()
        card = db.session.query(Card).filter_by(name=name).first()
        if card:
            card.name = new_name
            db.session.commit()
            return card
        else:
            logger.warning("Record not found")
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


def edit_reading(name, new_name):
    """ edit_read  Edit Card

        Delete the reading by name of a reading; since this is a unique
        value we can trust it to work with an existant reading. 

        Args:
            name (string): name of the reading
            new_name (string): name that the reading will be changed to

        Raises:
            e: Integrity Error for readings and reading record

        Returns:
            string: the name of the tarot reading
    """
    try:
        db = get_db()
        reading = db.session.query(Reading).filter_by(name=name).first()
        if reading:
            reading.name = new_name
            db.session.commit()
            return reading
        else:
            logger.warning("Record not found")
    except IntegrityError as e:
        logger.warning('Duplicate reading Record')
        raise e


def delete_reading(name):
    """delete_reading Delete a reading record by name

    Args:
        name (string): name of reading record

    Raises:
        e: Integrity Error for readings and readings record

    Returns:
        int: the id of the reading 
    """

    db = get_db()
    reading = db.session.query(Reading).filter_by(name=name).first()
    if reading:
        db.session.delete(reading)
        db.session.commit()
        return reading.name
    else:
        logger.warning("Record not found")
# TODO Should be in a seperate file like /db/helpers


def get_count(table_object):
    """get_count Get count of records in a table

    This is a database helper function to get the count of records
    for the table object 

    Args:
        table_object (object): Table reference 

    Returns:
        int: Number of records in table_object
    """
    db = get_db()
    count = db.session.query(table_object).count()
    return count


def get_all(table_object):
    """get_all Get all records in a table

    Call the query.all() on a table and returns 
    a JSON object that contains all the records 
    in the database

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
