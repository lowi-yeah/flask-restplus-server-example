# encoding: utf-8
"""
Asset data model
--------------------
"""
from marshmallow import validates


class Asset(object):
    def __init__(self, asset_id, metadata_digest):
        self.id = asset_id
        self.metadata = metadata_digest

    def __repr__(self):
        return '<Asset(id={self.id!r}, digest={self.metadata!r})>'.format(self=self)

