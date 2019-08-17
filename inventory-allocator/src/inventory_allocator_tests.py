import unittest
from inventory_allocator import convert_to_json_string, find_combo, process_input
from Models import Warehouse
import json


# encoding: utf-8
# json parsing tests


class TestConvertJsonString(unittest.TestCase):

    def test_1_item_1_warehouse(self):
        input_string = "{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]"
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{ "apple": 1 }'
        expected_inventory = '[{ "name": "owd", "inventory": { "apple": 1 } }]'
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)

    def test_no_warehouse(self):
        input_string = "{ apple: 1 }, []"
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{ "apple": 1 }'
        expected_inventory = '[]'
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)

    def test_no_order(self):
        input_string = "{}, [{ name: owd, inventory: { apple: 1 } }]"
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{}'
        expected_inventory = '[{ "name": "owd", "inventory": { "apple": 1 } }]'
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)

    def test_multiple_order_multiple_warehouses(self):
        input_string = "{ apple: 5, banana: 5, orange: 5 }, [{ name: owd, inventory: { apple: 5, banana: 5 } }, " \
                       "{ name: dm, inventory: { orange: 10 }}] "
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{ "apple": 5, "banana": 5, "orange": 5 }'
        expected_inventory = '[{ "name": "owd", "inventory": { "apple": 5, "banana": 5 } }, { "name": "dm", ' \
                             '"inventory": { "orange": 10 }}] '
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)

    def test_spaces_and_colon(self):
        input_string = "{ red apple: 5, banana: 5, florida orange: 5 }, [{ name: Carl's warehouse, inventory: { red " \
                       "apple: 5, banana: 5 } }, { name: dm, inventory: { florida orange: 10 }}] "
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{ "red apple": 5, "banana": 5, "florida orange": 5 }'
        expected_inventory = '[{ "name": "Carl\'s warehouse", "inventory": { "red apple": 5, "banana": 5 } }, ' \
                             '{ "name": "dm", "inventory": { "florida orange": 10 }}] '
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)

    def test_unicode(self):
        input_string = "{ 蘋果: 5, 바나나: 5, オレンジ: 5 }, [{ name: مستودع, inventory: { 蘋果: 5, 바나나: 5 } }, " \
                       "{ name: depósito, inventory: { orange: 10 }}] "
        actual_order, actual_inventory = convert_to_json_string(input_string)
        expected_order = '{ "蘋果": 5, "바나나": 5, "オレンジ": 5 }'
        expected_inventory = '[{ "name": "مستودع", "inventory": { "蘋果": 5, "바나나": 5 } }, { "name": "depósito", ' \
                             '"inventory": { "orange": 10 }}] '
        self.assertEqual(expected_order, actual_order)
        self.assertEqual(expected_inventory, actual_inventory)


