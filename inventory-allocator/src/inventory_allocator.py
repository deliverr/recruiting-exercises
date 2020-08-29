class InventoryAllocator:
    """
    A class used to allocate inventory based on a given order

    ...

    Attributes
    ----------
    order : dict
        A dictionary contianing items and their respective quantities
    warehouses : list
        A list of warehouses, with warehouses being formatted as dictionaries

    Methods
    -------
    check_valid(self)
        Checks the validity of the input parameters. 
        Raises an AssertionError if parameters are invalid

    allocate_inventory(self)
        Allocates inventory based on the stock available in the warehouses to satisfy the order. 
        Returns a list of items from their respective warehouses that satisfy the order.
    """


    def __init__(self, order, warehouses): 
        """
        Parameters
        ----------
        order : dict
            A dictionary contianing items and their respective quantities
        warehouses : list
            A list of warehouses, with warehouses being formatted as dictionaries
        """
        self.order = order
        self.warehouses = warehouses


    def check_valid(self):
        """Checks if the order and inventory are valid. 

        Raises
        ------
        AssertionError
            If the order or inventory values are invalid (ie. less than 0)
        """

        # Check each item in the order and assert it is larger than 0
        for item in self.order:
            assert self.order[item] >= 0, "An item in the order is invalid"
        
        # Check each item in each warehouse and assert it is larger than 0
        for warehouse in self.warehouses:
            for item in warehouse['inventory']:
                assert warehouse['inventory'][item] >= 0, "An item in the inventory is invalid"


    def allocate_inventory(self):
        """Allocates inventory based on the stock available in the warehouses to satisfy the order. 

        Raises
        ------
        AssertionError
            If the order or inventory values are invalid (ie. less than 0)
        """

        # Check if the input values are valid
        self.check_valid()

        # The final order output that is returned when the function is run
        order_output = []

        # Iterate through the warehouses list and identify the the name and inventory in each warehouse.
        for warehouse in self.warehouses:
            warehouse_name = warehouse['name']
            warehouse_inventory = warehouse['inventory']

            # For each warehouse, certain items are removed and added to the order output. 
            # This dict formats the order output for each warehouse and appends it to the order_output list.
            removed_form_warehouse = {}

            # The order is iterated through for each warehouse to identify the items which can be shipped 
            # from the current warehouse.
            for item_name in self.order:
                item_quantity_requested = self.order[item_name]

                # Check if the item name is in the warehouse inventory, if the item quantity is not 0 and 
                # if the warehouse quantity is not 0
                if item_name in warehouse_inventory and item_quantity_requested > 0 and warehouse_inventory[item_name] > 0:
                    
                    # Check if the quantity requested is greater than, equal to, or less than the warehouse 
                    # inventory available. 
                    # Depending on the case, different actions are performed to remove items from both the 
                    # warehouse and the order and are added to the order output. 
                    if item_quantity_requested > warehouse_inventory[item_name]:
                        removed_form_warehouse[item_name] = warehouse_inventory[item_name]
                        self.order[item_name] -= warehouse_inventory[item_name]
                        warehouse['inventory'][item_name] = 0
                    elif item_quantity_requested == warehouse_inventory[item_name]:
                        removed_form_warehouse[item_name] = warehouse_inventory[item_name]
                        warehouse['inventory'][item_name] = 0
                        self.order[item_name] = 0
                    else:
                        removed_form_warehouse[item_name] = item_quantity_requested
                        warehouse_inventory[item_name] -= item_quantity_requested
                        self.order[item_name] = 0
                
            # Check to see if items were removed from the current warehouse. If no items were removed, 
            # then the warehouse will not be added to the order_output
            if removed_form_warehouse:
                order_output.append({ warehouse_name: removed_form_warehouse })

        # Check to see if all items in the order have inventory allocated to them. If there remains 
        # unallocated inventory, return a blank list
        for item_name in self.order:
            if self.order[item_name] > 0:
                return []

        return order_output
                            

                    

