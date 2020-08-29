"""
@author: Priyans Nishithkumar Desai

"""
def prepare_shipment(self):
    """
    Input: 
        self [Order] - An instance of the order class (the order)

    Output: 
        shipment_prepared [List[Warehouse]] - A list of warehouses used to satisfy the order. 

    Aim: Prepares a list of warehouses which can be used to satisfy the order placed. 
    """
    # Checking if all items in the order could be fulfilled with one warehouse
    all_in_warehouse_possibilities = {}
    for warehouse in self.available_warehouses:
        all_in_warehouse = 0
        for order_item in self.contents:
                
            # Checking if certain order item is available 
            availability = warehouse.check_availability(order_item)
            if availability >= order_item.quantity:
                all_in_warehouse += 1

        # If only the warehouse completely fulfills all items in the order, it is considered. 
        if all_in_warehouse == len(self.contents):
            all_in_warehouse_possibilities[warehouse] = warehouse.cost

        # If there are multiple warehouses that completely fulfill an order, 
        # choose the cheapest one.
        if all_in_warehouse_possibilities != {}:
            cheapest_warehouse = min(all_in_warehouse_possibilities, 
                key=lambda warehouse: all_in_warehouse_possibilities[warehouse])
        else:
            cheapest_warehouse = None

    for order_item in self.contents:

        # Keeps Track of all the warehouses visted for the particular order item
        visited_warehouses = []

        # Tracks if a warehouse can completely satisfy an order item's quantity. 
        found_warehouse = None

        # Length of the shipment before the contents of this item are added. 
        old_length = len(self.shipment)

        # If cheapest warehouse was found, use that
        if cheapest_warehouse:
            found_warehouse, quantity = cheapest_warehouse, order_item.quantity

        # Checks if the shipment being prepared contains warehouses that can fulfill this particular order item
        elif len(self.shipment) != 0:

            # returns the warehouse from the existing shipment that can completely 
            # fulfill the current order item or returns a combination of warehouses (in the shipment) 
            # that can partially/completely fulfill the order item. 
            complete_warehouse_ship, visited_warehouses, current_quantity, partial_completion = self.partial_or_complete(
                                                                order_item.quantity, order_item, visited_warehouses, True) 
                
            # If a warehouse that could completely fulfill the order is not found and 
            # some combination of warehouses from the shipment partially fulfilled the order
            if current_quantity != 0 and complete_warehouse_ship == None:

                # For whatever quantity is left, all the remaining warehouses (NOT IN THE CURRENT SHIPMENT)
                # are looked through 
                complete_warehouse, visited_warehouses, returned_quantity, partial_with_leftover = self.partial_or_complete(
                        current_quantity, order_item, visited_warehouses, False)

                # If there is a warehouse that fulfills the entire order quantity and the partial combination does 
                # not exist or contains more than warehouse to satisfy the leftover quantity, this complete warehouse is chosen.
                if complete_warehouse and len(partial_with_leftover) != 1:
                    found_warehouse, quantity = complete_warehouse, order_item.quantity
                    
                # If there is a warehouse that can completely satisfy the order quantity and
                # there is a warehouse that can satisfy the leftover quantity, then a cheaper one is chosen
                elif complete_warehouse and len(partial_with_leftover) == 1:
                    if complete_warehouse.cost < partial_with_leftover[0][0].cost:
                        found_warehouse, quantity = complete_warehouse, order_item.quantity
                    else:
                        found_warehouse, quantity = partial_with_leftover[0][0], current_quantity

                # If multiple warehouses are found that can fulfill this leftover order and no warehouse is found 
                # that can completely fulfill the entire quantity, then those warehouses are chosen. 
                elif complete_warehouse == None and len(partial_with_leftover) != 0:
                    self.add_warehouses_list(partial_with_leftover, self.shipment)

            # If a warehouse in the shipment that satisfies the order completely is found, then that is chosen. 
            elif complete_warehouse_ship:
                found_warehouse, quantity = complete_warehouse_ship, order_item.quantity

            # If a combination of warehouses in the shipment is found with no warehouse that can fulfill the order
            # then that is chosen. 
            elif current_quantity == 0:
                self.add_warehouses_list(partial_completion, self.shipment)

        # If the shipment is empty, then all the warehouses are looked through
        else:
            new_complete_warehouse, visited_warehouses, order_quantity, partial = self.partial_or_complete(order_item.quantity, order_item, 
                            [], False)
                
            # If a warehouse that can completely fulfill the order is found, that is chosen. 
            if new_complete_warehouse:
                found_warehouse, quantity = new_complete_warehouse, order_item.quantity

            # If a partial combination is found that can completely fulfill the order is found, 
            # then those warehouses are added to the shipment. 
            elif partial and order_quantity == 0:
                self.add_warehouses_list(partial, self.shipment)

        # If a warehouse is found, then the order item is added to the warehouse's individual shipment. 
        if found_warehouse:
            found_warehouse.add_shipment(order_item, quantity)

            # If the warehouse is not in the shipment, then it is added. 
            if found_warehouse not in self.shipment:
                self.shipment.append(found_warehouse)

        # If a new warehouse is added in the shipment, then the shipment is resorted according to their cost
        # smallest first. 
        if len(self.shipment) != old_length:
            old_length = len(self.shipment)
            sorted(self.shipment, key=lambda a: a.cost)

    shipment_prepared = self.shipment
    self.shipment = []
    return shipment_prepared

