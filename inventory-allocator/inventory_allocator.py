from constants import NAME, INVENTORY
from typing import Dict, List, Any


class Warehouse:
    def __init__(self, name : str, inventory : Dict[str, int]) -> None:
        self.name = name
        self.inventory = inventory


class InventoryAllocator:
    def inventory_allocator(self, orders: Dict[str, int],
                            warehouses: List[Dict[str, Any]]) -> List[Any]:
        """
        Inventory allocator method, which produces what each warehouse would ship based on the orders placed.
        
        Args:
        orders: Dict[str, int]              
                Orders dictionary with name of item : quantity
        warehouses: List[Dict[str, Any]]    
                    List of warehouses in dictionary format with two keys (name and inventory)

        Returns:
        res: List[Any] 
             Returns a list of warehouses containing what each warehouse will ship can be empty if order cannot be fulfilled

        """
        res = []
        # Return empty if no orders
        if not orders:
            return res

        # Iterate through each warehouse and try to fulfill as many orders and quantities as possible (since sorted by cost)
        for whouse in warehouses:
            # Check for a valid warehouse dictionary else raise an exception
            if (NAME not in whouse) or (INVENTORY not in whouse):
                raise ValueError('Inavlid warehouse.')
            # Convert warehouse to a typed object
            warehouse = Warehouse(whouse.get(NAME), whouse.get(INVENTORY))
            allocation = {warehouse.name: {}}
            for item, quantity in orders.items():
                # Item exists in warehouse and quanity > 0
                if warehouse.inventory.get(item, 0) > 0 and quantity > 0:
                    # If warehouse cannot produce enough for order so be greedy and take as much as possible and try to get
                    # the rest of the order quantity from another warehouse 
                    # Else this warehouse has enough in inventory for order so use this warehouse
                    if quantity > warehouse.inventory.get(item):
                        allocation[warehouse.name][item] = warehouse.inventory.get(item)
                        orders[item] -= warehouse.inventory.get(item)
                    else:
                        allocation[warehouse.name][item] = quantity
                        orders[item] = 0
            # Only insert into the result list if order or part of order can be fulfilled 
            if len(allocation.get(warehouse.name)) > 0:
                res.append(allocation)

        # Check if any quanity is > 0 -> if so then delete any allocation for it as order cannot be fulfilled (lack of inventory)
        for item, quantity in orders.items():
            if quantity > 0:
                for warehouse in res:
                    whouse_name = list(warehouse.keys())[0]
                    order_items = warehouse.get(whouse_name)
                    if item in order_items:
                        del order_items[item]
        
        # Filter out any empty warehouse objects in the result list
        res = list(
            filter(
                lambda warehouse: len(warehouse[list(warehouse.keys())[0]]) > 0, res))
        return res
