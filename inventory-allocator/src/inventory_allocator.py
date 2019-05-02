class InventoryAllocator:
    
    """
    Input:
        order: Dict(string->int)
            e.g. {'apple': 5, 'banana': 5}
        inventories: List(Dict(string->string, string->Dict(string->int)))
            e.g. [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10 }}]
        
    Output: 
        allocations: List(Dict(Dict(string->int)))
            e.g. [{'owd': {'apple': 1}}]
    """
    def allocateOrder(self, order, inventories):
        if len(order) == 0 or len(inventories) == 0:
            return []
        
        copiedOrder = order.copy()
        """
        Remove all the items with 0 quantity from copiedOrder.
        """
        def removeZeroItems(itemName):
            if copiedOrder[itemName] == 0:
                del copiedOrder[itemName]
        list(map(removeZeroItems, list(order.keys())))
        
        allocations = []
        itemNames = list(copiedOrder.keys())
        for invIndex in range(len(inventories)):
            inventory = inventories[invIndex]['inventory']
            invName = inventories[invIndex]['name']
            tempAllocation = {invName: {}}
            
            """
            Append to tempAllocation if inventories[invIndex] contains itemName (items in order).
            """
            def allocate(itemName):
                if itemName in inventory:                    
                    if inventory[itemName] > 0 and inventory[itemName] >= copiedOrder[itemName]:
                        tempAllocation[invName][itemName] = copiedOrder[itemName]
                        del copiedOrder[itemName]
                    elif inventory[itemName] > 0:
                        tempAllocation[invName][itemName] = inventory[itemName]
                        copiedOrder[itemName] -= inventory[itemName]
            list(map(allocate, list(copiedOrder.keys())))
            
            if len(tempAllocation[invName]) > 0:
                allocations.append(tempAllocation)
            if len(copiedOrder) == 0:
                break
        
        if len(copiedOrder) > 0:
            return []
        
        return allocations
