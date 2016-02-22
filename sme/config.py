from os import environ


class Config(object):
    """Default."""
    DEBUG = False
    TESTING = False
    CSRF_ENAGLED = True
    SECRET_KEY = environ['SME_DEV_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = environ['SME_DEV_SQLALCHEMY_DATABASE_URI']


class ProductionConfig(Config):
    """Production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ['SME_PROD_SQLALCHEMY_DATABASE_URI']
    SECRET_KEY = environ['SME_PROD_SECRET_KEY']


class StagingConfig(Config):
    """Staging."""
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Development."""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing."""
    TESTING = True
