from DeliverrChallenge import InventoryAllocator

def getCheapest(orders, warehouseDetails):
    print("Orders and WarehouseDetails are as follows: ", orders, warehouseDetails)
    inventory = InventoryAllocator()
    print("Result is: ",inventory.cheapestShipment(orders, warehouseDetails))
    print("#####################################################################")

if __name__ == '__main__':

    # Test Case 1
    print("Test Case 1")
    orders = {"apple": 6, "orange": 10}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getCheapest(orders, warehouses)

    # Test Case 2
    print("Test Case 2")
    orders = {"apple": 5, "orange": 10}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getCheapest(orders, warehouses)

    # Test Case 3
    print("Test Case 3")
    orders = {"apple": 6, "orange": 10, "pineapple": 4}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getCheapest(orders, warehouses)

    # Test Case 4
    print("Test Case 4")
    orders = {}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getCheapest(orders, warehouses)

    # Test Case 5
    print("Test Case 5")
    orders = {"apple": 6, "orange": 10, "pineapple": 4}
    warehouses = []
    getCheapest(orders, warehouses)

    # Test Case 6
    print("Test Case 6")
    orders = {"apple": 6, "orange": 10, "pineapple": 4}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "mk", "inventory": {"pineapple": 5, "banana": 10}}]
    getCheapest(orders, warehouses)

    # Test Case 7
    print("Test Case 7")
    orders = { "apple": 1 }
    warehouses = [{ "name": "owd", "inventory": { "apple": 1 } }]
    getCheapest(orders, warehouses)

    # Test Case 8
    print("Test Case 8")
    orders = {"apple": 1}
    warehouses = [{"name": "owd", "inventory": {"apple": 0}}]
    getCheapest(orders, warehouses)