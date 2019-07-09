import os

# Base Config
class BaseConfig(object):
    DEBUG = False
    # Try replacig secret_key with os.urandom(24)
    secret_key = "blah"
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False
