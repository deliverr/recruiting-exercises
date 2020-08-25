from typing import List


class InventoryAllocator:
    def inventory_allocator(self, order: dict, stock: List[dict]):

        """

        Allocator method that produces the cheapest shipment based on the an order

        Arguments:
        :param order: dict
        :param stock: List[dict]
        :return: List[dict]

        """
        # Current order being updated through iterations
        shipment = []

        # Search for requested order in warehouses
        for warehouses in stock:

            # Setting local variables:
            # dictionary, unique list, and boolean to check if warehouse was already visited
            warehouse_supplies = dict()
            unique_order = set()
            warehouse_checked = False

            # NEED
            # HELP
            # HERE
            # Check for valid warehouse entry
            # if()

            # Checks and returns if an order is empty
            if not order:
                return shipment

            # Iterates to checks warehouses' stock
            for items in order:

                # Take appropriate stock
                if items in warehouses['stock']:
                    stocks_supplied = min(order[items], warehouses['stock'][items])
                    warehouses['stock'][items] -= stocks_supplied
                    order[items] -= stocks_supplied

                    # Mark what stock we took from a specific warehouses and update remaining items in order
                    if stocks_supplied > 0:
                        warehouse_checked = True
                    if order[items] == 0:
                        unique_order.add[items]
                    warehouse_supplies[items] = stocks_supplied

            # Add warehouses that contributed to completing the shipment
            if warehouse_checked:
                shipment.append({warehouse['name']: warehouse_supplies})
            # Update items in the shipment
            for items in unique_order:
                del order[items]

            #Not sure how to return this tbh
            return sorted(shipment)