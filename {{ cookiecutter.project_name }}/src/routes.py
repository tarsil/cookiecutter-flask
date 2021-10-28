from flask_restx import Api
from flask import current_app
from src.api.v1 import routes as v1


def routes(app):
    """
    Generate all the views and blueprints and corresponding endpoints.

    Args:
        app: Flask current app
    """
    api = Api(version="1.0")

    with app.app_context():
        add_specs = current_app.config.get('SWAGGER_SPECS', False)
        api.init_app(app, title="Service API", description="All the APIs of {{ cookiecutter.project_name }}", add_specs=add_specs)

    # APPLYING THE ROUTES
    v1.routes(api)
