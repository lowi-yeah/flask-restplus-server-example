# encoding: utf-8

"""
Transaction data models.
Just a serialization wrapper around a bigchainDB driver transaction
--------------------
"""


class ConditionDetails(object):
    # "public_key": "ALE8vDeiu4RornKHZ1i15dBkqXKMiwFor9Wr2durC4yj",
    # "type":       "ed25519-sha-256" }
    def __init__(self, details):
        self.public_key = details['public_key']
        self.type = details['type']


class Condition(object):
    # "details": Details
    # "uri": "ni:///sha-256;T3muw59ScsNDahwI-GG6mK9g7Unc0Tk4VoGfPhg2clM?fpt=ed25519-sha-256&cost=131072"
    def __init__(self, condition):
        self.uri = condition['uri']
        self.details = ConditionDetails(condition['details'])


class Output(object):
    # 'amount':        1
    # 'condition':     Condition
    # "public_keys": ["ALE8vDeiu4RornKHZ1i15dBkqXKMiwFor9Wr2durC4yj"]
    def __init__(self, tx_output):
        self.amount = tx_output['amount']
        self.condition = Condition(tx_output['condition'])
        self.public_keys = tx_output['public_keys']


# todo: Fulfills remain to be implemented
class Fulfill(object):
    def __init__(self, tx_fulfill):
        self.foo = tx_fulfill['bar']


class Input(object):
    # "fulfillment": "pGSAIIqmEjq07H09mSnEv4Kislvu2pKQIYpczUo4jBG_nQ8OgUCqT1Xcr1ey5UYyOBlyaBja_hIiaw95SG71gIQsjPEgo…"
    # "fulfills": "None",
    # "owners_before": ["ALE8vDeiu4RornKHZ1i15dBkqXKMiwFor9Wr2durC4yj"]
    def __init__(self, tx_input):
        if not (tx_input['fulfills'] is None):
            self.fulfills = list(map(lambda x: Fulfill(x), tx_input['fulfills']))
        self.fulfillment = tx_input['fulfillment']
        self.owners_before = tx_input['owners_before']


class Transaction(object):

    def __init__(self, tx):
        self.operation = tx['operation']
        self.version = tx['version']
        self.inputs = list(map(lambda x: Input(x), tx['inputs']))
        self.outputs = list(map(lambda x: Output(x), tx['outputs']))
        self.metadata = tx['metadata']
        self.asset = tx['asset']
        self.id = tx['id']

    def __repr__(self):
        return '<Transaction(name={self.id!r})>'.format(self=self)
