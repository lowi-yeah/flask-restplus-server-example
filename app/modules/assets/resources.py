# encoding: utf-8

"""
RESTful API Assets
------------------
"""

from flask_restplus._http import HTTPStatus

from app.extensions.api import abort
from app.extensions import blockchain
from app.extensions.api import Namespace
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

    # since we do not offer general querying for assets, this get on the root ns '/' is disabled
    # @api.response(AssetSchema(many=True))
    # def get(self, _args):
    #     """
    #     List of assets.
    #     ---------------
    #     Returns a list of assets starting from ``offset`` limited by ``limit``
    #     parameter.
    #     """

    @api.parameters(parameters.CreateAssetParameters())
    @api.response(TransactionSchema())
    @api.response(code=HTTPStatus.CONFLICT)
    @api.response(code=HTTPStatus.BAD_REQUEST)
    def post(self, args):
        """
        Create a new asset.
        """
        asset = Asset(**args)

        # precondition
        # make sure there is no asset with the same id
        existing_asset = blockchain.retrieve_asset(asset.id)
        if not (existing_asset is None):
            abort(code=HTTPStatus.CONFLICT,
                  message=f'Assets with id \'{asset.id}\' already exists')

        try:
            return blockchain.create_asset(asset)
        except Exception as e:
            abort(code=HTTPStatus.BAD_REQUEST,
                  message=f'Unknown error: {e}')


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
