import unittest
from inventory_allocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase): 
    
    def test_one_item_fully_shipped_from_one_warehouse_with_less_than_or_equal_items_in_inventory_passed(self):
        self.expected = [{'owd': {'apple': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3}, {'owd': {'apple': 5}})
        self.assertEqual(self.result, self.expected)
    
    def test_two_items_fully_shipped_from_one_warehouse_with_less_than_or_equal_number_of_items_passed(self):
        self.expected = [{'owd': {'apple': 3, 'orange': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {'apple': 5, 'orange': 5}})
        self.assertEqual(self.expected, self.result)
    
    def test_three_items_fully_shipped_from_one_warehouse_with_less_than_or_equal_number_of_items_passed(self):
        self.expected = [{'owd': {'apple': 3, 'orange': 3, 'banana':1}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3, 'banana':1}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_item_fully_shipped_with_option_of_two_warehouses_but_all_items_from_first_warehouse_only_passed(self):
        self.expected = [{'owd': {'apple': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_two_items_fully_shipped_with_option_of_two_warehouses_but_all_items_from_first_warehouse_only_passed(self):
        self.expected = [{'owd': {'apple': 3, 'orange': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.expected, self.result)
    
    def test_three_items_fully_shipped_with_option_of_two_warehouses_but_all_items_from_first_warehouse_only_passed(self):
        self.expected = [{'owd': {'apple': 3, 'orange': 3, 'banana':1}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3, 'banana':1}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.expected, self.result)
    
    def test_item_fully_shipped_with_option_of_two_warehouses_but_all_items_from_second_warehouse_only_passed(self):
        self.expected = [{'jak': {'apple': 6}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 6}, {'owd': {'apple': 0, 'orange': 3, 'banana': 1}, 'jak': {'apple': 9, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_two_items_fully_shipped_with_option_of_two_warehouses_but_all_items_from_second_warehouse_only_passed(self):
        self.expected = [{'jak': {'apple': 3, 'orange': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {'apple': 0, 'orange': 0, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.expected, self.result)
    
    def test_three_items_fully_shipped_with_option_of_two_warehouses_but_all_items_from_second_warehouse_only_passed(self):
        self.expected = [{'jak': {'apple': 3, 'orange': 3, 'banana':1}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3, 'banana':1}, {'owd': {'apple': 0, 'orange': 0, 'banana': 0}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.expected, self.result)
    
    def test_single_item_fully_shipped_with_option_of_two_warehouses_and_item_obtained_from_both_passed(self):
        self.expected = [{'owd': {'apple': 2}}, {'jak': {'apple': 6}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 8}, {'owd': {'apple': 2, 'orange': 3, 'banana': 1}, 'jak': {'apple': 9, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_single_item_fully_shipped_with_option_of_three_warehouses_and_items_obtained_from_all_passed(self):
        self.expected = [{'owd': {'apple': 5}}, {'jak': {'apple': 20}}, {'ek': {'apple': 25}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 50}, {'owd': {'apple': 5, 'orange': 1, 'banana': 1}, 'jak': {'apple': 20, 'orange': 3, 'banana':8}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)

    def test_two_items_fully_shipped_with_option_of_two_warehouses_and_items_obtained_from_both_passed(self):
        self.expected = [{'owd': {'orange': 2}}, {'jak': {'apple': 6}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 6, 'orange': 2}, {'owd': {'apple': 0, 'orange': 3, 'banana': 1}, 'jak': {'apple': 9, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_three_items_fully_shipped_with_option_of_two_warehouses_and_items_obtained_from_both_passed(self):
        self.expected = [{'owd': {'orange': 2, 'banana': 1}}, {'jak': {'apple': 6}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 6, 'orange': 2, 'banana': 1}, {'owd': {'apple': 0, 'orange': 3, 'banana': 1}, 'jak': {'apple': 9, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_items_fully_shipped_with_option_of_three_warehouses_and_items_obtained_from_all_passed(self):
        self.expected = [{'owd': {'apple': 5, 'orange': 1, 'banana': 1}}, {'jak': {'apple': 3, 'orange': 2, 'banana': 8}}, {'ek': {'apple': 12, 'banana': 1}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 20, 'orange': 3, 'banana':10}, {'owd': {'apple': 5, 'orange': 1, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':8}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)
    
    def test_items_fully_shipped_with_option_of_three_warehouses_and_items_obtained_from_first_and_second_passed(self):
        self.expected = [{'owd': {'apple': 15, 'orange': 1, 'banana': 3}}, {'jak': {'apple': 5, 'orange': 2, 'banana': 7}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 20, 'orange': 3, 'banana':10}, {'owd': {'apple': 15, 'orange': 1, 'banana': 3}, 'jak': {'apple': 7, 'orange': 3, 'banana':8}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)
    
    def test_items_fully_shipped_with_option_of_three_warehouses_and_items_obtained_from_first_and_last_passed(self):
        self.expected = [{'owd': {'apple': 15, 'orange': 1, 'banana': 3}}, {'ek': {'apple': 5, 'orange': 2, 'banana': 7}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 20, 'orange': 3, 'banana':10}, {'owd': {'apple': 15, 'orange': 1, 'banana': 3}, 'jak': {'apple': 0, 'orange': 0, 'banana':0}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)
    
    def test_items_fully_shipped_with_option_of_three_warehouses_and_items_obtained_from_second_and_last_passed(self):
        self.expected = [{'jak': {'apple': 10, 'orange': 1, 'banana': 4}}, {'ek': {'apple': 10, 'orange': 2, 'banana': 6}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 20, 'orange': 3, 'banana':10}, {'owd': {'apple': 0, 'orange': 0, 'banana': 0}, 'jak': {'apple': 10, 'orange': 1, 'banana':4}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)

    def test_items_fully_shipped_with_one_item_from_each_warehouse_passed(self):
        self.expected = [{'owd': {'apple': 20}}, {'jak': {'banana': 10}}, {'ek': {'orange': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 20, 'orange': 3, 'banana':10}, {'owd': {'apple': 20, 'orange': 0, 'banana': 0}, 'jak': {'apple': 10, 'orange': 0, 'banana':30}, 'ek': {'apple': 30, 'orange': 15, 'banana': 25}})
        self.assertEqual(self.expected, self.result)

    def test_one_item_partially_filled_order_from_one_warehouse_with_item_requested_greater_than_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 5}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_two_items_partially_filled_order_from_one_warehouse_with_item_requested_greater_than_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 6}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_three_items_partially_filled_order_from_one_warehouse_with_item_requested_greater_than_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3, 'banana': 2}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_not_enough_inventory_for_item_with_option_of_two_warehouses_but_item_requested_greater_than_combined_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 30}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_one_item_fully_shipped_but_second_item_requested_greater_than_combined_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 5, 'orange': 30}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}})
        self.assertEqual(self.result, self.expected)
    
    def test_not_enough_inventory_for_item_with_option_of_three_warehouses_because_item_requested_greater_than_combined_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 15, 'orange': 30}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}, 'ek': {'apple': 3, 'banana': 7, 'orange': 3}})
        self.assertEqual(self.result, self.expected)
    
    def test_not_enough_inventory_for_item_with_option_of_three_warehouses_and_one_warehouse_empty(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 15, 'orange': 30}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}, 'ek': {'apple': 3, 'banana': 7, 'orange': 3}})
        self.assertEqual(self.result, self.expected)

    def test_result_on_empty_warehouse_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {}})
        self.assertEqual(self.expected, self.result)

    def test_result_on_two_empty_warehouses_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {}, 'jak': {}})
        self.assertEqual(self.expected, self.result)
    
    def test_requested_item_without_match_in_single_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 5}, {'owd': {'orange': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_requested_items_without_match_in_single_warehouse_inventory_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 6}, {'owd': {'pear': 3, 'grape': 5, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_single_warehouse_with_a_zero_quantity_item_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {'apple': 0, 'orange': 3}})
        self.assertEqual(self.expected, self.result)
    
    def test_warehouses_with_a_missing_item_in_stock_passed(self):
        self.expected = []
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3, 'orange': 3}, {'owd': {'apple': 0, 'orange': 3}})
        self.assertEqual(self.expected, self.result)
    
    def test_zero_quantity_of_item_requested_from_one_warehouse_passed(self):
        self.expected = [{'owd': {'orange': 3}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 0, 'orange': 3}, {'owd': {'apple': 10, 'orange': 3}})
        self.assertEqual(self.expected, self.result)
    
    def test_zero_quantity_of_item_requested_from_two_warehouses_passed(self):
        self.expected = [{'owd': {'orange': 3, 'banana': 1}}]
        self.result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 0, 'orange': 3, 'banana': 1}, {'owd': {'apple': 2, 'orange': 3, 'banana': 4}, 'jak': {'apple': 10, 'orange': 4, 'banana': 1}})
        self.assertEqual(self.expected, self.result)
    
    def test_string_quantity_in_request_raises_error_passed(self):
        self.assertRaises((NameError, TypeError), InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': '4dsd', 'orange': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}}))

    def test_float_quantity_in_request_raises_error_passed(self):
        self.assertRaises((NameError, TypeError), InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 2.343, 'orange': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}}))
    
    def test_string_quantity_in_warehouse_inventory_raises_error_passed(self):
        self.assertRaises((NameError, TypeError), InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 4, 'orange': 3}, {'owd': {'apple': 'x', 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}}))

    def test_float_quantity_in_warehouse_inventory_raises_error_passed(self):
        self.assertRaises((NameError, TypeError), InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 5, 'orange': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 2.343}}))
   
if __name__ == "__main__":
    unittest.main()