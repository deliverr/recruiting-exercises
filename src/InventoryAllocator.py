class InventoryAllocator(object):

    
    def cheapest_shipment(self, items_ordered, warehouse_inventory_list):
        if items_ordered == {}:
            return []
        
        cheapest_shipment = []
        
        for w in warehouse_inventory_list:
            for warehouse, inventory in w.items():
                warehouse_list = {warehouse:{}}
                for item, amount in items_ordered.items():
                    for warehouse_item, stock in inventory.items(): 
                        if amount > 0 and stock > 0:
                            if item == warehouse_item and amount <= stock:
                                warehouse_list.get(warehouse).update({item:amount})
                                items_ordered.update({item:0})
                            elif item == warehouse_item and amount > stock:
                                warehouse_list.get(warehouse).update({item:stock})
                                amount -= stock
                                items_ordered.update({item:amount})
                if warehouse_list.get(warehouse) != {}:
                    cheapest_shipment.append(warehouse_list)
        
        
        for item, amount in items_ordered.items():
            if amount > 0:
                for warehouse_order in cheapest_shipment:
                    for warehouse, order in warehouse_order.items():
                        if item in order:
                            order.pop(item)     
                        if order == {}:
                            cheapest_shipment.remove(warehouse_order)
        
        return cheapest_shipment

            
            

            