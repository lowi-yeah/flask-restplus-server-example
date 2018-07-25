# encoding: utf-8
"""
Blockchain extension
====================
"""

from bigchaindb_driver import BigchainDB
from config import BaseConfig
from app.extensions.cryptography.keys import get_keypair
from app.extensions.blockchain.models import Transaction

from app.modules.assets.models import Asset


class Blockchain(object):
    """
    Blockchain extension
    """

    def __init__(self, app=None):
        self.bigchain = BigchainDB(BaseConfig.BIGCHAINDB__URL)
        self.logger = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Common Flask interface to initialize the blockchain connection
        """
        self.logger = app.logger
        self.logger.debug(f'init blockchain. url: {BaseConfig.BIGCHAINDB__URL}')

    def create_asset(self, asset):
        """
        Put an asset onto the blockchain
        """
        self.logger.debug(f'create_asset. {asset}')

        rddl_privkey, rddl_pubkey = get_keypair('rnc')
        data = {'data': {'id': asset.id}}
        metadata = {'hash_digest': asset.metadata}

        # prepare the transaction with the digital asset and issue 10 tokens for Bob
        prepared_token_tx = self.bigchain.transactions.prepare(
            operation='CREATE',
            signers=rddl_pubkey,
            asset=data,
            metadata=metadata)

        # fulfill and send the transaction
        fulfilled_token_tx = self.bigchain.transactions.fulfill(
            prepared_token_tx,
            private_keys=rddl_privkey)

        tx = self.bigchain.transactions.send(fulfilled_token_tx)
        return Transaction(tx)

    def retrieve_asset(self, asset_id):
        asset_search_results = self.bigchain.assets.get(search=asset_id)
        if len(asset_search_results) is 0:
            return None

        search_result = asset_search_results[0]
        transactions = self.bigchain.transactions.get(asset_id=search_result['id'])
        transaction = next(iter(transactions), None)

        if transaction is None:
            return None

        return Asset(transaction['asset']['data']['id'], transaction['metadata']['hash_digest'])

    def retrieve_transaction(self, tx_id):
        return self.bigchain.transactions.retrieve(txid=tx_id)
