from typing import List, Dict

OrderType = Dict
WarehousesType = List[Dict]
ShipmentType = List[Dict]


def allocate_inventory(order: OrderType, warehouses: WarehousesType) -> ShipmentType:
    """
    Function to optimize the allocation of inventory into different warehouses
    :param order: An order to optimize
    :param warehouses: Warehouses to allocate inventory into
    :return: Optimized allocated inventory
    """
    amount_needed = 0
    in_inventory = 0
    list_of_warehouses = []
    # go through the order and get the first value
    for value in order.values():
        # add it to a variable
        amount_needed = value
        # go through the list of warehouses and get the first inventory
        for index in range(len(warehouses)):
            for key in warehouses[index]:
                for amount in warehouses[index][key].values():
                    # if the amount in the inventory is greater than equal to amount for the first item in the order
                    if amount >= amount_needed:
                        # add it to list of warehouses needed to complete the order
                        list_of_warehouses.append(warehouses[index])
                        return list_of_warehouses
                    else:
                        continue


    # go through the inventory and get the first value
    # check if the first value of the order >= first value of inventory
    # if true, add warehouse to a list
    # if false, go to the next warehouse
    pass

# allocate_inventory({}, []) # tipos correctos

# allocate_inventory(1, "lol")  # tipos incorrectos


print(allocate_inventory({"apple": 5, "banana": 5, "orange": 5},
                   [ { "owd": { "apple": 5, "orange": 10 } }, { "dm": { "banana": 5, "orange": 10 } } ]))

print(allocate_inventory({ "apple": 10 }, [{"owd": { "apple": 5 } }, { "dm": { "apple": 5 }}]))
