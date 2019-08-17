from inventory_allocator import convert_to_json_string, find_combo
from Models import warehouse
import sys
import json

'''
Author: Carl Zhou
Process input of order and outputs shipment
'''


def main():
    input = sys.stdin.readline().strip()
    order_json_string, warehouse_json_string = convert_to_json_string(input)
    order_list = json.loads(order_json_string)
    warehouse_json = json.loads(warehouse_json_string)

    # convert warehouse_json to list of WareHouse objects
    warehouses = [warehouse.Warehouse(x) for x in warehouse_json]

    shipments = find_combo(order_list, warehouses)

    # print output
    print('[', end='')
    shipments_num = len(shipments)
    for i in range(0, shipments_num):
        print(shipments[i], end='')
        if i < shipments_num-1:
            print(', ', end='')
    print(']')
    sys.exit(0)


if __name__ == '__main__':
    main()