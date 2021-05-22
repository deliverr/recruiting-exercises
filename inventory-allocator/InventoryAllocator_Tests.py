import unittest
from InventoryAllocator import InventoryAllocator


class InventoryAllocatorUnitTest(unittest.TestCase):
        # Valid single warehouse order

    def test_single_warehouse_order(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 0, 'eggplant': 100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = [{'eggplant_inc': {'eggplant': 100}}]
        updated_stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 9900}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Multiple warehouses

    def test_split_warehouse(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 2, 'eggplant': 100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 0, 'eggplant': 10000}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 0}}]
        result = [{'eggplant_inc': {'eggplant': 100}}, {'orange_city': {'orange': 2}}]
        updated_stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 0, 'eggplant': 9900}},
                         {'name': 'orange_city', 'inventory': {'orange': 8, 'eggplant': 0}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Negative order value
        # Properly checked that warehouse value did not increase

    def test_negative_order(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 0, 'eggplant': -100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Negative warehouse stock value

    def test_negative_stock(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 0, 'eggplant': -100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': -6, 'eggplant': -10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Order doesnt exist

    def test_order_dne(self):
        inventory_alloc = InventoryAllocator()
        order = {'banganga': 10, 'cinnamon': 20}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 1, 'eggplant': 2}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Exact match

    def test_exacto_match(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 2, 'eggplant': 100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = [{'eggplant_inc': {'orange': 2, 'eggplant': 100}}]
        updated_stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 0, 'eggplant': 0}},
                         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Order number is string

    def test_order_as_string(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 'Nen', 'eggplant': 'Gon'}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Warehouse name is number

    def test_warehouse_number(self):
        inventory_alloc = InventoryAllocator()
        order = {'orange': 0, 'eggplant': 20}
        stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = [{69: {'eggplant': 20}}]
        updated_stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 80}},
                         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Order item is number

    def test_order_as_id(self):
        inventory_alloc = InventoryAllocator()
        order = {20: 2, 'eggplant': 20}
        stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': '20city', 'inventory': {20: 10, 'eggplant': 10}}]
        result = [{69: {'eggplant': 20}}, {'20city': {20: 2}}]
        updated_stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 80}},
                         {'name': '20city', 'inventory': {20: 8, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # No warehouses

    def test_no_stock(self):
        inventory_alloc = InventoryAllocator()
        order = {'apples': 10, 'starfruit': 9001}
        stock = []
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # No orders here today

    def test_no_order(self):
        inventory_alloc = InventoryAllocator()
        order = {}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Deliverr Ironman

    def test_break_pls(self):
        inventory_alloc = InventoryAllocator()
        order = {'apples': 100, 'bananas': 100, 'carrots': 100, 'dandruff shampoo': 5, 'eggplants': 24,
                 'french fries': 2, 'gum gum fruit': 1}
        stock = [{'name': 'owd', 'inventory': {'apples': 20}},
                 {'name': 'dm', 'inventory': {'apples': 60, 'bananas': 50}},
                 {'name': 'mil', 'inventory': {'apples': 100, 'bananas': 500}},
                 {'name': 'hq', 'inventory': {'carrots': 0, 'dandruff shampoo': 5}},
                 {'name': 'last stop', 'inventory': {'carrots': 100, 'eggplants': 2000, 'gum gum fruit': 1}},
                 {'name': "Mc Donald's", 'inventory': {'french fries': 2}}]
        result = [{'owd': {'apples': 20}}, {'dm': {'apples': 60, 'bananas': 50}},
                  {'mil': {'apples': 20, 'bananas': 50}},
                  {'hq': {'dandruff shampoo': 5}},
                  {'last stop': {'carrots': 100, 'eggplants': 24, 'gum gum fruit': 1}},
                  {"Mc Donald's": {'french fries': 2}}]
        updated_stock = [{'name': 'owd', 'inventory': {'apples': 0}},
                         {'name': 'dm', 'inventory': {'apples': 0, 'bananas': 0}},
                         {'name': 'mil', 'inventory': {'apples': 80, 'bananas': 450}},
                         {'name': 'hq', 'inventory': {'carrots': 0, 'dandruff shampoo': 0}},
                         {'name': 'last stop', 'inventory': {'carrots': 0, 'eggplants': 1976, 'gum gum fruit': 0}},
                         {'name': "Mc Donald's", 'inventory': {'french fries': 0}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)


if __name__ == '__main__':
    unittest.main(verbosity=99)
