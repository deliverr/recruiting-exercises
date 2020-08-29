'''
Created on Aug 25, 2020

@author: beatr
'''
import unittest
import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    
    def setUp(self):
        self.inventory_allocator = InventoryAllocator.InventoryAllocator()
        
    def test_exactMatch(self):
        # Example given
        order = {"apple": 1}
        warehouse_inventory = [ {"owd" : {"apple" : 1}} ]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"owd" : {"apple" : 1}}]
        
        self.assertCountEqual(result, expected)
    
    def test_emptyInventory(self):
        # Example given
        order = {"apple": 1}
        warehouse_inventory = [ {"owd": {"apple" : 0}} ]
    
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = []
        
        self.assertCountEqual(result, expected) 
    
    def test_splitItem(self):
        # Example given
        order = {"apple" : 10}
        warehouse_inventory = [ {"owd" : {"apple" : 5}},
                             {"dm" : { "apple" : 5}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"dm" : {"apple" : 5}}, {"owd" : {"apple" : 5}}]
        
        self.assertCountEqual(result, expected)
    
    def test_emptyOrder(self):
        # Test for empty order
        order = {}
        warehouse_inventory = [{"abc" : {"apple" : 5}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = []
        
        self.assertCountEqual(result, expected)
    
    def test_emptyOrderEmptyInventory(self):
        # Test for empty order and empty inventory
        order = {}
        warehouse_inventory = [{"abc" : {"apple" : 0, "banana" : 0}},
                               {"xyz" : {"apple" : 0, "cantaloupe" : 0}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = []
        
        self.assertCountEqual(result, expected)
           
    def test_threeItemsOneWarehouseSufficient(self):
        # Test for 3 items ordered, fulfilled by one warehouse with more than enough inventory
        order = {"apple" : 2, "banana" : 5, "cantaloupe" : 4}
        warehouse_inventory = [{"abc" : {"apple" : 8, "banana" : 7, "cantaloupe" : 12}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 2, "banana" : 5, "cantaloupe" : 4}}]
        
        self.assertCountEqual(result, expected)
    
    def test_threeItemsTwoWarehouseSufficient(self):
        #Test for 3 items ordered, fulfilled by two warehouses with enough inventory
        order = {"apple" : 7, "banana" : 3, "cantaloupe" : 5}
        warehouse_inventory = [{"abc" : {"apple" : 7, "banana" : 0, "cantaloupe" : 5}},
                               {"xyz" : {"banana" : 3}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 7, "cantaloupe" : 5}},
                    {"xyz" : {"banana" : 3}}]
        
        self.assertCountEqual(result, expected)
        
    def test_threeItemsTwoWarehouseSufficient2(self):
        # Test for 3 items ordered, fulfilled by two warehouses with more enough inventory
        # Different from test_threeItemsTwoWarehouseSufficient because checking for more than enough inventory
        order = {"apple" : 7, "banana" : 3, "cantaloupe" : 5}
        warehouse_inventory = [{"abc" : {"apple" : 8, "banana" : 0, "cantaloupe" : 6}},
                               {"xyz" : {"banana" : 5}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 7, "cantaloupe" : 5}},
                    {"xyz" : {"banana" : 3}}]
        
        self.assertCountEqual(result, expected)
    
    def test_threeItemsTwoWarehouseSufficient3(self):
        # Test for 3 items ordered, fulfilled by two warehouses with more than enough inventory
        # Differs from test_threeItemsTwoWarehouseSufficient and test_threeItemsTwoWarehouseSufficient2 because checking for cheapest order
        order = {"apple" : 6, "banana" : 3}
        warehouse_inventory = [{"abc" : {"apple" : 12, "banana" : 3}},
                               {"xyz" : {"apple" : 6, "banana" : 2}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 6, "banana" : 3}}]
        
        self.assertCountEqual(result, expected)
        
    def test_threeItemsTwoWarehouseSufficientSplitItem(self):
        # Test for 3 items ordered, fulfilled by two warehouses with split item
        order = {"apple" : 7, "banana" : 3, "cantaloupe" : 5}
        warehouse_inventory = [{"abc" : {"apple" : 4, "banana" : 0, "cantaloupe" : 5}},
                               {"xyz" : {"apple" : 5, "banana" : 5}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 4, "cantaloupe" : 5}},
                    {"xyz" : {"apple" : 3, "banana" : 3}}]
        
        self.assertCountEqual(result, expected)
    
    def test_threeItemsOneWarehouseInsufficient(self):
        # Test for 3 items ordered, unable to be fulfill whole order with one warehouse
        order = {"pencil" : 2, "apple" : 2, "honey" : 4}
        warehouse_inventory = [{"abc" : {"pencil" : 0, "apple" : 3, "honey" : 5}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 2, "honey" : 4}}]
        
        self.assertCountEqual(result, expected)
    
    def test_threeItemsOneWareHouseInsufficient2(self):
        # Test for 3 items ordered, unable to fulfill order with one warehouse
        # Different from test_threeItemsOneWarehouseInsufficient because returns empty shipment
        order = {"pencil" : 2, "apple" : 3, "cantaloupe" : 8}
        warehouse_inventory = [{"abc" : {"pencil" : 1, "banana" : 3, "apple" : 0, "cantaloupe" : 4}}]
        
        result = self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = []
        
        self.assertCountEqual(result, expected)
        
    def test_threeItemsTwoWarehouseInsufficient(self):
        # Test for 3 items ordered, unable to fulfill whole order with two warehouses
        order = {"pencil" : 2, "apple" : 2, "honey" : 4}
        warehouse_inventory = [{"abc" : {"pencil" : 0, "apple" : 3, "honey" : 1}}, 
                               {"xyz" : {"pencil" : 3, "apple" : 1, "honey" : 2}}]
        
        result =  self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = [{"abc" : {"apple" : 2}},
                    {"xyz" : {"pencil" : 2}}]
        
        self.assertCountEqual(result, expected)  
        
    def test_threeItemsTwoWarehouseInsufficient2(self):
        # Test for 3 items ordered, unable to fulfill order with two warehouses
        # Different from test_threeItemsTwoWarehouseInsufficient because returns empty shipment
        order = {"pencil" : 2, "apple" : 2, "cantaloupe" : 3}
        warehouse_inventory = [{"abc" : {"pencil" : 0, "apple" : 1, "honey" : 1, "cantaloupe" : 0}}, 
                               {"xyz" : {"pencil" : 1, "apple" : 0, "honey" : 2, "cantaloupe" : 1}}]
        
        result =  self.inventory_allocator.cheapest_shipment(order, warehouse_inventory)
        expected = []
        
        self.assertCountEqual(result, expected)
        
    
        
if __name__ == "__main__":
    unittest.main()