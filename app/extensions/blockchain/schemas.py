# encoding: utf-8
"""
Serialization schemas for Transactions
----------------------------------------------------
"""

from flask_marshmallow import base_fields as fields
from flask_restplus_patched import Schema


class ConditionDetailsSchema(Schema):
    public_key = fields.String()
    type = fields.String()


class ConditionSchema(Schema):
    uri = fields.Url()
    details = fields.Nested(ConditionDetailsSchema)


class InputSchema(Schema):
    fulfillment = fields.Str()
    fulfills = fields.Str()
    owners_before = fields.List(fields.String)


class OutputSchema(Schema):
    amount = fields.Number()
    public_keys = fields.List(fields.String)
    condition = fields.Nested(ConditionSchema)


class TransactionSchema(Schema):
    """
    Schema for transactions.
    """
    id = fields.Str()
    version = fields.Str()
    operation = fields.Str()
    inputs = fields.Nested(InputSchema, many=True)
    outputs = fields.Nested(OutputSchema, many=True)
    asset = fields.Method('get_assset_id')
    metadata = fields.Method('get_metadata_digest')

    def get_assset_id(self, obj):
        return obj.asset['data']['id']

    def get_metadata_digest(self, obj):
        return obj.metadata['hash_digest']
