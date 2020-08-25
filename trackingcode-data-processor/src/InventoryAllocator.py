import copy

class InventoryAllocator():
    def __init__(self, order, inventory):
        self.inventory = inventory
        self.order = order

    def shipment(self):
        # returns empty list if not given an order or inventory
        if not self.inventory or not self.order:
            return []
        else:
            # create deepcopy of order and inventory data
            orders = copy.deepcopy(self.order)
            warehouses = copy.deepcopy(self.inventory)

            # initialize answer list 
            ans = []

            # iterate through every warehouse
            for warehouse in warehouses:

                # dictionary to hold items we can ship from said warehouse
                can_ship = {}

                # iterate through every item in the order
                for item in orders.keys():

                    # check if there as an order placed for specific item
                    if orders[item] > 0:
                        # check if item can be found at warehouse
                        if item in warehouse['inventory'].keys():
                            # check if there is sufficient stock at warehouse for item order
                            if warehouse['inventory'][item] > orders[item]:
                                # add item into dictionary
                                can_ship[item] = orders[item]
                                # remove item from warehouse inventory because will be shipping/using it
                                warehouse['inventory'][item] = warehouse['inventory'][item] - orders[item]
                                # set order amount to 0 since order is finished
                                orders[item] = 0
                            else:
                                # warehouse doesn't have enough stock
                                can_ship[item] = warehouse['inventory'][item]
                                # update number of items to be total needed minus max what we can take from current warehouse
                                orders[item] = orders[item] - warehouse['inventory'][item]
                                # update current warehouse stock to 0
                                warehouse['inventory'][item] = 0

                # add shipment warehouse and number of stock taken to answer list
                ans.append({warehouse['name']: can_ship})

            # check if all orders are completed
            for item in orders.keys():
                # Return empty list to indicate empty shipment
                if orders[item] > 0:
                    return []

            # update inventory, removing items in the shipment
            self.inventory = copy.deepcopy(warehouses)
            return ans


if __name__ == '__main__':
    allocate = InventoryAllocator({'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 10}}])
    print "Shipment: ",allocate.shipment()
    print "Warehouse inventory after shipment: ", allocate.inventory
