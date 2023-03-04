import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'SUPER_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLAlchemy_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1/IDGS803"
    SQLAlchemy_TRACK_MODIFICATION = False