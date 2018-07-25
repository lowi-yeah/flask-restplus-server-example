from marshmallow.validate import ValidationError, Validator
from app.extensions.cryptography.base_58 import b58decode, calculate_entropy
from config import BaseConfig


def validate_public_key(value):
    """
    Validate that the given value is in the format of a base58-encoded Ed25519 key
    :param value: The value to be validated
    :raises: ValidationError
    """
    if not value:
        raise ValidationError('key cannot be None')

    if len(value) < BaseConfig.PUBLIC_KEY_LENGTH:
        raise ValidationError('key too short')

    if len(value) > BaseConfig.PUBLIC_KEY_LENGTH:
        raise ValidationError('key too long')

    if calculate_entropy(value) < 1:
        raise ValidationError('key not random enough')

    # encoding: base58
    try:
        b58decode(value)
    except ValueError:
        raise ValidationError('not base58')


class Ed25519Key(Validator):
    """Validate an base58-encoded Ed25519 key.

    :param str error: Error message to raise in case of a validation error. Can be
        interpolated with `{input}`.
    """

    default_message = 'Not a valid public key.'

    def __init__(self, error=None):
        self.error = error or self.default_message

    def _format_error(self, value):
        return self.error.format(input=value)

    def __call__(self, value):
        validate_public_key(value)
        raise ValidationError('WAT')
        # return value


def validate_hash_digest(value):
    """
       Validate that the given value is in the format of a sha3/256 digest
       :param value: The value to be validated
       :raises: ValidationError
       """
    if not value:
        raise ValidationError('hash digest cannot be None')

    if len(value) < BaseConfig.SHA3_256_DIGEST_LENGTH:
        raise ValidationError('hash digest too short')

    if len(value) > BaseConfig.SHA3_256_DIGEST_LENGTH:
        raise ValidationError('hash digest too long')

    if calculate_entropy(value) < 1:
        raise ValidationError('hash digest not random enough')


class SHA3256(Validator):
    """Validate a SHA3 256 hash digest.
       :param str error: Error message to raise in case of a validation error. Can be
           interpolated with `{input}`.
       """

    default_message = 'Not a valid sha3 256 digest.'

    def __init__(self, error=None):
        self.error = error or self.default_message

    def _format_error(self, value):
        return self.error.format(input=value)

    def __call__(self, value):
        validate_hash_digest(value)
        raise ValidationError('F00')
        # return value
