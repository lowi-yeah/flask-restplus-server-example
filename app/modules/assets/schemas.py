# encoding: utf-8

"""
Serialization schemas for Team resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from marshmallow import validates_schema, validates, ValidationError
from flask_restplus_patched import Schema
from .models import Asset
from app.extensions.cryptography.fields import PublicKey


class AssetSchema(Schema):
    """
    Schema for assets.
    """
    __envelope__ = {'single': 'asset', 'many': 'assets'}
    __model__ = Asset

    id = PublicKey()
    metadata = fields.Str()

    # @validates_schema
    # def validate_asset(self, data):
    #     """
    #     Validate the format of the asset.
    #     The 'id' must be a public key. The 'metadata' must be a sha3/256 digest
    #     :param data:
    #     """
    #     print('validate asset', data)
    #     raise ValidationError('field_a must be greater than field_b')
    #
    # @validates('id')
    # def validate_id(self, data):
    #     """
    #     Validate the format of the asset.
    #     The 'id' must be a public key. The 'metadata' must be a sha3/256 digest
    #     :param data:
    #     """
    #     print('validate id', data)
    #     raise ValidationError('field_a must be greater than field_b')
