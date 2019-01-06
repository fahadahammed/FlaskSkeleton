from flask import Flask
from {PROJECT_NAME}.Configuration.configuration import configure_app


# Initiate App
app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

# Configuration
configure_app(app)

# Routes
from {PROJECT_NAME}.Views import home