def partial_or_complete(self, order_quantity, order_item, visited_warehouses, shipment):
    """
    Input: 
        self [Order] - an instance of the order class (the order)
        order_quantity [int] - the amount of a particular item that need to be satisfied. 
        order_item [Item] - an instance of the Item class, the item that needs to be ordered. 
        visited_warehouses [List[Warehouse]] - a list of warehouses that have already been visited.
        shipment [boolean] - whether the current shipment is used or not to satisfy the order of this item.

    Output:
        complete_warehouse [Warehouse] - None if no warehouse was found to satisfy order completely, otherwise the
        warehouse that was found to satisfy the order
        visited_warehouses [List[Warehouse]] - An updated list of visited warehouses
        order_quantity (int) - Whatever of the quantity is left of the order
        partial_completion_possible [List[Warehouse]] - A list of warehouses if there are warehouses can be used to
        satisfy the order completely/partially. 

    Aim:
        Find a complete warehouses/a combination of warehouses to satisfy certain order quantity. 

    """
    # Indicates if a warehouse used to satisfy the order completely is found. 
    complete_warehouse = None

    # List of warehouses to satisfy order partially/completely
    partial_completion_possible = []

    # If shipment is true, we look for warehouses in the shipment, otherwise in all available warehouses.
    if shipment:
        look_into = self.shipment
    else:
        look_into = self.available_warehouses

    for warehouse in look_into:
        if warehouse not in visited_warehouses:

            # How much of the order item is available in the warehouse's inventory. 
            availability = warehouse.check_availability(order_item)

            # if a complete warehouse is found satisfying the entire order
            if availability >= order_item.quantity and not complete_warehouse:
                if shipment:
                    complete_warehouse = warehouse
                    break
                else:
                    complete_warehouse = warehouse

            # Check for partial satisfaction of the order_quantity
            elif availability != 0:
                if availability >= order_quantity:
                    order_quantity -= order_quantity
                    partial_completion_possible.append((warehouse, order_item, availability))
                    break
                else:
                    order_quantity -= availability
                    partial_completion_possible.append((warehouse, order_item, availability))
        visited_warehouses.append(warehouse)
    return complete_warehouse, visited_warehouses, order_quantity, partial_completion_possible

def add_warehouses_list(self, lst, shipment):
    """
    Input: 
        self [Order] - The current order
        lst  [List[Warehouse, Item of the order, Quantity]] - a list of (warehouse, the item and order quantity) 
        to edit the shipment of the warehouse. 
        shipment [List[Warehouse]] - shipment of this order

    Aim: 
        Adds items to the warehouse's shipment.
        Adds warehouse to the order's shipment if not there already
    """
    for warehouse in lst:

        # Adds the order_item to the warehouse's individual shipment
        warehouse[0].add_shipment(warehouse[1], warehouse[2])

        # Only adds warehouse to the order's shipment if not already there. 
        if warehouse[0] not in shipment:
            shipment.append(warehouse[0])





