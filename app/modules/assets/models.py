# encoding: utf-8

"""
Asset data model
--------------------
"""


class Asset(object):
    def __init__(self, asset_id, metadata_digest):
        self.asset_id = asset_id
        self.metadata_digest = metadata_digest

    def __repr__(self):
        return '<Asset(asset_id={self.asset_id!r}, metadata_digest={self.metadata_digest!r})>'.format(self=self)
