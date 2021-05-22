class InventoryAllocator:
    """
    Input:
        orderList: Dict { string : int }
        warehouses: List [ Dict { string : string, string : Dict { string : int } } ] 
        
    Output: 
        fulfillment: List [ Dict { string :  Dict { string : int } } ]
    """


    def fulfillOrder( self, orderList, warehouses):
        
        # if either order or warehouses are 0, return empty list
        if len(orderList) == 0 or len(warehouses) == 0 :
            return []

        # create a checklist which will reduce for every item fulfilled
        checklist = {}
        for item in orderList:
            if orderList[item] != 0 :
                checklist[item] = orderList[item]
        
        # stores fulfillment solution
        fulfillment = []
        
        # check stock of every warehouse
        for warehouse in warehouses:
            wareName = warehouse['name']
            inventory = warehouse['inventory']


            # optimization where this checks for every warehouse if it has enough stock to fulfill the entire order List instead of breaking the order to separate warehouses
            if all(item in list(inventory.keys()) for item in list(orderList.keys())):
                if all(orderList[item] <= inventory[item] for item in list(orderList.keys())):
                    cart = {wareName: orderList}
                    fulfillment = [cart]
                    checklist = {}
                    break


            # keeping the available item from the checklist into a cart for a specific warehouse location
            cart = {wareName: {}}

            # check whcih item in the checklist can be fulfilled by the warehouse
            for item in orderList:
                if (item in list(inventory.keys()) and item in list(checklist.keys())):
                    if inventory[item] > 0 and inventory[item] >= checklist[item] :
                        cart[wareName][item] = checklist[item]
                        del checklist[item]
                    elif inventory[item] > 0:
                        cart[wareName][item] = inventory[item]
                        checklist[item] -= inventory[item]

            # at the end of the inventory check, store whatever in the cart to the fulfillment solution
            if len(cart[wareName]) > 0:
                fulfillment.append(cart)

            # if there is no more item in checklist, no need to check other warehouses
            if len(checklist) == 0:
                break

        # if there are still some item left in the checklist, that means the item is not available on any warehouse, cancel order
        if len(checklist) > 0:
            return []


        return fulfillment