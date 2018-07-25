from config import BaseConfig
import json


def _get_predefined_keys():
    """
    OUT
        <dict>
    """

    # The file is read everytime a key is requested, so we can modify it "on the fly"
    with open(BaseConfig.PREDEFINED_KEYS_FILE, 'r') as f:
        return json.load(f)


def get_keypair(item_key):
    """
    IN
        item_key <str>
            "rnc" (riddle & code)
            "producer"
            "product"
            "future_owner"

    OUT
        (<private key:str>, <public key:str>) (<tuple>)
    """

    keys = _get_predefined_keys()
    if item_key in keys:
        return tuple(keys.get(item_key))

    else:
        raise Exception(f'Non existing key: {item_key}')
