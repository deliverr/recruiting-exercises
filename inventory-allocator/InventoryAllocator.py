class InventoryAllocator:
    def __init__(self, order, warehouseList):
        self.order = order
        self.warehouseList = warehouseList

    def best_shipment(self):
        """ Return empty list if order/inventory cannot be fulfilled or lacks valid criteria """
        if self.order == {}:
            return []

        """ shipment will be a list resulting in orders from selected warehouses """
        shipment = list()

        """ Iterate through each warehouse and establish a dictionary for 
            each that is appeneded to shipment """
        for warehouse in self.warehouseList:
            warehouse_name = warehouse['name']
            warehouse_inventory = warehouse['inventory']
            warehouse_export = dict()

            """ Iterate through order to establish items and quantity that need to be supplied """
            for item in self.order:
                item_quantity = self.order[item]

                """ Establish which items match up to any given warehouse 
                    and ensure order/invetory amounts are not 0 """
                for item in warehouse_inventory:
                    if item_quantity > 0 and warehouse_inventory[item] > 0:

                        """ If the current order quantity is less than or equal to warehouse inventory,
                            order for item is fulfilled and order value is set to zero. Otherwise, the warehouse
                            exports remaining amount of the given item and value is subtracted from the order."""
                        if item_quantity <= warehouse_inventory[item]:
                            warehouse_export[item] = item_quantity
                            self.order[item] = 0
                        else:
                            warehouse_export[item] = warehouse_inventory[item]
                            self.order[item] -= warehouse_inventory[item]

            """ Append the supplies provided by each warehouse to shipment list """
            if warehouse_export != {}:
                shipment.append({warehouse_name: warehouse_export})
        return shipment