class TestFindCombo(unittest.TestCase):

    def test_1_item_1_warehouse(self):
        order = {"apple": 1}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 1 } }'))
        warehouses = [warehouse1]
        actual = find_combo(order, warehouses)
        expected_owd = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 1 } }'))
        expected = [expected_owd]
        self.assertEqual(expected, actual)

    def test_0_item_1_warehouse(self):
        order = {}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 1 } }'))
        warehouses = [warehouse1]
        actual = find_combo(order, warehouses)
        expected = []
        self.assertEqual(expected, actual)

    def test_1_item_0_warehouse(self):
        order = {'apple': 1}
        warehouses = []
        actual = find_combo(order, warehouses)
        expected = []
        self.assertEqual(expected, actual)

    def test_order_of_0(self):
        order = {}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 1 } }'))
        warehouses = [warehouse1]
        actual = find_combo(order, warehouses)
        expected = []
        self.assertEqual(expected, actual)

    def test_1_item_multiple_warehouses_multiple_needed(self):
        order = {'apple': 10}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 4 } }'))
        warehouse2 = Warehouse(json.loads('{ "name": "dm", "inventory": { "apple": 7 } }'))
        warehouses = [warehouse1, warehouse2]
        actual = find_combo(order, warehouses)
        expected_owd = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 4 } }'))
        expected_dm = Warehouse(json.loads('{ "name": "dm", "inventory": { "apple": 6 } }'))
        expected = [expected_owd, expected_dm]
        self.assertEqual(expected, actual)

    def test_1_item_multiple_warehouses_1_needed(self):
        order = {'apple': 3}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 4 } }'))
        warehouse2 = Warehouse(json.loads('{ "name": "dm", "inventory": { "apple": 7 } }'))
        warehouses = [warehouse1, warehouse2]
        actual = find_combo(order, warehouses)
        expected_owd = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 3 } }'))
        expected = [expected_owd]
        self.assertEqual(expected, actual)

    def test_1_item_multiple_warehouses_1_needed_1_zero(self):
        order = {'apple': 3}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 0 } }'))
        warehouse2 = Warehouse(json.loads('{ "name": "dm", "inventory": { "apple": 7 } }'))
        warehouses = [warehouse1, warehouse2]
        actual = find_combo(order, warehouses)
        expected_dm = Warehouse(json.loads('{ "name": "dm", "inventory": { "apple": 3 } }'))
        expected = [expected_dm]
        self.assertEqual(expected, actual)

    def test_1_item_not_enough(self):
        order = {'apple': 1}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 0 } }'))
        warehouses = [warehouse1]
        actual = find_combo(order, warehouses)
        expected = []
        self.assertEqual(expected, actual)

    def test_multiple_item_multiple_warehouses(self):
        order = {'apple': 10, 'banana': 5, 'orange': 100}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 5, "orange": 50 } }'))
        warehouse2 = Warehouse(json.loads('{ "name": "dm", "inventory": { "banana": 5 } }'))
        warehouse3 = Warehouse(
            json.loads('{ "name": "afd", "inventory": { "apple": 5, "banana": 100, "orange": 50 } }'))
        warehouses = [warehouse1, warehouse2, warehouse3]
        actual = find_combo(order, warehouses)
        expected_owd = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 5, "orange": 50 } }'))
        expected_dm = Warehouse(json.loads('{ "name": "dm", "inventory": { "banana": 5 } }'))
        expected_afd = Warehouse(json.loads('{ "name": "afd", "inventory": { "apple": 5, "orange": 50 } }'))
        expected = [expected_owd, expected_dm, expected_afd]
        self.assertEqual(expected, actual)

    def test_partial_fulfillment(self):
        order = {'apple': 10, 'banana': 6, 'orange': 100}
        warehouse1 = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 5, "orange": 50 } }'))
        warehouse2 = Warehouse(json.loads('{ "name": "dm", "inventory": { "banana": 5 } }'))
        warehouse3 = Warehouse(
            json.loads('{ "name": "afd", "inventory": { "apple": 5, "orange": 50 } }'))
        warehouses = [warehouse1, warehouse2, warehouse3]
        actual = find_combo(order, warehouses)
        expected_owd = Warehouse(json.loads('{ "name": "owd", "inventory": { "apple": 5, "orange": 50 } }'))
        expected_afd = Warehouse(json.loads('{ "name": "afd", "inventory": { "apple": 5, "orange": 50 } }'))
        expected = [expected_owd, expected_afd]
        self.assertEqual(expected, actual)


class TestProcessInput(unittest.TestCase):

    def test_valid_input(self):
        input_string = '{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]'
        actual = process_input(input_string)
        expected = "[{owd: {apple: 5}}, {dm: {apple: 5}}]"
        self.assertEqual(expected, actual)

    def test_invalid_json_input(self):
        input_string = '{ apple: 10 }, [{ name: '
        with self.assertRaises(json.decoder.JSONDecodeError):
            process_input(input_string)


if __name__ == '__main__':
    unittest.main()
