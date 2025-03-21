# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint, jsonify

# Local applicaion imports
from models import Reading


logger = logging.getLogger(os.path.basename(__file__))

reading_routes = Blueprint('reading_routes', __name__)
logger.info("Reading routes")


@reading_routes.route('/readings', methods=['GET'])
def get_readings():
    logger.info("hello from reading_routes")
    # readings = Reading.query.all()
    return jsonify("hello")

# @reading_routes.route('/readings/add/{0}/{1}', methods=['GET'])
# def get_readings():
#     logger.info("hello from reading_routes")
