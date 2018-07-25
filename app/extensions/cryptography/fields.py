from marshmallow import fields


class PublicKey(fields.Field):
    """
    Marshmallow field for representing public keys
    """

    default_error_messages = {'invalid': 'Please provide a valid public key.'}

    def _serialize(self, value, attr, obj):
        print(f'_serialize public key {value}')
        if value is None:
            return ''
        return f'f00000{value}'

    def _deserialize(self, value, attr, data):
        print(f'_deserialize public key {value}')
        return value
