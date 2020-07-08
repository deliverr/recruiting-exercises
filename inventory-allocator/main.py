class itemAllocation():

    def itemAllocator(order, allocation):
        """
        Purpose of this function is to allocate the order into the appropriate warehouses
        
        Parameters:

        order (type: dictionary): A dictionary of orders with item names as keys and
        non-negative integers as the values.
        
        allocation (type: list of dictionaries): The key is the warehouse name and the 
        value is an object which has inventory information

        Output:

        A list of dictionaries, each dictionary will have the warehouse as key and 
        the amount of things they will store as value. If there isn't a possbile
        allocation, it will be empty
        """
        results = []
        if len(order) == 0:
            return results
        for warehouse in allocation:
            nameWarehouse = warehouse['name']
            inventory = warehouse['inventory']
            newAllocation = {nameWarehouse: {}}
            for item, space in inventory.items():
                if item in order and order[item] > 0 and space > 0:
                    if space >= order[item]:
                        newAllocation[nameWarehouse][item] = order[item]
                        del order[item]
                    else: 
                        newAllocation[nameWarehouse][item] = space
                        order[item] -= space
            if newAllocation[nameWarehouse] != {}:
                results.append(newAllocation)

        return results
