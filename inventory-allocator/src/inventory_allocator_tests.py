from inventory_allocator import InventoryAllocator

import unittest


class InventoryAllocatorTests(unittest.TestCase):
    """
    A class used to test the InventoryAllocator class functionality

    """

    # Case in which the items of the order match the inventory
    def test_inventory_match(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        order_output = [{'owd': {'apple': 1}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in which the items of the order cannot be satisfied by the inventory
    def test_inventory_insufficient(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        order_output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)
    
    # Case in which the order is split across multiple warehouses
    def test_order_split_across_warehouses(self):
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, 
                     {'name': 'dm', 'inventory': {'apple': 5}}]
        order_output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in the inventory is empty
    def test_inventory_blank(self):
        order = {'apple': 10}
        inventory = []
        order_output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in which the order is blank
    def test_order_blank(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}}, 
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}}]
        order_output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in which there are multiple items in the order
    def test_order_multiple_items(self):
        order = {'apple': 10, 'banana': 10, 'orange': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}}, 
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}}]
        order_output = [{'owd': {'apple': 10, 'banana': 5, 'orange': 10}}, {'dm': {'banana': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)
    
    # Case in which there are multiple items in the order and mutiple inventories
    def test_multiple_items_and_inventories(self):
        order = {'apple': 15, 'banana': 20, 'orange': 20}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}}, 
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}},
                     {'name': 'ca', 'inventory': {'apple': 5, 'orange': 10}}]
        order_output = [{'owd': {'apple': 10, 'banana': 5, 'orange': 15}}, {'dm': {'apple': 5, 'banana': 15, 'orange': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in which there is an item in the order which does not exist in the inventory
    def test_order_does_not_exist(self):
        order = {'apple': 15, 'banana': 20, 'orange': 20, 'kiwis': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}}, 
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}},
                     {'name': 'ca', 'inventory': {'apple': 5, 'orange': 10}}]
        order_output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.allocate_inventory(), order_output)

    # Case in which there is an invalid item in the order
    def test_invalid_order(self):
        order = {'apple': -15, 'banana': -20, 'orange': -1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}}]
        with self.assertRaises(AssertionError):
            InventoryAllocator(order, inventory).allocate_inventory()

    # Case in which there is an invalid item in the inventory
    def test_invalid_inventory(self):
        order = {'apple': 15, 'banana': 20, 'orange': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': -10, 'banana': 5, 'orange': 15}}]
        with self.assertRaises(AssertionError):
            InventoryAllocator(order, inventory).allocate_inventory()

if __name__ == '__main__':
    unittest.main()
