import copy


class InventoryAllocator():
    def __init__(self, order, inventory):
        self.inventory = inventory
        self.order = order

    def shipment(self):
        if not self.inventory or not self.order:
            # return empty list if no order placed or we have no inventory details
            return []
        else:
            # create deepcopy of the order and the inventory data
            order_tracking = copy.deepcopy(self.order)
            warehouses = copy.deepcopy(self.inventory)

            # initialize list to hold shipment details
            ship = []

            # iterate through every warehouse
            for warehouse in warehouses:

                # dictionary to hold items we can ship from said warehouse
                can_ship = {}

                # iterate through every item in the order
                for key in order_tracking.keys():

                    # check if we need to fulfil this item
                    if order_tracking[key] > 0:
                        # check if this item is present in said warehouse
                        if key in warehouse['inventory'].keys():
                            # check if said warehouse has more stock than the amount needed to fulfil this item
                            if warehouse['inventory'][key] > order_tracking[key]:
                                # make note of the details in can_ship
                                can_ship[key] = order_tracking[key]
                                # update said warehouse inventory by subtracting because we're taking this item
                                # out of said warehouse
                                warehouse['inventory'][key] = warehouse['inventory'][key] - order_tracking[key]
                                # because we've fulfilled this item, we now set the amount of this item needed to 0
                                order_tracking[key] = 0
                            else:
                                # said warehouse does not have necessary stock to fulfil this item
                                # we take whatever we can get from this warehouse
                                can_ship[key] = warehouse['inventory'][key]
                                # update number of items needed to fulfil order
                                order_tracking[key] = order_tracking[key] - warehouse['inventory'][key]
                                # because we took all items from said warehouse, this warehouse no longer has this item
                                # in stock. So set this number to 0 to reflect this change
                                warehouse['inventory'][key] = 0

                # add details to shipment details before moving on to next warehouse
                ship.append({warehouse['name']: can_ship})

            # check if every item in the order has been fulfilled. Even if one item has not been fulfilled,
            # we cannot proceed with this shipment (because customers don't want incomplete shipments).
            # Return empty list to indicate empty shipment
            for key in order_tracking.keys():
                if order_tracking[key] > 0:
                    return []

            # if all items in the order have been fulfilled, return shipment details.
            # also, update inventory details to indicate items were taken out of inventory for shipment.
            # (you can also reference the original order anytime with self.order)
            self.inventory = copy.deepcopy(warehouses)
            return ship


if __name__ == '__main__':
    inventory_allocator = InventoryAllocator({'apple': 5, 'banana': 5, 'orange': 5},
                                             [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
                            {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}])
    print("The shipment details are:")
    print(inventory_allocator.shipment())
    print("The updated inventory details after shipment are:")
    print(inventory_allocator.inventory)
