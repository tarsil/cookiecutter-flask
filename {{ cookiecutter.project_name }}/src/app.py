import flask_seasurf
from flask import Flask
from flask_marshmallow import Marshmallow


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

    marshmallow = Marshmallow(app)
    marshmallow.init_app(app)

    from .routes import routes
    routes(app)


def create_app():
    """
    Main entry-point of the service.
    Initializes the service and all the dependencies

    1. Creates the scaffold app
    2. Initializes the dependencies and add them to the application context
    """
    app = Flask(__name__)
    configure_app(app)

    return app


app = create_app()
