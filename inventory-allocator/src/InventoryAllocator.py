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

    def fulfillOrder( self, orderList, warehouses):
        
        if len(orderList) == 0 or len(warehouses) == 0 :
            return []

        checklist = {}
        for item in orderList:
            if orderList[item] != 0 :
                checklist[item] = orderList[item]

        fulfillment = []

        for warehouse in warehouses:
            wareName = warehouse['name']
            inventory = warehouse['inventory']

            cart = {wareName: {}}

            for item in orderList:
                if (item in list(inventory.keys()) and item in list(checklist.keys())):
                    if inventory[item] > 0 and inventory[item] >= checklist[item] :
                        cart[wareName][item] = checklist[item]
                        del checklist[item]
                    elif inventory[item] > 0:
                        cart[wareName][item] = inventory[item]
                        checklist[item] -= inventory[item]

            if len(cart[wareName]) > 0:
                fulfillment.append(cart)
            if len(checklist) == 0:
                break

        if len(checklist) > 0:
            return []

        #for item in orderList:

        #    for warehouse in warehouses:
        #        wareName = warehouse['name']
        #        inventory = warehouse['inventory']

        #        if inventory[item] > 0 and inventory[item] >= orderList[item]:

        return fulfillment