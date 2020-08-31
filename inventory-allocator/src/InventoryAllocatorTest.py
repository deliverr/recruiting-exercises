import unittest
from InventoryAllocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):

    def test_order_can_be_shipped_using_one_warehouse(self):
        self.solution = [{'owd': {'apple': 3}}]
        self.result = InventoryAllocator.cheapestShipment(InventoryAllocator, {'apple': 3}, [{'name':'owd', 'inventory':{'apple': 5}}])
        self.assertEqual(self.result, self.solution)

    def test_order_can_be_shipped_using_multiple_warehouses(self):
        self.solution = [{ 'owd': { 'apple': 5 }}, { 'dm': { 'apple': 5 } }]
        self.result = InventoryAllocator.cheapestShipment(InventoryAllocator, {'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}])
        self.assertEqual(self.result, self.solution)

    def test_order_cannot_be_shipped_because_there_is_not_enough_inventory_1(self):
        self.solution = []
        self.result = InventoryAllocator.cheapestShipment(InventoryAllocator, { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 }}] )
        self.assertEqual(self.result, self.solution)

    def test_order_cannot_be_shipped_because_there_is_not_enough_inventory_2(self):
        self.solution = []
        self.result = InventoryAllocator.cheapestShipment(InventoryAllocator, { 'apple': 2 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 }}] )
        self.assertEqual(self.result, self.solution)

    



if __name__ == "__main__":
    unittest.main()
