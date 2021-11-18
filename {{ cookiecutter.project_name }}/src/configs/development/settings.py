from src.configs.settings import *

DEBUG = True
ENV = 'development'
FLASK_ENV = ENV

SWAGGER_SPECS = True
COVALENTHQ_API = []

try:
    from src.configs.development.local_settings import *
except ImportError:
    pass

CORS_ORIGINS = ['http://localhost:4200', 'http://localhost:8000']
