# Standard Library imports
import os
import logging

# Third-party imports
from flask import Blueprint
from flask import jsonify

# Local applicaion imports
from models import Reading
from database import add_reading
from database import delete_reading

logger = logging.getLogger(os.path.basename(__file__))

reading_routes = Blueprint('reading_routes', __name__)
logger.info("Reading routes")


@reading_routes.route('/reading', methods=['GET'])
def get_readings():
    """get_readings Get all the reading records

    Get all the contents of the reading table
    Returns:
        string : name of reading
    """
    reading = Reading.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in reading])


@reading_routes.route('/reading/add/<string:read_name>', methods=['GET'])
def adding_reading(read_name):
    """adding_reading Add reading 

    Add a reading record
    Args:
        read_name (string): Name of reading

    Returns:
        string: result of operation encoded in JSON 
    """
    record_id = add_reading(read_name)
    return jsonify([{'id': record_id, 'read_name': read_name}])


@reading_routes.route("/reading/delete/<string:name>")
def deleting_reading(name):
    """deleting_reading Delete reading record

    Args:
        name (string): Name of reading

    Returns:
        string: result of operation encoded in JSON
    """
    reading_deleted = delete_reading(name)
    logger.warning("In deleting_reading")
    return jsonify(f'Deleted  {reading_deleted}')
