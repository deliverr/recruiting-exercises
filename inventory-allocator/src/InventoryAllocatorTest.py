import unittest
from InventoryAllocator import InventoryAllocator

"""
Usage:
$ python3 InventoryAllocatorTest.py

"""

class InventoryAllocatorTest(unittest.TestCase):
    def test_simple_case(self):
        print("Simple Case:")
        allocator = InventoryAllocator()
        order = {'apple': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 1}}]
        expected = [{'owd': {'apple': 1}}]
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_not_enough_case(self):
        print("Not Enough Inventory Case:")
        allocator = InventoryAllocator()
        order = {'apple': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 0}}]
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_split_case(self):
        print("Split Case:")
        allocator = InventoryAllocator()
        order = {'apple': 10}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5}},
                  {'name': 'dm', 'inventory': {'apple': 5}}]
        expected = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_no_order_case(self):
        print("No Order Case:")
        allocator = InventoryAllocator()
        order = {}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5}}]
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_no_warehouse_case(self):
        print("No Warehouse Case:")
        allocator = InventoryAllocator()
        order = {'apple': 10}
        warehouse = []
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_none_order_case(self):
        print("None Input Case:")
        allocator = InventoryAllocator()
        order = None
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5}}]
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_none_warehouse_case(self):
        print("None Warehouse Case:")
        allocator = InventoryAllocator()
        order = {'apple': 10}
        warehouse = None
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_multi_input_case(self):
        print("Multi Input Case:")
        allocator = InventoryAllocator()
        order = {'apple': 10, 'banana': 5}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 0}},
                    {'name': 'dm', 'inventory': {'apple': 5, 'banana': 5}}]
        expected = [{'owd': {'apple': 5}},
                    {'dm': {'apple': 5, 'banana': 5}}]
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_partly_fullfilled_case(self):
        print("Party Fullfilled Case:")
        allocator = InventoryAllocator()
        order = {'apple': 11, 'banana': 5}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 0}},
                    {'name': 'dm', 'inventory': {'apple': 5, 'banana': 2}}]
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")

    def test_wrong_item_case(self):
        print("Party Fullfilled Case:")
        allocator = InventoryAllocator()
        order = {'apple': 11, 'banana': 5}
        warehouse = [{'name': 'owd', 'inventory': {'peach': 5, 'orange': 10}},
                    {'name': 'dm', 'inventory': {'grape': 5, 'lemon': 2}}]
        expected = []
        self.assertEqual(allocator.allocate(order, warehouse), expected)
        print("Test Passed!")


if __name__ == '__main__':
    print("Running tests for Inventory Allovator:")
    unittest.main()
