# encoding: utf-8
"""
Input arguments (Parameters) for Asset resources RESTful API
------------------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from flask_restplus_patched import Parameters, PatchJSONParameters

from app.extensions.cryptography.fields import PublicKey


class CreateAssetParameters(Parameters):
    asset_id = PublicKey(description="A public key representing the asset")
    metadata_digest = fields.String(description="sha3/256 digest of the metadata")


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
