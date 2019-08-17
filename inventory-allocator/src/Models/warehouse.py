import json


class Warehouse(object):

    def __init__(self, json_object):
        self.name = ""
        self.inventory = {}
        self.__dict__ = json_object

    @classmethod
    def new(cls):
        dummy_string = '{ "name": "", "inventory": {} }'
        return cls(json.loads(dummy_string))

    def __repr__(self):
        return json.dumps({self.name: self.inventory}).replace('"', '')
