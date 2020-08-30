from Deliverr_InventoryAllocator import Deliverr_InventoryAllocator

order = eval(input("Order : "))
inv = eval(input("Inventory : "))

if __name__ == "__main__":
    inventoryAllocator = Deliverr_InventoryAllocator()
    print("Solution: ")
    print(inventoryAllocator.get_cheapest_shipment(order, inv))