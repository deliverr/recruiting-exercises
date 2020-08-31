"""
@author: Priyans Nishithkumar Desai

"""

from Inventory import Inventory
from Item import Item
from Warehouse import Warehouse
from Order import Order

class Main(object):
    """
    The Driver class for running the inventory allocation for a particular oder. 
    """

    def __init__(self, order, warehouses):

        """
        This method initializes an instance of the driver class for this order.

        Input:
            order (dict) - a dictionary of orders
            warehouses (List[Dict]) - a list of dictionaries of different warehouses.  
        """

        # raw_order in a dictionary form
        self.raw_order = order

        # raw warehouses to be processed 
        self.raw_warehouses = warehouses

        # Processing of the warehouses' dictionary
        self.warehouses = self.add_warehouses()

        # Processing of the order dictionary. 
        self.order = self.add_order()

    def add_warehouses(self):
        """
        Aim: Processes the warehouses given in a raw format

        Input:
            self - instance of the Main driver class. 

        Output:
            List[Warehouse] - a list of warehouses (instances of the Warehouse class)
        """
        warehouses = []
        for index in range(len(self.raw_warehouses)):
            warehouse = self.raw_warehouses[index]

            # Instance of a Warehouse is created with index + 1 as its cost. 
            new_warehouse = Warehouse(warehouse['name'], warehouse['inventory'], index + 1)
            warehouses.append(new_warehouse)
        return warehouses

    def add_order(self):
        """
        Aim: Processes the order given in a raw format

        Input:
            self - instance of the Main driver class. 

        Output:
            Order - an instance of the Order class
        """
        return Order(self.raw_order, self.warehouses)

    def find_cheapest_shipment(self):
        """
        Aim: Finds the cheapest shipment 

        Input:
            self - instance of the Main driver class. 

        Output:
            dict
                key: name of the warehouse
                value: a dictionary of items with their quantities
        """
        shipment = self.order.prepare_shipment()
        result = {}
        for warehouse in shipment:
            if warehouse.name in result:
                for item in warehouse.shipment:
                    result[warehouse.name][item[0]] = item[1]
            else:
                result[warehouse.name] = {}
                for item in warehouse.shipment:
                    result[warehouse.name][item[0]] = item[1]
        return result

order = {"apple": 6, "orange": 4, "banana": 4}
warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2} }, 
        { "name": "amazon", "inventory": {"banana": 2, "apple": 3}},  
        { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 2}},
    ]
main = Main(order, warehouses)
shipment = main.find_cheapest_shipment()
print(shipment)