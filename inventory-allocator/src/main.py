"""
Author: Carl Zhou
Inventory Allocator Recruiting Exercise for Deliverr
Process input of order and outputs shipment
"""
# encoding: utf-8
from inventory_allocator import process_input
import sys
import json


def main():
    input_string = sys.stdin.readline().strip()  # read input string from STD IN
    try:
        result = process_input(input_string)  # process input string
        print(result)  # print results to STDOUT
    except json.decoder.JSONDecodeError:  # failure in parsing json
        print("Error: Invalid Json: " + input_string)
        sys.exit(-1)  # Error exit code
    sys.exit(0)  # Success exit code


if __name__ == '__main__':
    main()
