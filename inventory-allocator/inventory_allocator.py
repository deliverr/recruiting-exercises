from typing import List
import unittest

class InventoryAllocatorTest(unittest.TestCase):
    def testHappyCase(self):
        order = {"apple": 1}
        inventory = [{"name": "owd", "inventory": {"apple": 1}}]
        output = [{"owd": {"apple": 1}}]
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)
    
    def testNotEnoughInvenctory(self):
        order = {"apple": 1}
        inventory = [{"name": "owd", "inventory": {"apple": 0}}]
        output = []
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 0}}]
        self.assertEqual(inventory, inventoryAfterOrder)
    
    def testSplit(self):
        order = {"apple": 10}
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = [{"dm": {"apple": 5}}, {"owd": {"apple": 5}}]
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testEmptyOrder(self):
        order = dict()
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testOutOfStockItem(self):
        order = {"dragonfruit": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 5, "dragonfruit": 0}}, {"name": "dm", "inventory": {"apple": 5, "dragonfruit": 0}}]
        output = []
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 5, "dragonfruit": 0}}, {"name": "dm", "inventory": {"apple": 5, "dragonfruit": 0}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testNewItem(self):
        order = {"dragonfruit": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testTooMuchInventoryOverall(self):
        order = {"apple": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 15}}, {"name": "dm", "inventory": {"apple": 25}}]
        output = [{"dm": {"apple": 5}}, {"owd": {"apple": 15}}]
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 20}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testTooMuchInventorySingleWarehouse(self):
        order = {"apple": 20}
        inventory = [{"name": "owd", "inventory": {"apple": 25}}, {"name": "dm", "inventory": {"apple": 25}}]
        output = [{"owd": {"apple": 20}}]
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 25}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

    def testMultipleOrders(self):
        order = {"apple": 20, "dragonfruit": 7, "perpetualMotionMachine": 68}
        inventory = [{"name": "owd", "inventory": {"apple": 15, "dragonfruit": 12}}, {"name": "dm", "inventory": {"apple": 25}}]
        output = [{"dm": {"apple": 5}}, {"owd": {"apple": 15, "dragonfruit": 7}}]
        inventoryAfterOrder = [{"name": "owd", "inventory": {"apple": 0, "dragonfruit": 5}}, {"name": "dm", "inventory": {"apple": 20}}]
        self.assertEqual(output, InventoryAllocator().bestShipment(order, inventory))
        self.assertEqual(inventory, inventoryAfterOrder)

class InventoryAllocator(object):
    def bestShipment(self, order: dict, inventory: List[dict]):
        """
        :param order: dict
        :param inventory: List[dict]
        :return: List[dict]
        """

        shipment = []

        # Check each warehouse in the given order
        for warehouse in inventory:

            # Stop searching when our order is fulfilled
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

            # Only list warehouses that supplied anything at all, and erase fulfilled requests
            if warehouseUsed:
                shipment.append({warehouse["name"]: currentAllocation})
            for item in fulfilledRequests:
                del order[item]

        # Sorted output based on warehouse name
        return sorted(shipment, key = lambda allocation: list(allocation.keys())[0])

if __name__ == "__main__":
    unittest.main(verbosity=2)
