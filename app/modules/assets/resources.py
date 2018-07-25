# encoding: utf-8

"""
RESTful API Assets
------------------
"""

from flask_restplus._http import HTTPStatus

from app.extensions.api import abort
from app.extensions.api.parameters import PaginationParameters
from app.extensions import blockchain
from app.extensions.api import Namespace
from app.extensions.blockchain.schemas import TransactionSchema
from flask_restplus_patched import Resource
from . import parameters
from .models import Asset
from .schemas import AssetSchema
from app.extensions.cryptography.schemas import Ed25519KeySchema

api = Namespace('asset',
                description="Assets",
                validate=True)


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
    @api.response(TransactionSchema(strict=True), code=HTTPStatus.CREATED)
    @api.response(code=HTTPStatus.CONFLICT)
    @api.response(code=HTTPStatus.BAD_REQUEST)
    def post(self, args):
        """
        Create a new asset.
        """
        asset = Asset(**args)

        # precondition
        # make sure there is no asset with the same id
        existing_asset = blockchain.get_asset(asset.id)
        if not (existing_asset is None):
            abort(code=HTTPStatus.CONFLICT,
                  message=f'Assets with id \'{asset.id}\' already exists')

        try:
            return blockchain.create_asset(asset), HTTPStatus.CREATED
        except Exception as e:
            abort(code=HTTPStatus.BAD_REQUEST,
                  message=f'Unknown error: {e}')


@api.route('/<string:asset_id>')
class AssetByID(Resource):
    """
    Manipulations with a specific asset.
    """

    # @api.parameters(parameters.GetAssetParameters())
    @api.response(AssetSchema(strict=True),
                  code=HTTPStatus.OK)
    @api.response(
        code=HTTPStatus.NOT_FOUND,
        description='Asset not found.')
    def get(self, asset_id):
        """
        Get asset details by ID.
        """

        # validate the asset_id manually, since I don't know how to make marshmallow aware of the
        # url/path parameter. using the @api.parameters decorator creates a query parameter, which is not what we want

        asset = blockchain.get_asset(asset_id)
        if asset is None:
            abort(code=HTTPStatus.NOT_FOUND, message=f'Asset not found: {asset_id}')

        return asset, HTTPStatus.OK

    @api.response(AssetSchema(), code=HTTPStatus.OK)
    @api.response(code=HTTPStatus.CONFLICT)
    def patch(self, args, asset):
        """
        Patch asset metadata by ID.
        """
        # tx = bigchain.updateMetadata(asset)
        return asset


@api.route('/<string:asset_id>/transactions/')
@api.response(code=HTTPStatus.NOT_FOUND,
              description="asset not found.")
class AssetTransactions(Resource):
    """
    Transactions of a given asset
    """

    @api.parameters(PaginationParameters())
    @api.response(TransactionSchema(many=True))
    def get(self, args, asset_id):
        """
        Get transactions of an asset with the id 'asset_id'.
        """
        return blockchain.get_asset_transactions(asset_id=asset_id, offset=args['offset'], limit=args['limit'])
