from InventoryAllocator import InventoryAllocator
import unittest


class InventoryAllocatorTest(unittest.TestCase):

    """ Tests shipping a single item from a single warehouse """

    def test_single(self):
        order = {'apple': 1}
        warehouse_inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests returning blank list when inventory is insufficient """

    def test_insufficient_inventory(self):
        order = {'apple': 1}
        warehouse_inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests returning blank list when order is empty """

    def test_blank_order(self):
        order = {}
        warehouse_inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests returning blank list when order is negative """

    def test_invalid_order(self):
        order = {'apple': -5}
        warehouse_inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests shipping items from multiple warehouses """

    def test_multiple_warehouses(self):
        order = {'apple': 5}
        warehouse_inventory = [
            {'name': 'owd', 'inventory': {'apple': 3}},
            {'name': 'dm', 'inventory': {'apple': 2}}]
        output = [
            {'owd': {'apple': 3}},
            {'dm': {'apple': 2}}]
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests shipping multiple items from one warehouse """

    def test_multiple_items(self):
        order = {'apple': 5, 'banana': 5, 'orange': 5}
        warehouse_inventory = [
            {'name': 'owd', 'inventory': {'apple': 5, 'banana': 5, 'orange': 5}}]
        output = [
            {'owd': {'apple': 5, 'banana': 5, 'orange': 5}},
        ]
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests shipping multiple items from multiple warehouses """

    def test_multiple_shipments(self):
        order = {'apple': 10, 'banana': 5, 'orange': 5}
        warehouse_inventory = [
            {'name': 'owd', 'inventory': {'apple': 5, 'orange': 5}},
            {'name': 'dm', 'inventory': {'apple': 5, 'banana': 5}}]
        output = [
            {'owd': {'apple': 5, 'orange': 5}},
            {'dm': {'apple': 5, 'banana': 5}}
        ]
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)

    """ Tests to ensure order is fulfilled even with overstock """

    def test_warehouse_overstock(self):
        order = {'apple': 5, 'banana': 5, 'orange': 5}
        warehouse_inventory = [
            {'name': 'owd', 'inventory': {'apple': 10, 'banana': 10, 'orange': 10}}]
        output = [
            {'owd': {'apple': 5, 'banana': 5, 'orange': 5}},
        ]
        res = InventoryAllocator(order, warehouse_inventory)
        self.assertEqual(res.best_shipment(), output)


if __name__ == '__main__':
    unittest.main()
