import sys

import flask_seasurf
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from loguru import logger

from .utils.handlers import InterceptHandler
from .utils.helpers import get_app, set_app


def configure_app(app: Flask) -> None:
    """
    The configuration is read from the filename in the "FLASK_SETTINGS_FILENAME"
    environment variable (if it exists) and some other important settings

    Additional settings such as SECRET_KEY and other settings should be added
    accordingly.

    :param Flask app: The Flask app that requires configuring.
    :return: None
    """
    app.config.from_envvar("FLASK_SETTINGS_FILENAME", silent=True)
    app.csrf = flask_seasurf.SeaSurf(app)

    # CORS
    CORS(app)

    # MARSHMALLOW
    marshmallow = Marshmallow(app)
    marshmallow.init_app(app)

    # LOGGER
    # LOGGER
    logger.add(sys.stdout, level=app.config['LOG_LEVEL'], format="{time} {level} {message}", colorize=True,
                 backtrace=app.config['LOG_BACKTRACE'])
    app.logger.addHandler(InterceptHandler())


    from .routes import routes
    routes(app)


def create_app():
    """
    Main entry-point of the service.
    Initializes the service and all the dependencies

    1. Creates the scaffold app
    2. Initializes the dependencies and add them to the application context
    3. Checks if there is more than one thread
    """
    app = Flask(__name__)

    try:
        app = get_app(app.__class__.__name__)
    except ValueError:
        configure_app(app)
        set_app(app)
    return app


app = create_app()
