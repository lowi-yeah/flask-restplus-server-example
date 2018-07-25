# encoding: utf-8
"""
Input arguments (Parameters) for Asset resources RESTful API
------------------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from flask_restplus_patched import Parameters, PatchJSONParameters
from marshmallow import validates

from app.extensions.cryptography.validate import validate_public_key, validate_hash_digest


class CreateAssetParameters(Parameters):
    asset_id = fields.String(description="A public key representing the asset")
    metadata_digest = fields.String(description="sha3/256 digest of the metadata")

    @validates('asset_id')
    def validate_id(self, asset_id):
        """
        Validate the format of the asset id. must be a public key
        :param asset_id: the id to be validated
        :raises: ValidationError
        """
        validate_public_key(asset_id)

    @validates('metadata_digest')
    def validate_metadata(self, metadata):
        """
        Validate the format of the asset id.
        :param metadata: the sha3/256 digest to be validated
        :raises: ValidationError
        """
        validate_hash_digest(metadata)


class GetAssetParameters(Parameters):
    asset_id = fields.String(description="A public key representing the asset")

    @validates('asset_id')
    def validate_id(self, asset_id):
        """
        Validate the format of the asset id. must be a public key
        :param str asset_id: the id to be validated
        :raises: ValidationError
        """
        validate_public_key(asset_id)


class PatchAssetMetadataParameters(PatchJSONParameters):
    @classmethod
    def add(cls, obj, field, value, state):
        pass

    @classmethod
    def remove(cls, obj, field, state):
        pass

    @classmethod
    def move(cls, obj, field, value, state):
        pass

    @classmethod
    def copy(cls, obj, field, value, state):
        pass

    # pylint: disable=abstract-method,missing-docstring
    OPERATION_CHOICES = (
        PatchJSONParameters.OP_REPLACE,
    )

    PATH_CHOICES = tuple(
        # '/%s' % field for field in (
        #     Asset.id.key
        # )
    )
