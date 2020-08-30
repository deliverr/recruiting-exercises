import unittest
from Deliverr_InventoryAllocator import Deliverr_InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    def setUp(self):
        self.allocator = Deliverr_InventoryAllocator()

    def test01_empty_order_empty_inventoryDict(self):
        self.assertEqual(self.allocator.get_cheapest_shipment({}, []), [])

    def test02_empty_order(self):
        order = {}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 5}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test03_zero_order(self):
        inventoryDict = [{"name": "store1", "inventory": {"apple": 5}}]
        order = {"apple": 0}
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test04_empty_inventoryDict(self):
        order = {"apple": 1}
        inventoryDict = []
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test05_zero_inventoryDict(self):
        order = {"apple": 1}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 0}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test06_negative_inventoryDict(self):
        order = {"apple": 1}
        inventoryDict = [{"name": "store1", "inventory": {"apple": -1}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test07_Item_Names_capital_Inventory(self):
        order = {"apple": 2, "orange": 1}
        inventoryDict = [{"name": "owd", "inventory": {"Apple": 2, "Orange": 1}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(
            order, inventoryDict), [{'owd': {'orange': 1, 'apple': 2}}])

    def test08_Items_Names_Capital_Order(self):
        order = {"Apple": 2, "Orange": 1}
        inventoryDict = [{"name": "owd", "inventory": {"apple": 2, "orange": 1}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(
            order, inventoryDict), [{'owd': {'orange': 1, 'apple': 2}}])

    def test09_less_inventory(self):
        order = {"apple": 2}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 1}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test10_missing_item_inventory(self):
        order = {"apple": 3}
        inventoryDict = [{"name": "store1", "inventory": {"grape": 2}},
                         {"name": "store2", "inventory": {"orange": 2}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [])

    def test11_some_items_less_inventory(self):
        order = {"apple": 3, "orange": 2}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 1, "orange": 1}},
                   {"name": "store2", "inventory": {"apple": 1, "orange": 1}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [{'store1': {'orange': 1}}, {'store2': {'orange': 1}}])

    def test12_items_multiple_inventory(self):
        order = {"apple": 5, "orange": 5}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 1, "orange": 5}},
                   {"name": "store2", "inventory": {"apple": 2, "orange": 2}},
                         {"name": "store3", "inventory": {"apple": 2, "orange": 5}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [{'store1': {'orange': 5, 'apple': 1}}, {'store2': {'apple': 2}}, {'store3': {'apple': 2}}])


    def test13_Exact_Match(self):
        order = {"apple": 5, "orange": 5}
        inventoryDict = [{"name": "store1", "inventory": {"apple": 5, "orange": 5}}]
        self.assertEqual(self.allocator.get_cheapest_shipment(order, inventoryDict), [{'store1': {'orange': 5, 'apple': 5}}])

if __name__ == '__main__':
    unittest.main()