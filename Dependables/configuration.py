import os

if not os.path.exists('Logs'):
    os.makedirs('Logs')


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s at %(threadName)s in %(module)s : %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'logfile': {
            # 'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'Logs/logs.log',
            'formatter': 'default',
            'maxBytes': 1000000,
            'backupCount': 10
        }
    },
    'root': {
        'handlers': ['wsgi', 'logfile']
    }
}


class BaseConfig(object):
    PROJECT_NAME = "PROJECTNAMEFSKLTN"


    PROTECTED_PATH = "ProtectedPath"
    THREADED = True

    ENV = 'dev'
    HOST = "_FSKLTN_HOST"
    PORT = _FSKLTN_PORT

    CACHE_TYPE = 'simple'

    # Database
    kPROJECTNAMEFSKLTN_DB_PORT = 27017
    kPROJECTNAMEFSKLTN_DB_HOST = "127.0.0.1"
    kPROJECTNAMEFSKLTN_DB_USER = "PROJECTNAMEFSKLTN"
    kPROJECTNAMEFSKLTN_DB_PASSWORD = "PROJECTNAMEFSKLTN"
    kPROJECTNAMEFSKLTN_DB_NAME = "PROJECTNAMEFSKLTN"

    SECRET_KEY = "Yc30VUEQfSXtrbLazgFRDvvZb5dbEStjwyo8q12R"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True

    ENV = 'prod'

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = '11'
    CACHE_KEY_PREFIX = '@PROJECTNAMEFSKLTN'
    CACHE_DEFAULT_TIMEOUT = 43200


config = {
    "dev": "PROJECTNAMEFSKLTN.Configuration.configuration.DevelopmentConfig",
    "prod": "PROJECTNAMEFSKLTN.Configuration.configuration.ProductionConfig",
    "default": "PROJECTNAMEFSKLTN.Configuration.configuration.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('ENV', 'default')
    app.config.from_object(config[config_name])
