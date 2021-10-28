from src.configs.settings import *

DEBUG = True
TESTING = True
ENV = 'development'
FLASK_ENV = ENV

SWAGGER_SPECS = True
COVALENTHQ_API = []

try:
    from src.configs.development.local_settings import *
except ImportError:
    pass
