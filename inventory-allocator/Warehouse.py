"""
@author: Priyans Nishithkumar Desai

"""

from Inventory import Inventory

class Warehouse(object):

    """
    This is the Warehouse class, handling all the functionalities of a particular warehouse. 
    """

    def __init__(self, name, inventory, cost):
        """
        This function initializes an instance of the Warehouse Class. 

        Input:
            name: name of the warehouse
            inventory: an instance of the Inventory class specifying the items of the inventory

        Output:
            None
        """

        # Name of the warehouse (String)
        self.name = name

        # Inventory of the warehouse (Dictionary with count of quantity of each item)
        self.inventory = Inventory(inventory)

        # Cost is calculated by the order it comes in overall inventory (int)
        self.cost = cost

        # The Individual shipment of the warehouse which is combined at the end. 
        self.shipment = []

    def check_availability(self, order_item):
        """
        Aim: Checks how much of an item is available in the Warehouse's inventory
        Input: 
            self (Warehouse) - This Warehouse
            order_item (Item) - An instance of the Item class whose quantity needs to be checked

        Output:
            int - the amount of order_item
        """

        # Checks in the inventory the quantity available of the order_item
        return self.inventory.check_item(order_item)

    def add_shipment(self, order_item, quantity):
        """
        Aim: Adds an order_item to this warehouse's individual shipment
        Input:
            order_item (Item) - which item needs to be ordered
            quantity (int) - how much of the item needs to be ordered
        """

        # Orders from the inventory and adjusts the stock after quantity is taken for shipment
        self.inventory.order(order_item, quantity)

        # Appends the order to the shipment
        self.shipment.append((order_item.name, quantity))

    def complete_delivery_of_shipment(self):
        """
        Aim: Tell the warehouse that its existing shipment delivery is complete. 
        Input:
            self (Warehouse) - this warehouse
        Output:
            None
        """
        self.shipment = []
