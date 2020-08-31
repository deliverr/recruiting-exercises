"""
@author: Priyans Nishithkumar Desai

"""

from Item import Item

class Order(object):

    """
    This is the implementation of the Order class, which processes an order received. 
    """

    def __init__(self, order_dict, available_warehouses):

        # A list of items (instances of the Item class) which need to be ordered
        self.contents = []

        # A list of warehouses (instances of the Warehouse class) 
        # that are available to complete the order
        self.available_warehouses = available_warehouses

        # A list containing warehouses which will complete the order. 
        self.shipment = []

        # Instantiating an instance of the Item class for every item in the order dictionary. 
        for (order_item, order_value) in order_dict.items():
            self.contents.append(Item(order_item, order_value))

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
            print(order_item.quantity)
            # If partial is found
            found_partial = False

            # Tracks if a warehouse can completely satisfy an order item's quantity. 
            found_warehouse = None

            # If cheapest warehouse was found, use that
            if cheapest_warehouse:
                found_warehouse, quantity = cheapest_warehouse, order_item.quantity

            # If no cheapest warehouse is found,s then all the warehouses are looked through
            else:
                new_complete_warehouse, order_quantity, partial = self.partial_or_complete(order_item.quantity, order_item)
                # If a warehouse that can completely fulfill the order is found, that is chosen. 
                print(new_complete_warehouse, partial)
                if new_complete_warehouse:
                    found_warehouse, quantity = new_complete_warehouse, order_item.quantity

                # If a partial combination is found that can completely fulfill the order is found, 
                # then those warehouses are added to the shipment. 
                elif partial and order_quantity == 0:
                    found_partial = True
                    self.add_warehouses_list(partial, self.shipment)

            
            # If any item remains unallocated, return empty shipment
            if found_warehouse == None and found_partial == False:
                return {}
            # If a warehouse is found, then the order item is added to the warehouse's individual shipment. 
            if found_warehouse:
                found_warehouse.add_shipment(order_item, quantity)

                # If the warehouse is not in the shipment, then it is added. 
                if found_warehouse not in self.shipment:
                    self.shipment.append(found_warehouse)

        shipment_prepared = self.shipment
        self.shipment = []
        return shipment_prepared

    def partial_or_complete(self, order_quantity, order_item):
        """
        Input: 
            self [Order] - an instance of the order class (the order)
            order_quantity [int] - the amount of a particular item that need to be satisfied. 
            order_item [Item] - an instance of the Item class, the item that needs to be ordered. 

        Output:
            complete_warehouse [Warehouse] - None if no warehouse was found to satisfy order completely, otherwise the
            warehouse that was found to satisfy the order
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

        for warehouse in self.available_warehouses:
            # How much of the order item is available in the warehouse's inventory. 
            availability = warehouse.check_availability(order_item)

            # if a complete warehouse is found satisfying the entire order
            if availability >= order_item.quantity:
                complete_warehouse = warehouse
                break

            # Check for partial satisfaction of the order_quantity

            # Check if order_quantity is greater than availability,
            # if that's the case, break. 
            elif availability >= order_quantity and order_quantity != 0:
                partial_completion_possible.append((warehouse, order_item, order_quantity))
                order_quantity = 0

            # If availabilty is not zero i.e. it is not a warehouse not containing the item or it has exhausted
            elif availability != 0 and order_quantity != 0:
                order_quantity -= availability
                partial_completion_possible.append((warehouse, order_item, availability))
        return complete_warehouse, order_quantity, partial_completion_possible

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





