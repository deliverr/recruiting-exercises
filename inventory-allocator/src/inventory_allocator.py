
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


result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 15, 'orange': 30}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}, 'jak': {'apple': 3, 'orange': 3, 'banana':1}, 'ek': {'apple': 3, 'banana': 7, 'orange': 3}})
print(result)

'''

class InventoryAllocator:

    def find_cheapest_shipment(self, requested_items, warehouse_inventory):
        
        self.final_shipment = []
        self.requested_items = requested_items
        self.warehouse_inventory = warehouse_inventory
        
        try:
            for warehouse in list(self.warehouse_inventory.keys()):
                self.items_to_ship = {}

                for item in self.requested_items: 
                    try: 
                        if self.requested_items[item] <= self.warehouse_inventory[warehouse][item]:
                            self.items_to_ship.update({item : self.requested_items[item]})
                            self.requested_items[item] = 0
                            self.warehouse_inventory[warehouse][item] = self.warehouse_inventory[warehouse][item] - self.requested_items[item]
                        else:
                            self.items_to_ship.update({item : self.warehouse_inventory[warehouse][item]})
                            self.requested_items[item] = self.requested_items[item] - self.warehouse_inventory[warehouse][item]
                            self.warehouse_inventory[warehouse][item] = self.requested_items[item] - self.warehouse_inventory[warehouse][item]
                    except KeyError:
                        pass
                
                self.result_by_warehouse = {warehouse: self.items_to_ship}
                self.final_shipment.append(self.result_by_warehouse)

                
                if len(self.items_to_ship) == 0: #second warehouse does not need to be used
                    del self.items_to_ship
                else: 
                    self.result_by_warehouse = {warehouse: self.items_to_ship}
                    self.final_shipment.append(self.result_by_warehouse)
                

            for item in self.requested_items:
                if self.requested_items[item] > 0: #full order could not be shipped - items are still missing
                    self.final_shipment.clear()
                    #print(item + ": missing "+str(requested_items[item]))
            
            for item in self.final_shipment:
                if self.final_shipment[item] == 0:
                    del final_shipment[item]
            
            return self.final_shipment
        
        except (NameError, TypeError):
            return "Please provide numerical value (int)"

result = InventoryAllocator.find_cheapest_shipment(InventoryAllocator, {'apple': 3}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 5, 'orange': 3, 'banana':1}})
print(result)
'''
'''
class InventoryAllocator:

    def __init__(self, requested_items, warehouse_inventory):
        self.requested_items = requested_items
        self.warehouse_inventory = warehouse_inventory
        self.final_shipment = []
        self.find_cheapest_shipment(self.warehouse_inventory, self.requested_items)


    def find_cheapest_shipment(self, warehouse_inventory, requested_items):

        for warehouse in list(self.warehouse_inventory.keys()):
            self.items_to_ship = {}

            for item in self.requested_items: 
                try:
                    if self.requested_items[item] <= self.warehouse_inventory[warehouse][item]:
                        self.items_to_ship.update({item : self.requested_items[item]})
                        self.requested_items[item] = 0
                        self.warehouse_inventory[warehouse][item] = self.warehouse_inventory[warehouse][item] - self.requested_items[item]
                    
                    else:
                        self.items_to_ship.update({item : self.warehouse_inventory[warehouse][item]})
                        self.requested_items[item] = self.requested_items[item] - self.warehouse_inventory[warehouse][item]
                        self.warehouse_inventory[warehouse][item] = self.requested_items[item] - self.warehouse_inventory[warehouse][item]
        
                except KeyError:
                    pass 


            if len(self.items_to_ship) == 0: #second warehouse does not need to be used
                del self.items_to_ship
            else: 
                self.result_by_warehouse = {warehouse: self.items_to_ship}
                self.final_shipment.append(self.result_by_warehouse)

        for item in self.requested_items:
            if self.requested_items[item] > 0: #full order could not be shipped - items are still missing
                self.final_shipment.clear()
                print(item + ": missing "+str(self.requested_items[item]))
        
        print(self.final_shipment)


    
if __name__ == "__main__":
    
    
    
    try:
        #Test 1: Order includes non-numeric quantities in requested item.
        Output for all tests: Please provide correct input
        
        test1_1 = InventoryAllotment({'apple': x, 'orange': 3}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}})
            
        test1_2 = InventoryAllotment({'apple': '4dfd', 'orange': 3}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}})
        test1_3 = InventoryAllotment({'apple': 0, 'orange': 'dfd'}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}})
        #Test 2: Order can be shipped entirely using one warehouse.
        test2_1 = InventoryAllotment({'apple': 3, 'orange': 3}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
            #Output: [{'owd': {'apple': 3, 'orange': 3}}]
        test2_2 = InventoryAllotment({'orange': 5, 'banana': 1}, {'owd': {'apple': 3, 'orange': 5, 'banana': 1}})
            #Output: [{'owd': {'orange': 5, 'banana': 1}}]
        #Test 3: Order is shipped using multiple warehouses but all items are available
        test3_1 = InventoryAllotment({'apple': 10, 'orange': 3}, {'owd': {'apple': 5, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}}) 
            #Output: [{'owd': {'apple': 5, 'orange': 3}}, {'jak': {'apple': 5}}]

        #test2 = InventoryAllotment({'apple': 10, 'orange': 3}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}})
        #test3 = InventoryAllotment({'apple': 2}, {'owd': {'apple': 2, 'orange': 5, 'banana': 1}})
        #simple_test = InventoryAllotment({'apple': 2, 'orange': 2}, {'owd': {'apple': 8, 'orange': 5, 'banana': 1}})
        #simple_test = InventoryAllotment({'apple': 2, 'orange': 3}, {'owd': {'apple': 0, 'orange': 5, 'banana': 1}, 'jak': {'apple': 8}})
        #test_instance = InventoryAllotment({'apple': 2, 'orange': 0, 'grapes': 7, 'banana': 1}, {'owd': {'apple': 2, 'orange': 0, 'banana': 1}, 'jak': {'apple': 8, 'orange': 3, 'banana': 2}})

    except (NameError, TypeError):
        print("Please provide correct input")   
        pass
    '''