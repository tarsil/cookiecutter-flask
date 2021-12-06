from flask_restx import Api
from ...apps.{{ cookiecutter.app_name }}.v1.routes import routes as {{ cookiecutter.app_name }}_v1


def routes(api: Api):
    """
    Generate all the views and blueprints and corresponding endpoints.

    Args:
        app: Flask current app
    """
    {{ cookiecutter.app_name }}_v1(api)
