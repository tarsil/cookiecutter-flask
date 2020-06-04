import os
import binascii
import unittest
from src.app import create_app


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))

    def test_call_main_endpoint(self):
        """API endpoint test is 200"""
        client = self.client.get('/')

        self.assertEqual(client.status_code, 200)

    def test_call_api_test(self):
        """API endpoint test is 200"""
        client = self.client.get('/{{ cookiecutter.project_name }}/api/v1/hello/')

        self.assertEqual(client.status_code, 200)


if __name__ == '__main__':
    unittest.main()
