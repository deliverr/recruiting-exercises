"""
@author: Priyans Nishithkumar Desai

File Description:
    Main driver class for managing various orders

"""

from Inventory import Inventory
from Item import Item
from Warehouse import Warehouse
from Order import Order

class Main(object):

    def __init__(self, order, warehouses):
        self.raw_order = order
        self.raw_warehouses = warehouses
        self.warehouses = self.add_warehouses()
        self.order = self.add_order()

    def add_warehouses(self):
        warehouses = []
        for index in range(len(self.raw_warehouses)):
            warehouse = self.raw_warehouses[index]
            new_warehouse = Warehouse(warehouse['name'], warehouse['inventory'], index)
            warehouses.append(new_warehouse)
        return warehouses

    def add_order(self):
        return Order(self.raw_order, self.warehouses)

    def find_cheapest_shipment(self):
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



main = Main({"apple": 5, "banana": 2, "orange": 4}, [
    { "name": "owd", "inventory": { "apple": 5} }, 
    { "name": "dm", "inventory": { "apple": 5, "banana": 2, "orange": 4}}, ])
shipment = main.find_cheapest_shipment()
print(shipment)


order = {"banana": 2, "orange": 6, "guava": 30, "pineapple": 100, "strawberries": 400, "raspberries": 20, "apple": 50, "grapes": 20}
warehouses =  [
        { "name": "owd", "inventory": { "apple": 2, "orange": 2, "pineapple": 10}}, 
        { "name": "amazon", "inventory": {"banana": 1, "orange": 3}},  
        { "name": "dm", "inventory": { "apple": 20, "banana": 2, "orange": 5, "pineapple": 120}},
        { "name": "flipkart", "inventory": {"apple": 30, "strawberries": 40}},
        { "name": "wish", "inventory": {"guava": 10, "strawberries": 100}}, 
        { "name": "bigbasket", "inventory": {"raspberries": 25, "strawberries": 200}}, 
        { "name": "berkeley bowl", "inventory": {"strawberries": 100, "grapes": 20, "guava": 50}}
    ]
main = Main(order, warehouses)
shipment = main.find_cheapest_shipment()
expected = {
        'dm': {'banana': 2, 'orange': 1, 'pineapple': 100, 'apple': 20}, 
        'owd': {'orange': 2}, 
        'amazon': {"orange": 3}, 
        'berkeley bowl': {"guava": 30, "grapes": 20, "strawberries": 60}, 
        'wish': {'strawberries': 100}, 
        'flipkart': {'strawberries': 40, "apple": 28}, 
        'bigbasket': {'strawberries': 200, 'raspberries': 20}
    }

print(shipment)


