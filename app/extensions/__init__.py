# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position,wrong-import-order
"""
Extensions setup
================

Extensions provide access to common resources of the application.

Please, put new extension instantiations and initializations here.
"""

from .logging import Logging

logging = Logging()

from flask_cors import CORS
cross_origin_resource_sharing = CORS()

from flask_marshmallow import Marshmallow
marshmallow = Marshmallow()

from . import api

from .blockchain import Blockchain
blockchain = Blockchain()

def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
        logging,
        cross_origin_resource_sharing,
        marshmallow,
        api,
        blockchain):
        extension.init_app(app)
