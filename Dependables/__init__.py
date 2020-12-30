import os
import json
from flask import Flask
from PROJECTNAMEFSKLTN.Configuration.configuration import configure_app, LOGGING_CONFIG

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
# Example
# @ncache.cached(timeout=60, key_prefix=str(section))

# Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["30000 per minute", "5000 per second"],
)


# Extras
os.makedirs(str(os.path.abspath(path="./"))+"/"+app.config["PROTECTED_PATH"], exist_ok=True)


# Routes
from PROJECTNAMEFSKLTN.Views import _v_Home
