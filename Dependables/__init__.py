from flask import Flask
from {PROJECT_NAME}.Configuration.configuration import configure_app, LOGGING_CONFIG

# Logging
from logging.config import dictConfig
dictConfig(LOGGING_CONFIG)

# Initiate App
app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

# Configuration
configure_app(app)


# Caching
from flask_caching import Cache
ncache = Cache(app, config={'CACHE_TYPE': app.config.get('CACHE_TYPE'),
                            'CACHE_REDIS_HOST': app.config.get('CACHE_REDIS_HOST'),
                            'CACHE_REDIS_PORT': app.config.get('CACHE_REDIS_PORT'),
                            'CACHE_REDIS_DB': app.config.get('CACHE_REDIS_DB'),
                            'CACHE_KEY_PREFIX': app.config.get('CACHE_KEY_PREFIX'),
                            'CACHE_DEFAULT_TIMEOUT': app.config.get('CACHE_DEFAULT_TIMEOUT')
                            })

# Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per minute", "2 per second"],
)



# Routes
from {PROJECT_NAME}.Views import home
