import re
from Models import warehouse
import json
# encoding: utf-8
'''
Input: string in format defined in README.md
Returns: tuple of json string of items requested, json string of array of warehouse and quantity of items
'''


def convert_to_json_string(input_string):
    json_string = re.sub(r'([{,])(\s)([\w\d])', r'\1\2"\3', input_string, re.UNICODE)  # pass 1 - { a
    json_string = re.sub(r'([\w\d])(:)([\s])', r'\1"\2\3', json_string, re.UNICODE)  # pass 2 - e: 1
    json_string = re.sub(r'(name\"?:)(\s)([\w])', r'\1\2"\3', json_string, re.UNICODE)  # pass 3 - name: o
    # pass 4: d, inventory:
    json_string = re.sub(r'([\w\d])(,\s)(\"?inventory)', r'\1"\2\3', json_string, re.UNICODE)
    formatted_str_arr = json_string.split(", [")  # split orders from inventory
    return formatted_str_arr[0], "[" + formatted_str_arr[1]


'''
# Use the approach described here: https://en.wikipedia.org/wiki/Greedy_algorithm
Input: asking_items: dict, warehouses: list of WareHouse object
Returns: list of [warehouse name, item count]
'''


def find_combo(asking_items, warehouses):
    results = []
    # base case
    asking_items_length = len(asking_items)
    if asking_items_length == 0:  # blank order - do nothing
        return results

    # determine which items can be shipped
    shippable_items = {}
    for item_name in asking_items:
        total_inventory = sum(
            map(lambda y: y.inventory[item_name], list(filter(lambda x: item_name in x.inventory, warehouses))))
        if total_inventory >= asking_items[item_name]:
            shippable_items[item_name] = asking_items[item_name]

    if not shippable_items:  # order cannot be fulfilled at all
        return results

    # go through each warehouse and item and determine allocation
    for wh in warehouses:
        warehouse_shipment = warehouse.Warehouse.new()
        for name in shippable_items:
            asking_quantity = asking_items[name]
            if name in wh.inventory:
                if 0 < asking_items[name] <= wh.inventory[name]:  # enough inventory in one warehouse
                    warehouse_shipment.name = wh.name
                    warehouse_shipment.inventory[name] = asking_quantity
                    asking_items[name] -= asking_quantity
                elif asking_quantity > wh.inventory[name] > 0:  # not enough inventory in one warehouse
                    warehouse_shipment.name = wh.name
                    warehouse_shipment.inventory[name] = wh.inventory[name]
                    asking_items[name] -= wh.inventory[name]
                    wh.inventory[name] = 0
        if warehouse_shipment.inventory:  # don't add unused warehouses
            results.append(warehouse_shipment)
    return results


'''
End to End function for processing input string
input: json_string
returns: output_string described in readme.md
'''


def process_input(input_string):
    order_json_string, warehouse_json_string = convert_to_json_string(input_string)
    order_list = json.loads(order_json_string)
    warehouse_json = json.loads(warehouse_json_string)

    # convert warehouse_json to list of WareHouse objects
    warehouses = [warehouse.Warehouse(x) for x in warehouse_json]

    shipments = find_combo(order_list, warehouses)

    # return the output string to print
    result = '['
    shipments_num = len(shipments)
    for i in range(0, shipments_num):
        result += str(shipments[i])
        if i < shipments_num - 1:  # don't add extra comma at the end
            result += ', '
    result += ']'
    return result
