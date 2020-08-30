import unittest
from InventoryAllocator import InventoryAllocator
 
class Test_InventoryAllocator(unittest.TestCase):
    
    def test_shipment(self):
        
        #when the order can be fulfilled by inventory -> choose the cheapest shipment
        inventory1 = InventoryAllocator({'apple':5},[{'name':'pann', 'inventory':{'apple':5, 'banana':10}},
        {'name':'owa', 'inventory':{'apple':5,'banana':10}}])
        
        self.assertEqual(inventory1.find_cheapest_shipment(),[{'pann': {'apple':5, 'banana':10}}])
        
        #when the order can be fulfilled by inventory -> choose the cheapest shipment by splitting into two shipments if 
        #the amount from order is not sastified yet
        inventory2 = InventoryAllocator({'apple':10},[{'name':'pann', 'inventory':{'apple':5}},
        {'name':'owa', 'inventory':{'apple':5}}])  
        
        self.assertEqual(inventory2.find_cheapest_shipment(), [{ 'pann': {'apple': 5},  'owa': { 'apple': 5}}])
        
        #order cannot be fulfilled as there is less quantity in inventory -> return [] as the result
        inventory3 = InventoryAllocator({'apple':5},[{'name':'pann', 'inventory':{'apple':0}},
        {'name':'owa', 'inventory':{'apple':3}}]) 
        
        self.assertEqual(inventory3.find_cheapest_shipment(), [])
        
        #order can be fulfilled -> one warehouse that has larger amount of quantity to satisfy the order but in susequent position of the list
        inventory4 = InventoryAllocator({'apple':5},[{'name':'pann', 'inventory':{'apple':0}},
        {'name':'owa', 'inventory':{'apple':10}}]) 
         
        self.assertEqual(inventory4.find_cheapest_shipment(), [{'owa': { 'apple': 10}}])
        
        #order cannot be fullfiled -> warehouse cannot complete the order -> return [] as the result
        inventory5 = InventoryAllocator({'apple':1},[{'name':'pann', 'inventory':{'apple':0}}]) 
        
        self.assertEqual(inventory5.find_cheapest_shipment(), [])
        
        #order can be fulfilled -> iterate through all the list of warehouse to find the minimum of shipments 
        inventory6 = InventoryAllocator({'apple':5, 'orange':6},[{'name':'pann', 'inventory':{'orange': 3, 'pineapple':7}},
        {'name':'owa', 'inventory':{'apple':2, 'orange': 10}}, {'name':'dwa', 'inventory':{'apple':20, 'orange': 1}}])                      
        
        self.assertEqual(inventory6.find_cheapest_shipment(), [{'owa':{'apple':2, 'orange': 10}, 'dwa':{'apple':20, 'orange': 1}}])
        
        #order cannot be fulfilled -> the amount of order is 0 -> the value is invalid -> return False as result
        inventory7 = InventoryAllocator({'apple':0},[{'name':'pann', 'inventory':{'apple':2}},
        {'name':'owa', 'inventory':{'apple':10}}]) 
       
        self.assertEqual(inventory7.find_cheapest_shipment(), False)
        




        