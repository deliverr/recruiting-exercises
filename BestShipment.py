class BestShipment():
    #the main function essentially
    #The order is the first input that tells us how many of each item we need
    #The warehouses is the second input that ells us the warehouse name and how many items it can ship
    def findBestShipment(self, order, warehouses):
        #we apply Greedy algorithms for each company
        solutionOrder = []
        for warehouse in warehouses:
            #warehouseStorage keeps track of the number of items being stored by that warehouse
            warehouseStorage = {}
            inventory = warehouse['inventory']
            for item in inventory:
                if item in order:
                    #If we can store more than the ordered number of items, we erase that item from the order dict;
                    #This way, we keep track of items we still need to ship
                    if inventory[item] >= order[item]:
                        warehouseStorage[item] = order[item]
                        del order[item]
                    #Otherwise if the warehouse does not have enough space for the items, we just simply use up all its space
                    #Then we make sure to keep track that we only need to store order[item] - inventory[item] left.
                    else:
                        warehouseStorage[item] = inventory[item]
                        order[item] = order[item] - inventory[item]
            #now we check if warehouseStorage is empty
            #in which case we just simply do not keep track of that (otherwise, it would be redundant to have {'a': {}} as part of the solution for example)
            #we do this by the fact that bool(dictionary) returns false iff dictionary is empty
            if not(bool(warehouseStorage)):
                continue
            #properWarehouseStorage is just of the form {name: warehouseStorage}
            #we name it proper because that is the output form that is proper.
            properWarehouseStorage = {}
            properWarehouseStorage[warehouse['name']] = warehouseStorage
            solutionOrder.append(properWarehouseStorage)
        #finally we check if there are still items left in the order
        #if none, we output solutionOrder (which is a list of the full inventory storage)
        #otherwise, we output an emptylist.
        #we do this by the fact that bool(dictionary) returns false iff dictionary is empty
        if bool(order):
            return []
        else:
            return solutionOrder


Test = BestShipment()




