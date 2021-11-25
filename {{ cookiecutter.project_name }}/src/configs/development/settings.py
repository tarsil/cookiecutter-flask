from src.configs.settings import *

DEBUG = True
FLASK_ENV = 'development'
AUTO_RELOADER = True

SWAGGER_SPECS = True
COVALENTHQ_API = []

# LOGGING
LOG_BACKTRACE = True
LOG_LEVEL = 'DEBUG'

try:
    from src.configs.development.local_settings import *
except ImportError:
    pass

CORS_ORIGINS = ['http://localhost:4200', 'http://localhost:8000']
