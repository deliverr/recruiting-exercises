from Main import Main

# Describes the order to be placed
order = {"apple": 5}
print("Order Received: {}".format(order))

# Describes the available warehouses
warehouses =  [
        { "name": "owd", "inventory": { "apple": 6} }, 
]

# Initializes the driver class for the inventory allocator
print("Order placed...")
main = Main(order, warehouses)

# Prepares the shipment
print("Preparing the shipment...")
shipment = main.find_cheapest_shipment()

# Prints the shipment
print("Shipment: {}".format(shipment))