"""
All the custom settings are placed here. The settings are therefore loaded
trough environment variable `FLASK_APP_SETTINGS` that should be just a location
of the file
"""
import os
import datetime
import binascii

# GENERAL SETTINGS

DEBUG = False
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
SECRET_KEY = os.getenv('SECRET_KEY', binascii.hexlify(os.urandom(24)))

if FLASK_ENV in ('dev', 'development'):
    DEBUG = True
    AUTO_RELOADER = True

# DATABASE CONFIGURATION

DATABASE_USER = os.environ.get('POSTGRES_USER', 'postgres')
DATABASE_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
DATABASE_NAME = os.environ.get('POSTGRES_DB', '{{ cookiecutter.project_name }}')
DATABASE_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME
)

# CACHES

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)


# These control flask-seasurf.
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_TIMEOUT = datetime.timedelta(days=1)

# SWAGGER
SWAGGER_SPECS = False
