from flask_restx import Api
from .views import HelloWorldApiView


def routes(app):
    """
    Generate all the views and blueprints and corresponding endpoints.

    Args:
        app: Flask current app
    """
    api = Api(app=app, version="1.0", title="Service API",
              description="All the APIs of {{ cookiecutter.project_name }}")

    namespace = api.namespace("{{ cookiecutter.project_name }}")

    # APPLYING THE ROUTES
    namespace.add_resource(HelloWorldApiView, '/api/v1/hello/', endpoint='hello-world')
