# encoding: utf-8

"""
Asset data model
--------------------
"""


class Asset(object):
    def __init__(self, asset_id, metadata_digest):
        self.id = asset_id
        self.metadata = metadata_digest

    def __repr__(self):
        return '<Asset(asset_id={self.id!r}, metadata_digest={self.metadata!r})>'.format(self=self)
