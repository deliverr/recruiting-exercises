import unittest 
from InventoryAllocator import InventoryAllocator

class Test(unittest.TestCase):

    # empty order placed
    def test_empty_order(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apples': 1}}]
        output = []
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # empty inventory
    def test_empty_inventory(self):
        order = {'apples': 1}
        inventory = []
        output = []
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # empty order and inventory
    def test_empty_order_and_inventory(self):
        # test for no order placed and no inventory details
        order = {}
        inventory = []
        output = []
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # same order placed as inventory
    def test_happy_case(self):
        order = {'apples': 5}
        inventory = [{'name': 'owd', 'inventory': {'apples': 5}}]
        output = [{'owd': {'apples': 5}}]
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # not enough stock as order placed
    def test_not_enough_stock(self):
        order = {'apples': 10}
        inventory = [{'name': 'owd', 'inventory': {'apples': 0}}]
        output = []
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # multiple warehouses' stock needed
    def test_stock_at_other_warehouses(self):
        # order at multiple warehouses
        order = {'apples': 5, 'grapes': 5, 'oranges': 5}
        inventory = [{'name': 'owd', 'inventory': {'apples': 5, 'oranges': 10}}, {'name': 'dm', 'inventory': {'grapes': 5, 'oranges': 10}}]
        output = [{'owd': {'apples': 5, 'oranges': 5}}, {'dm': {'grapes': 5}}]
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

        # item at multiple warehouses
        order = {'apples': 10}
        inventory = [{'name': 'owd', 'inventory': {'apples': 5}}, {'name': 'dm', 'inventory': {'apples': 5}}]
        output = [{'owd': {'apples': 5}}, {'dm': {'apples': 5}}]
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

        # item and order at multiiple warehouses
        order = {'apples': 15, 'grapes': 5, 'oranges': 5}
        inventory = [{'name': 'owd', 'inventory': {'apples': 5, 'oranges': 10}},
                     {'name': 'dm', 'inventory': {'apples': 10, 'grapes': 5, 'oranges': 10}}]
        output = [{'owd': {'apples': 5, 'oranges': 5}}, {'dm': {'apples': 10, 'grapes': 5}}]
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)

    # item placed in order doesn't exist in inventory
    def test_no_item(self):
        order = {'starfruits': 1}
        inventory = [{'name': 'owd', 'inventory': {'apples': 1}}]
        output = []
        allocate = InventoryAllocator(order, inventory)
        self.assertEqual(allocate.shipment(), output)


if __name__ == '__main__':
    unittest.main()