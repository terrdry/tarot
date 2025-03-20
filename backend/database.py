# Standard Library imports
import os
import logging

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from models import Card, get_db, Reading


logger = logging.getLogger(os.path.basename(__file__))


def add_card(name, major, img="TODO"):
    """add_card 

    Args:
        name (string): Name of tarot card
        major (bool): Major arcana card
        img (byte): Tarot card image

    Returns:
        int : returns the id of the card record if successful
    """
    try:
        db = get_db()

        card = Card(name=name,
                    major=major,
                    img=img)
        db.session.add(card)
        db.session.commit()
        return card.id
    except IntegrityError as e:
        logger.warning('Duplicate card Record')
        raise e


def delete_card(name):
    try:
        db = get_db()
        card = db.session.query(Card).filter_by(name=name).first()
        if card:
            db.session.delete(card)
            db.session.commit()
        else:
            logger.warning("Record not found")
    except IntegrityError as e:
        logger.warning('Duplicate card Record')
        raise e


def add_reading(position, card_id):
    """add_reading 

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
    try:
        db = get_db()
        count = db.session.query(table_object).count()
    except IntegrityError as e:
        logger.warning("get_count returned error")
        raise e
    return count


def get_all(table_object):
    try:
        db = get_db()
        card_list = db.session.query(table_object).all()
    except IntegrityError as e:
        logger.warning('not able to do all query')
        raise e
    return card_list
