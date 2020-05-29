"""
ALl the views of {{ cookiecutter.project_name }}
"""
from flask import make_response
from flask_api import status
from flask_restplus import Resource


class HelloWorldApiView(Resource):
    """
    Auto generated api
    """
    def get(self):
        return make_response("Welcome to {}".format("{{ cookiecutter.project_name }}"), status.HTTP_200_OK)
