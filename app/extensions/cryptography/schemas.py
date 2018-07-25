# encoding: utf-8

"""
Serialization schemas for Team resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields as fields

from app.extensions.cryptography.validate import Ed25519Key as KeyValidator
from flask_restplus_patched import Schema


class Ed25519KeySchema(Schema):
    """
    Schema for a base58-encoded Ed25519 public key.
    """
    key = fields.Str(validate=KeyValidator())

    # @validates('id')
    # def validate_id(self, id):
    #     """
    #     Validate the format of the asset id. must be a public key
    #     :param asset_id: the id to be validated
    #     :raises: ValidationError
    #     """
    #     raise ValidationError('wat')
