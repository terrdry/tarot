# Standard Library imports
import os
import logging 

# Third-party imports
from sqlalchemy.exc import IntegrityError

# Local applicaion imports
from models import Card, get_db,Reading


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
        db= get_db()
        card=  Card(name=name, 
                    major=major, 
                    img=img)
        db.session.add(card)
        db.session.commit()
        return card.id
    except IntegrityError as e:
        logger.warning('Duplicate card Record')
        raise e

def add_reading(position, card_id):
    """add_reading 

    Returns:
        _type_: _description_
    """
    try:    
        db= get_db()
        reading=  Reading(position=position, 
                          card_id=card_id)
        db.session.add(reading)
        db.session.commit()
    except IntegrityError as e:
        logger.warning('Duplicate reading Record')
        raise e
    return reading.id