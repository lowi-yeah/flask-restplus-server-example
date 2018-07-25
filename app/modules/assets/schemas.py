# encoding: utf-8

"""
Serialization schemas for Team resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from marshmallow import validates_schema, validates, ValidationError
from flask_restplus_patched import Schema
from .models import Asset
from app.extensions.cryptography.validate import Ed25519Key as KeyValidator
from app.extensions.cryptography.validate import SHA3256 as HashValidator


class AssetSchema(Schema):
    """
    Schema for assets.
    """
    __envelope__ = {'single': 'asset', 'many': 'assets'}
    __model__ = Asset

    id = fields.Str(validate=KeyValidator())
    metadata = fields.Str(validate=HashValidator())

    @validates('id')
    def validate_id(self, id):
        """
        Validate the format of the asset id. must be a public key
        :param asset_id: the id to be validated
        :raises: ValidationError
        """
        raise ValidationError('wat')
