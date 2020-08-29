"""
@author: Priyans Nishithkumar Desai

"""

from Item import Item

class Inventory(object):

    """
    This is the implementation of the Inventory class, which keeps stocks item available in a warehouse
    """

    def __init__(self, items_dictionary):
        """
        This method initializes an instance of the the Inventory

        Input:
            items_dictionary (dict) - Specifies how much of a particular item is present
        """

        # stores how much of a particular item is available in an invetory. 
        self.stock = {}
        for (order_item, order_value) in items_dictionary.items():
            self.stock[order_item] = Item(order_item, order_value)

    def check_item(self, item):
        """
        Aim: Checks how much of an item is in the inventory
        Input:
            item (string) - the item that needs to be checked.

        Output:
            int - the amount of the item if available in the inventory
        """

        # Checks if the item is available in the inventory
        item_in_stock = self.stock.get(item.name, None)

        # If item is available, then its quantity is returned. 
        if item_in_stock:
            return item_in_stock.quantity
        else:
            return 0

    def order(self, order_item, quantity):
        """
        Aim: Places an order on the inventory and adjusts the stock after the order. 
        Input:
            order_item (Item) - the item that is being ordered.
            quantity - the amount of the item that is being ordered. 
        """

        # Checks if the item is available in the inventory
        item_in_stock = self.stock.get(order_item.name, None)

        # If the item is available, then its new quantity is set considering this order. 
        if item_in_stock:
            item_in_stock.set_new_quantity(item_in_stock.quantity - quantity)