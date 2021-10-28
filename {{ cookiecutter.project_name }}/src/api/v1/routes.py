from flask_restx import Api
from .views import HelloWorldApiView


def routes(api: Api):
    """
    Generate all the views and blueprints and corresponding endpoints.

    Args:
        app: Flask current app
    """
    namespace = api.namespace("api/v1/{{ cookiecutter.project_name }}")

    # APPLYING THE ROUTES
    namespace.add_resource(HelloWorldApiView, '/hello', endpoint='hello-world')
