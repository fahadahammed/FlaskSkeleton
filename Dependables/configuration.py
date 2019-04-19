import os

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
            'class': 'logging.FileHandler',
            'filename': 'Logs/logs.log',
            'formatter': 'default'
        }
    },
    'root': {
        'handlers': ['wsgi', 'logfile']
    }
}


class BaseConfig(object):
    PROTECTED_PATH = "ProtectedPath"
    THREADED = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = 'dev'
    HOST = "{HOST}"
    PORT = {PORT}
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = "{PROJECT_NAME-RANDOM}"

    ACCOUNT_ENDPOINT = "http://127.0.0.1:55501/"

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = '11'
    CACHE_KEY_PREFIX = '{CACHE_KEY_PREFIX}'
    CACHE_DEFAULT_TIMEOUT = 43200

    {PROJECT_NAME_FOR_DB}_DB_PORT = 3306
    {PROJECT_NAME_FOR_DB}_DB_HOST = "127.0.0.1"
    {PROJECT_NAME_FOR_DB}_DB_USER = "{PROJECT_NAME}"
    {PROJECT_NAME_FOR_DB}_DB_PASSWORD = "{PROJECT_NAME}"
    {PROJECT_NAME_FOR_DB}_DB_NAME = "{PROJECT_NAME}"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = 'prod'
    HOST = "{HOST}"
    PORT = {PORT}
    TEMPLATES_AUTO_RELOAD = False
    SECRET_KEY = "{PROJECT_NAME-RANDOM}"
    ACCOUNT_ENDPOINT = "http://127.0.0.1:55501/"

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = '11'
    CACHE_KEY_PREFIX = '{CACHE_KEY_PREFIX}'
    CACHE_DEFAULT_TIMEOUT = 43200

    {PROJECT_NAME_FOR_DB}_DB_PORT = 3306
    {PROJECT_NAME_FOR_DB}_DB_HOST = "127.0.0.1"
    {PROJECT_NAME_FOR_DB}_DB_USER = "{PROJECT_NAME}"
    {PROJECT_NAME_FOR_DB}_DB_PASSWORD = "{PROJECT_NAME}"
    {PROJECT_NAME_FOR_DB}_DB_NAME = "{PROJECT_NAME}"


config = {
    "dev": "{PROJECT_NAME}.Configuration.configuration.DevelopmentConfig",
    "prod": "{PROJECT_NAME}.Configuration.configuration.ProductionConfig",
    "default": "{PROJECT_NAME}.Configuration.configuration.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('APPLICATION_ENV', 'default')
    app.config.from_object(config[config_name])
