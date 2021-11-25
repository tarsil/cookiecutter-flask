import os
import binascii
import unittest
from src.app import create_app
from flask_testing import TestCase


class TestAPI(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))

    def test_call_api_test(self):
        """API endpoint test is 200 for the hello endpoint"""
        client = self.client.get('/api/v1/{{ cookiecutter.project_name }}/hello')

        self.assertEqual(client.status_code, 200)
