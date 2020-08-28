from typing import List


class InventoryAllocator:
    def inventory_allocator(self, order: dict, stock: List[dict]):

        """
        Allocator method that produces the cheapest deliverry based on the an order
        Arguments:
        :param order: dict
        :param stock: List[dict]
        :return: List[dict]
        """
        # Current order being updated through iterations
        deliverry = []

        # Search for requested order in warehouses
        for warehouse in stock:

            warehouse_supplies = dict()

            # Checks and returns if an order is empty
            if not order:
                return deliverry

            # Iterates through warehouses' stock
            for items in order:

                if (type(order[items]) == type(0)) and (order[items] > 0):

                    # Take appropriate stock
                    if items in warehouse['inventory']:
                        stocks_supplied = min(order[items], warehouse['inventory'][items])
                        warehouse['inventory'][items] -= stocks_supplied
                        order[items] -= stocks_supplied

                        if stocks_supplied > 0:
                            warehouse_supplies[items] = stocks_supplied

            # Mark what stock we took from a specific warehouses and update remaining items in order
            if len(warehouse_supplies) > 0:
                deliverry.append({warehouse['name']: warehouse_supplies})

        return deliverry
