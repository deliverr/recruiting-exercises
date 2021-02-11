
class InventoryAllocator:

    def find_cheapest_shipment(self, requested_items, warehouse_inventory):
        self.final_shipment = []

        try:
            for warehouse in list(warehouse_inventory.keys()):
                self.items_to_ship = {}

                for item in requested_items: 
                    try: 
                        if requested_items[item] == 0 or warehouse_inventory[warehouse][item] == 0:
                            pass
                        elif requested_items[item] <= warehouse_inventory[warehouse][item]:
                            self.items_to_ship.update({item : requested_items[item]})
                            requested_items[item] = 0
                            warehouse_inventory[warehouse][item] = warehouse_inventory[warehouse][item] - requested_items[item]
                            
                        else:
                            self.items_to_ship.update({item : warehouse_inventory[warehouse][item]})
                            requested_items[item] = requested_items[item] - warehouse_inventory[warehouse][item]
                            warehouse_inventory[warehouse][item] = requested_items[item] - warehouse_inventory[warehouse][item]
                        
                    except KeyError:
                        pass 


                if len(self.items_to_ship) == 0: #second warehouse does not need to be used
                    del self.items_to_ship
                else: 
                    self.result_by_warehouse = {warehouse: self.items_to_ship}
                    self.final_shipment.append(self.result_by_warehouse)

            for item in requested_items:
                if requested_items[item] > 0: #full order could not be shipped - items are still missing
                    self.final_shipment.clear()
            
            return self.final_shipment
        
        except (NameError, TypeError):
            return "Please provide numerical value (int)"
