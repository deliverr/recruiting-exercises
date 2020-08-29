"""
@author: Priyans Nishithkumar Desai

"""


class Item(object):
    
    """
    This is the implementatioon of the Item class, which represents an item that is being ordered or stored in an
    inventory. 
    """
    
    def __init__ (self, name, value):
        """
        Aim: Initializes an instance of the Item Class. 

        Input:
            name (string) - name of the item
            value (int) - quantity of the item
        """

        # Name of the Item. 
        self.name = name

        # Quantity of the item being ordered or stored. 
        self.quantity = value

    def set_new_quantity(self, quantity):
        """
        Aim: After an order is processed, set the new quantity of the item in the inventory
        """
        self.quantity = quantity

