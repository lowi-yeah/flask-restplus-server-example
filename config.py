# pylint: disable=too-few-public-methods,invalid-name,missing-docstring
import os


class BaseConfig(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    ERROR_404_HELP = False

    REVERSE_PROXY_SETUP = os.getenv('EXAMPLE_API_REVERSE_PROXY_SETUP', False)

    AUTHORIZATIONS = {
        'oauth2_password': {
            'type':     'oauth2',
            'flow':     'password',
            'scopes':   {},
            'tokenUrl': '/auth/oauth2/token',
        },
        # TODO: implement other grant types for third-party apps
        # 'oauth2_implicit': {
        #    'type': 'oauth2',
        #    'flow': 'implicit',
        #    'scopes': {},
        #    'authorizationUrl': '/auth/oauth2/authorize',
        # },
    }

    ENABLED_MODULES = (
        'assets',
        'api',
    )

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OAUTH_CLIENT_ID = 'documentation'
    SWAGGER_UI_OAUTH_REALM = "Authentication for Flask-RESTplus Example server documentation"
    SWAGGER_UI_OAUTH_APP_NAME = "Flask-RESTplus Example server documentation"

    # TODO: consider if these are relevant for this project
    CSRF_ENABLED = True

    BIGCHAINDB__URL = 'localhost:9984'
    # BIGCHAINDB__URL = 'http://ec2-18-195-153-114.eu-central-1.compute.amazonaws.com:9984'
    PREDEFINED_KEYS_FILE = os.path.join(PROJECT_ROOT, 'keys/rddl_keys.json')

    PUBLIC_KEY_LENGTH = 44
    SHA3_256_DIGEST_LENGTH = 64


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('EXAMPLE_API_SERVER_SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
