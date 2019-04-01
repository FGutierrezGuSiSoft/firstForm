import os


class BaseConfig:
    """ Base configuration """
    TESTING = False
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
