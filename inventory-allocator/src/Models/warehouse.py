"""
Author: Carl Zhou
Inventory Allocator Recruiting Exercise for Deliverr
Warehouse Object for Modeling Inventory Data
"""
# encoding: utf-8
import json


class Warehouse(object):

    def __init__(self, json_object):
        self.name = ""
        self.inventory = {}
        self.__dict__ = json_object

    '''
    for creating an empty warehouse object
    '''

    @classmethod
    def new(cls):
        dummy_string = '{ "name": "", "inventory": {} }'
        return cls(json.loads(dummy_string))

    '''
    overload this for printing output
    '''

    def __repr__(self):
        if self.name == '':
            return ''
        return json.dumps({self.name: self.inventory}).replace('"', '')

    '''
    overload == for unit testing
    '''

    def __eq__(self, other):
        return self.name == other.name and self.inventory == other.inventory
