from collections import OrderedDict
import json

class Deliverr_InventoryAllocator:

    def __init__(self):
        self.inventory = OrderedDict(OrderedDict())
        self.item_inventory_size = {}

    def get_cheapest_shipment(self, orders, inventory):
        if len(orders) == 0 or len(inventory) == 0:
            return []
        self.update_transform_inventory(inventory)
        return self.shipment(orders)

    def shipment(self, orders):
        """
        :param order:
        :return:
        """
        allocation = self._shipment(orders)

        # print the final allocation
        formatted_allocation = self._format_allocation(allocation)
        return formatted_allocation

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


    def _shipment(self, orders):
        final_allocation = OrderedDict()
        orders = {k.lower(): v for k, v in orders.items()}
        for order_item in orders:
            self._allocate_order(order_item, orders[order_item], final_allocation)

        return final_allocation

    def _allocate_order(self, order_item, order_size, final_allocation):

        if order_item not in self.inventory or order_size <= 0 or order_size > self.item_inventory_size[order_item]:
            return

        for inventory in self.inventory[order_item]:
            if self.inventory[order_item][inventory] <= 0 or order_size <= 0:
                continue
            final_allocation[inventory] = final_allocation.get(inventory, OrderedDict())
            if order_size <= self.inventory[order_item][inventory]:
                final_allocation[inventory][order_item] = order_size
                self.inventory[order_item][inventory] -= order_size
                return
            else:
                order_size = order_size - self.inventory[order_item][inventory]
                final_allocation[inventory][order_item] = self.inventory[order_item][inventory]
                self.inventory[order_item][inventory] = 0


    def _format_allocation(self, allocation):
        formatted_allocation = []
        for order in allocation:
            formatted_allocation.append({order: dict(allocation[order])})
        # print(formatted_allocation)
        return formatted_allocation
