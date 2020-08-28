import unittest
from InventoryAllocator import InventoryAllocator


class InventoryAllocatorUnitTest(unittest.TestCase):
    inventory_alloc = InventoryAllocator()

        # Valid single warehouse order

    def single_warehouse_order(self):
        order = {'orange': 0, 'eggplant': 100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = [{'eggplant_inc': {'eggplant': 100}}]
        updated_stock = [{'name': 'owd', 'inventory': {'orange': 6, 'eggplant': 9900}}]
        self.assertEqual((result, inventory_alloc.inventory_allocator(order, stock)))
        self.assertEqual(stock, updated_stock)

        # Multiple warehouses

    def split_warehouse(self):
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

    def negative_order(self):
        order = {'orange': 0, 'eggplant': -100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Negative warehouse stock value

    def negative_stock(self):
        order = {'orange': 0, 'eggplant': -100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': -6, 'eggplant': -10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Order doesnt exist

    def order_dne(self):
        order = {'banganga': 10, 'cinnamon': 20}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 1, 'eggplant': 2}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Exact match

    def exacto_match(self):
        order = {'orange': 2, 'eggplant': 100}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = [{'eggplant_inc': {'orange': 2, 'eggplant': 100}}]
        updated_stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 0, 'eggplant': 0}},
                         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Order number is string

    def order_as_string(self):
        order = {'orange': 'Nen', 'eggplant': 'Gon'}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Warehouse name is number

    def warehouse_number(self):
        order = {'orange': 0, 'eggplant': 20}
        stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        result = {[{69: {'eggplant': 20}}]}
        updated_stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 80}},
                         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # Order item is number

    def order_as_id(self):
        order = {20: 2, 'eggplant': 20}
        stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
                 {'name': '20city', 'inventory': {20: 10, 'eggplant': 10}}]
        result = [{69: {'eggplant': 20}}, {'20city': {20: 2}}]
        updated_stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 80}},
                         {'name': '20city', 'inventory': {20: 8, 'eggplant': 10}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)

        # No warehouses

    def no_stock(self):
        order = {'apples': 10, 'starfruit': 9001}
        stock = []
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # No orders here today

    def no_order(self):
        order = {}
        stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
        result = []
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))

        # Deliverr Ironman

    def break_pls(self):
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
                         {'name': 'last stop', 'inventory': {'carrots': 100, 'eggplants': 1976, 'gum gum fruit': 0}},
                         {'name': "Mc Donald's", 'inventory': {'french fries': 0}}]
        self.assertEqual(result, inventory_alloc.inventory_allocator(order, stock))
        self.assertEqual(stock, updated_stock)


if __name__ == '__main__':
    unittest.main()
