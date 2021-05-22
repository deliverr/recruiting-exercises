import unittest
from inventory_allocator import InventoryAllocator


class Test(unittest.TestCase):

    def test_happy_case(self):
        # test for exact inventory match
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_not_enough_inventory(self):
        # test for not enough inventory
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_split_across_warehouses(self):
        # test for splitting item across warehouses
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

        # test for splitting order across warehouses
        order = {'apple': 5, 'banana': 5, 'orange': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}]
        output = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

        # test for splitting item and splitting order across warehouses
        order = {'apple': 15, 'banana': 5, 'orange': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
                     {'name': 'dm', 'inventory': {'apple': 10, 'banana': 5, 'orange': 10}}]
        output = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'apple': 10, 'banana': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_no_order(self):
        # test for no order places
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_no_inventory(self):
        # test for no inventory details
        order = {'apple': 1}
        inventory = []
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_no_order_no_inventory(self):
        # test for no order placed and no inventory details
        order = {}
        inventory = []
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def test_no_item(self):
        # test for item not found in inventory
        order = {'kiwi': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)


if __name__ == '__main__':
    unittest.main()
