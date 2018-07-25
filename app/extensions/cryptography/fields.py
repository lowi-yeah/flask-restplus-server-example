from marshmallow import fields


class PublicKey(fields.Field):
    """
    Marshmallow field for representing public keys
    """
    def _serialize(self, value, attr, obj):
        if value is None:
            return ''
        return value

    # def _deserialize(self, value, attr, data):
