from collections import OrderedDict

class Deliverr_InventoryAllocator:

    def __init__(self):
        self.inventory = OrderedDict(OrderedDict())

    # ** Transforms the existing data structure to a different structure which will
    # speed up the querying operation. As this trnaformation is a one time operation.
    # ** Also supports to update the inventory.
    # ** Assumption: the number of calls to update inventory way higher then calls to
    # shipment allocation
    def update_transform_inventory(self, inventory_dict):
        for inventory in inventory_dict:
            inventory_name = inventory["name"].lower()
            items_in_inventory = inventory["inventory"]
            for each_item in items_in_inventory:
                self.item_inventory_size[each_item.lower()] = \
                    self.item_inventory_size.get(each_item.lower(), 0) + items_in_inventory[each_item]
                if each_item not in self.inventory:
                    self.inventory[each_item.lower()] = OrderedDict()
                self.inventory[each_item.lower()][inventory_name] = items_in_inventory[each_item]
        return self.inventory