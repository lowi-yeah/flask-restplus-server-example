import numpy as np
from math import log, e

# lifted from: https://github.com/keis/base58/blob/master/base58.py

# 58 character alphabet used
alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

iseq, bseq, buffer = (
    lambda s: s,
    bytes,
    lambda s: s.buffer)


def calculate_entropy(data, base=None):
    """
    Computes entropy of the public key.
    Lifted from https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
    """

    if isinstance(data, str):
        data = list(data)

    n_labels = len(data)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(data, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy
    base = e if base is None else base
    for i in probs:
        ent -= i * log(i, base)

    return ent


def scrub_input(v):
    if isinstance(v, str) and not isinstance(v, bytes):
        v = v.encode('ascii')

    if not isinstance(v, bytes):
        raise TypeError(
            "a bytes-like object is required (also str), not '%s'" %
            type(v).__name__)

    return v


def b58decode_int(v):
    """Decode a Base58 encoded string as an integer"""

    v = scrub_input(v)
    decimal = 0
    for char in v:
        decimal = decimal * 58 + alphabet.index(char)
    return decimal


def b58decode(v):
    """Decode a Base58 encoded string"""
    v = scrub_input(v)
    origlen = len(v)
    v = v.lstrip(alphabet[0:1])
    newlen = len(v)

    acc = b58decode_int(v)

    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)

    return (b'\0' * (origlen - newlen) + bseq(reversed(result)))
