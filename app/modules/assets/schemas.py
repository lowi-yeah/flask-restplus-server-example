# encoding: utf-8

"""
Serialization schemas for Team resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from flask_restplus_patched import Schema


class AssetSchema(Schema):
    """
    Schema for assets.
    """
    id = fields.Str(attribute='asset_id')
    metadata = fields.Str(attribute='metadata_digest')
