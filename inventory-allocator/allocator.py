import unittest
from typing import List


class Warehouse(unittest.TestCase):
    def testHappyCase(self):
        order = {"apple": 4}
        inventory = [{"name": "owd", "inventory": {"apple": 4}}]
        output = [{"owd": {"apple": 4}}]
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testNotEnoughInvenctory(self):
        order = {"apple": 10}
        inventory = [{"name": "owd", "inventory": {"apple": 0}}]
        output = []
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 0}}]
        self.assertEqual(inventory, inventoryAfterOrder)

    def testSplit(self):
        order = {"apple": 10}
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = [{"dm": {"apple": 5}}, {"owd": {"apple": 5}}]
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testEmptyOrder(self):
        order = dict()
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testOutOfStockItem(self):
        order = {"dragonfruit": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 5, "dragonfruit": 0}}, {"name": "dm", "inventory": {"apple": 5, "dragonfruit": 0}}]
        output = []
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 5, "dragonfruit": 0}}, {"name": "dm", "inventory": {"apple": 5, "dragonfruit": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testNewItem(self):
        order = {"dragonfruit": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testMultipleOrders(self):
        order = {"apple": 20, "dragonfruit": 7, "perpetualMotionMachine": 68}
        inventory = [{"name": "owd", "inventory": {"apple": 15, "dragonfruit": 12}}, {"name": "dm", "inventory": {"apple": 25}}]
        output = [{"dm": {"apple": 5}}, {"owd": {"apple": 15, "dragonfruit": 7}}]
        inventoryAftertheOrder = [{"name": "owd", "inventory": {"apple": 0, "dragonfruit": 5}}, {"name": "dm", "inventory": {"apple": 20}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

class Warehouse(object):
    def bestwarehouseShipment(self, order: dict, inventory: List[dict]):
        """
        :param order: dict
        :param inventory: List[dict]
        :return: List[dict]
        """

        shipment = []

        # will loop through each warehouse
        for warehouse in inventory:

            # The search will be stopped if not the order
            if not order:
                break

            currentAllocation = dict()
            fulfilledRequests = set()
            warehouseUsed = False

            # See if the warehouse supplies each item we still need
            for item in order:
                if item in warehouse["inventory"]:

                    # Supply exactly as much is available, and no more
                    amountSupplied = min(order[item], warehouse["inventory"][item])
                    warehouse["inventory"][item] -= amountSupplied
                    order[item] -= amountSupplied

                    # Note that a warehouse supplied something to us, and note fulfilled parts of the order
                    if amountSupplied > 0:
                        warehouseUsed = True
                    if order[item] == 0:
                        fulfilledRequests.add(item)
                    currentAllocation[item] = amountSupplied

            # print the warehouse that provided the order else do not print the warehouse name 
            if warehouseUsed:
                shipment.append({warehouse["name"]: currentAllocation})
            for item in fulfilledRequests:
                del order[item]


        return sorted(shipment, key = lambda allocation: list(allocation.keys())[0])

if __name__ == "__main__":
    unittest.main(verbosity=2)
