from pathlib import Path
import os
import logging
logger = logging.getLogger(os.path.basename(__file__))

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.join(BASE_DIR, "db")
BASE_DIR = "sqlite:///"+ BASE_DIR
class testConfig:
    DB_NAME = "tarot-test.db"
    SQLALCHEMY_DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
class devConfig:
    DB_NAME = "tarot-dev.db"
    SQLALCHEMY_DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
class prodConfig:
    DB_NAME = "tarot.db"
    SQLALCHEMY_DATABASE_URI = os.path.join(BASE_DIR, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False