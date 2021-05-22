import unittest
from InventoryAllocator import InventoryAllocator

##########################################
#        INSTRUCTIONS FOR TESTING        #
##########################################
#										 #
# run the following code:				 #
#										 #
# $ python InventoryAllocatorTest.py     #
#										 #
##########################################


class InventoryAllocatorTest(unittest.TestCase):

    def test_happy_case(self):
    	print("\nStarting Test: test_happy_case")
    	IA = InventoryAllocator()
    	order = { 'apple': 5}
    	store_1 = {'name':'owd', 'inventory': { 'apple': 5}}
    	inventory_dist = [store_1]
    	expected = [{'owd': {'apple': 5}}]
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_not_enough_inventory(self):
    	print("\nStarting Test: test_not_enough_inventory")
    	IA = InventoryAllocator()
    	order = { 'apple': 5}
    	store_1 = {'name':'owd', 'inventory': { 'apple': 2 }}
    	inventory_dist = [store_1]
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_should_split(self):
    	print("\nStarting Test: test_should_split")
    	IA = InventoryAllocator()
    	order = { 'apple': 5, 'banana': 10}
    	store_1 = {'name':'owd', 'inventory': { 'apple': 2 , 'banana': 1}}
    	store_2 = {'name':'dsw', 'inventory': { 'apple': 3 , 'banana': 12}}
    	inventory_dist = [store_1, store_2]
    	expected = [{'owd': {'apple': 2, 'banana': 1}}, {'dsw': {'apple':3, 'banana': 9}}]
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_not_at_any_stores(self):
    	print("\nStarting Test: test_not_at_any_stores")
    	IA = InventoryAllocator()
    	order = { 'apple': 5, 'banana': 10}
    	store_1 = {'name':'owd', 'inventory': { 'pickles': 2 , 'grapes': 1}}
    	store_2 = {'name':'dsw', 'inventory': { 'chips': 3 , 'juice': 12}}
    	inventory_dist = [store_1, store_2]
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_zero_inventory_stores(self):
    	print("\nStarting Test: test_zero_inventory_stores")
    	IA = InventoryAllocator()
    	order = { 'apple': 5, 'banana': 10}
    	store_1 = {'name':'owd', 'inventory': { 'apple': 0 , 'banana': 0}}
    	store_2 = {'name':'dsw', 'inventory': { 'chips': 0 , 'banana': 0}}
    	inventory_dist = [store_1, store_2]
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_no_stores(self):
    	print("\nStarting Test: test_no_stores")
    	IA = InventoryAllocator()
    	order = { 'apple': 5, 'banana': 10}
    	inventory_dist = []
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_no_order(self):
    	print("\nStarting Test: test_no_order")
    	IA = InventoryAllocator()
    	order = {}
    	store_1 = {'name':'owd', 'inventory': { 'apple': 0 , 'banana': 0}}
    	store_2 = {'name':'dsw', 'inventory': { 'chips': 0 , 'banana': 0}}
    	inventory_dist = [store_1, store_2]
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")

    def test_no_order_no_stores(self):
    	print("\nStarting Test: test_no_order_no_stores")
    	IA = InventoryAllocator()
    	order = {}
    	inventory_dist = []
    	expected = []
    	self.assertEqual(IA.solution(order, inventory_dist), expected)
    	print("PASSED!")


if __name__ == '__main__':
	print('\n'+'='*40)
	print('= Running Tests for InventoryAllocator =')
	print('='*40,'\n')
	unittest.main()