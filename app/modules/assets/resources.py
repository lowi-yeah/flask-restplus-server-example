# encoding: utf-8

"""
RESTful API Assets
------------------
"""

from flask_restplus._http import HTTPStatus
from app.extensions import blockchain
from app.extensions.api import Namespace
from app.extensions.api.parameters import PaginationParameters
from app.extensions.blockchain.schemas import TransactionSchema
from flask_restplus_patched import Resource
from . import parameters
from .models import Asset
from .schemas import AssetSchema

api = Namespace('asset', description="Assets")  # pylint: disable=invalid-name


@api.route('/')
class Assets(Resource):
    """
    Manipulations of assets.
    """

    @api.parameters(PaginationParameters())
    @api.response(AssetSchema(many=True))
    def get(self, _args):
        """
        List of assets.

        Returns a list of assets starting from ``offset`` limited by ``limit``
        parameter.
        """
        hash_digest = '6df43c5cc25b1630b8aafee95f038dc9fedd7b096c82bf7b3f05d552772b6558'
        asset = Asset(asset_id="Monty", metadata_hash_digest=hash_digest)
        return [asset]

    @api.parameters(parameters.CreateAssetParameters())
    @api.response(TransactionSchema())
    @api.response(code=HTTPStatus.CONFLICT)
    def post(self, args):
        """
        Create a new asset.
        """
        asset = Asset(**args)
        tx = blockchain.create_asset(asset)
        return tx


@api.route('/<string:asset_id>')
@api.response(
    code=HTTPStatus.NOT_FOUND,
    description="Asset not found.")
class AssetByID(Resource):
    """
    Manipulations with a specific asset.
    """

    @api.response(AssetSchema())
    def get(self, asset_id):
        """
        Get asset details by ID.
        """
        return blockchain.retrieve_asset(asset_id)

    # @api.parameters(parameters.PatchAssetMetadataParameters())
    @api.response(AssetSchema())
    @api.response(code=HTTPStatus.CONFLICT)
    def patch(self, args, asset):
        """
        Patch asset metadata by ID.
        """
        # tx = bigchain.updateMetadata(asset)
        return asset

    @api.response(code=HTTPStatus.CONFLICT)
    @api.response(code=HTTPStatus.NO_CONTENT)
    def delete(self, asset):
        """
        Delete an asset by ID.
        """
        # obacht: we're working with blockchains here. this implies that assets cannot be deleted
        return None

#
# @api.route('/<int:team_id>/transactions/')
# @api.response(
#     code=HTTPStatus.NOT_FOUND,
#     description="asset not found.",
# )
# @api.resolve_object_by_model(Asset, 'asset')
# class AssetTransactions(Resource):
#     """
#     Manipulations of transactions of a specific asset
#     """
#
#     @api.parameters(PaginationParameters())
#     @api.response(AssetSchema(many=True))
#     def get(self, args, asset):
#         """
#         Get transactions by asset ID.
#         """
#         transactions = "get_asset_transactions(asset=asset, offset=args['offset'], limit=args['limit'])"
#         return transactions
