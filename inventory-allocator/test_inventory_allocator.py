import unittest
from constants import NAME, INVENTORY
from inventory_allocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):
    def test_happy_case(self):
        # Happy case where order = inventory of a warehouse
        orders = {'apple': 1}
        warehouses = [{NAME: 'owd', INVENTORY: {'apple': 1}}]
        res = [{'owd': {'apple': 1}}]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_no_allocation(self):
        # No allocation case where order > inventory of any warehouses
        orders = {'apple': 1}
        warehouses = [{NAME: 'owd', INVENTORY: {'apple': 0}}]
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_perfect_split(self):
        # Split order over multiple warehouses perfectly
        orders = {'apple': 10}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 5
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 5
            }
        }]
        res = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_no_allocation_split(self):
        # Order cannot be fulfilled due to lack of inventory across all warehouses
        orders = {'apple': 11}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 5
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 5
            }
        }]
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_happy_case_found_later(self):
        # Order fulfilled by not the first (cheapest) warehouse
        orders = {'mango': 2}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 1
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'mango': 5
            }
        }]
        res = [{'dm': {'mango': 2}}]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_multiple_orders(self):
        # Order multiple items from different warehouses
        orders = {'apple': 5, 'banana': 5, 'orange': 5}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 1,
                'orange': 3
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 4,
                'orange': 3,
                'banana': 5
            }
        }]
        res = [{
            'owd': {
                'apple': 1,
                'orange': 3
            }
        }, {
            'dm': {
                'apple': 4,
                'orange': 2,
                'banana': 5
            }
        }]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_no_warehouses(self):
        # Empty warehouses list
        orders = {'apple': 5, 'banana': 5, 'orange': 5}
        warehouses = []
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_no_orders(self):
        # Empty orders
        orders = {}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 1,
                'orange': 3
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 4,
                'orange': 3,
                'banana': 5
            }
        }]
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_no_orders_and_no_warehouses(self):
        # Empty warehouses list and orders
        orders = {}
        warehouses = []
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_zero_quantity(self):
        # Order something with 0 quantity
        orders = {'apple': 0}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 5
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 5
            }
        }]
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_negative_quantity(self):
        # Order something with negative quantity
        orders = {'apple': -10}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 5
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 5
            }
        }]
        res = []
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_multiple_orders_with_no_allocation(self):
        # Order multiple items with an order item that cannot be fulfilled
        orders = {'apple': 5, 'banana': 5, 'orange': 15}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 1,
                'orange': 3
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 4,
                'orange': 3,
                'banana': 5
            }
        }]
        res = [{
            'owd': {
                'apple': 1,
            }
        }, {
            'dm': {
                'apple': 4,
                'banana': 5
            }
        }]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)

    def test_invalid_warehouse_input(self):
        # Input an invalid warehouse object
        orders = {'apple': 1}
        warehouses = [{NAME: 'owd', 'invent': {'apple': 10}}]
        res = []
        with self.assertRaises(ValueError):
            InventoryAllocator().inventory_allocator(orders, warehouses)

    def test_multiple_orders_with_multiple_splits(self):
        # Order multiple items from multiple different warehouses 
        orders = {'apple': 5, 'banana': 5, 'orange': 15, 'mango': 100}
        warehouses = [{
            NAME: 'owd',
            INVENTORY: {
                'apple': 10,
                'orange': 3,
                'mango': 30,
                'guava': 9
            }
        }, {
            NAME: 'dm',
            INVENTORY: {
                'apple': 4,
                'orange': 23,
                'banana': 5,
                'mango': 20
            }
        }, {
            NAME: 'gg',
            INVENTORY: {
                'apple': 40,
                'orange': 2,
                'banana': 5,
                'mango': 300
            }
        }]
        res = [{
            'owd': {
                'apple': 5,
                'orange': 3,
                'mango': 30
            }
        }, {
            'dm': {
                'orange': 12,
                'banana': 5,
                'mango': 20
            },
        }, {
            'gg': {
                'mango': 50
            },
        }]
        self.assertEqual(
            InventoryAllocator().inventory_allocator(orders, warehouses), res)


if __name__ == "__main__":
    unittest.main()
