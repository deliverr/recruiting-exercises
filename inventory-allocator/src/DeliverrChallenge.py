"""
Time Complexity - O(n*m) where n and m is size of orders and warehousedetails respectively
Space Complexity - O(m) where m is size of warehousedetails
"""

class InventoryAllocator:
    def cheapestShipment(self, orders, warehouseDetails):
        if len(orders) == 0 or len(warehouseDetails) == 0:
            return []

        shipment = list()
        for warehouse in warehouseDetails:
            maxOrderWarehouse = dict()

            for fruit, quantity in orders.items():
                # checking whether warehouse has facility to accept current order
                if warehouse["inventory"].get(fruit) and quantity > 0:
                    if quantity <= warehouse["inventory"][fruit]:

                        maxOrderWarehouse[fruit] = quantity
                        orders[fruit] = 0
                    else:
                        maxOrderWarehouse[fruit] = warehouse["inventory"][fruit]
                        orders[fruit] -= warehouse["inventory"][fruit]

            # appending the result to shipment if warehouse has appropriate facility
            if len(maxOrderWarehouse) > 0:
                shipment.append({warehouse["name"] : maxOrderWarehouse})

        # checking whether any item is remaining from the orders
        for item, quantity in orders.items():
            if quantity > 0:
                return []

        return shipment








