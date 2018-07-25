# encoding: utf-8
"""
Input arguments (Parameters) for Asset resources RESTful API
------------------------------------------------------------
"""

from flask_marshmallow import base_fields
from flask_restplus_patched import Parameters, PatchJSONParameters


class CreateAssetParameters(Parameters):
    asset_id = base_fields.String(
        description="Hex string")

    metadata_hash_digest = base_fields.String(
        description="sha3/256 digest of the metadata")


class PatchAssetMetadataParameters(PatchJSONParameters):
    # pylint: disable=abstract-method,missing-docstring
    OPERATION_CHOICES = (
        PatchJSONParameters.OP_REPLACE,
    )

    PATH_CHOICES = tuple(
        # '/%s' % field for field in (
        #     Asset.id.key
        # )
    )
