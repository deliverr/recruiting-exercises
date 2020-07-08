import unittest
from main import itemAllocation


class Test(unittest.TestCase):

    def test_happy_case(self):
        items = {'apple': 1}
        allocation = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_unhappy_case(self):
        items = {'apple': 1}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 0} }]
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)
    
    def test_late_allocation(self):
        items = {'apple': 1}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 0} }, { 'name': 'dm', 'inventory': {'apple': 0} }, { 'name': 'td', 'inventory': {'apple': 1} }]
        output = [{'td': {'apple': 1}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_exact_split(self):
        items = {'apple': 10}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 5}}, { 'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_unused_inventory(self):
        items = {'apple': 10}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 10}}, { 'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 10}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_three_items(self):
        items = {'apple': 15, 'banana': 5, 'orange': 5}
        allocation = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},{'name': 'dm', 'inventory': {'apple': 10, 'banana': 5, 'orange': 10}}]
        output = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'apple': 10, 'banana': 5}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_no_items(self):
        items = {}
        allocation = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_no_inventory(self):
        items = {'orange': 5}
        allocation = []
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_empty(self):
        items = {}
        allocation = []
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_uneven_split(self):
        items = {'apple': 10}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 6}}, { 'name': 'dm', 'inventory': {'apple': 4}}]
        output = [{'owd': {'apple': 6}}, {'dm': {'apple': 4}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)
    
    def test_no_allocation(self):
        items = {'apple': 10}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 0}}, { 'name': 'dm', 'inventory': {'apple': 0, 'orange': 20}}]
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_complicated_split_1(self):
        items= {'apple': 5, 'banana': 3, 'orange': 17}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 4, 'banana': 3, 'orange': 1}}, { 'name': 'dm', 'inventory': {'apple': 1, 'orange': 20}}]
        output = [{'owd': {'apple': 4, 'banana': 3, 'orange': 1}}, {'dm': {'apple': 1, 'orange': 16}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)
    
    def test_complicated_split_2(self):
        items= {'apple': 5, 'banana': 7, 'orange': 17}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 4, 'banana': 3, 'orange': 1}}, 
        { 'name': 'dm', 'inventory': {'apple': 1, 'orange': 5, 'banana': 5}}, 
        { 'name': 'td', 'inventory': {'apple': 1, 'orange': 20, 'pineapple' : 5}}]
        output = [{'owd': {'apple': 4, 'banana': 3, 'orange': 1}}, {'dm': {'apple': 1, 'orange': 5, 'banana': 4}}, {'td': {'orange': 11}}]
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)

    def test_negative_numbers(self):
        items = {'apple': -5}
        allocation = [{ 'name': 'owd', 'inventory': {'apple': 4, 'banana': 3, 'orange': 1}}]
        output = []
        self.assertEqual(itemAllocation.itemAllocator(items, allocation), output)
        
if __name__ == '__main__':
    unittest.main()